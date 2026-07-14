#!/usr/bin/env python
"""
Скрипт для запуска тестов с различными опциями
"""

import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path


def run_tests(markers: str = "", allure: bool = True, parallel: bool = False):
    """Запускает тесты"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = f"reports/allure_{timestamp}"

    # Формируем команду
    cmd = ["pytest"]

    # Добавляем маркеры
    if markers:
        cmd.extend(["-m", markers])

    # Параллельный запуск
    if parallel:
        cmd.extend(["-n", "auto"])

    # Allure отчёт
    if allure:
        cmd.extend(["--alluredir", report_dir])

    cmd.append("-v")
    cmd.append("-s")

    # Запускаем
    print(f"🚀 Запуск тестов: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)

    if allure:
        print(f"\n📊 Allure отчёт сохранён в: {report_dir}")
        print("Для просмотра отчёта выполните:")
        print(f"  allure serve {report_dir}")

    return result.returncode


if __name__ == "__main__":
    # Парсим аргументы командной строки
    args = sys.argv[1:]
    markers = ""
    allure = True
    parallel = False

    for arg in args:
        if arg.startswith("--markers="):
            markers = arg.split("=")[1]
        elif arg == "--no-allure":
            allure = False
        elif arg == "--parallel":
            parallel = True

    exit_code = run_tests(markers, allure, parallel)
    sys.exit(exit_code)