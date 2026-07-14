import json
import os
from datetime import datetime
from typing import Any, Dict

def load_json_file(file_path: str) -> Dict:
    """Загружает JSON из файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_file(file_path: str, data: Any):
    """Сохраняет данные в JSON файл"""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_timestamp() -> str:
    """Возвращает текущую метку времени"""
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def ensure_dir(path: str):
    """Создаёт папку, если её нет"""
    os.makedirs(path, exist_ok=True)

def validate_response(response, expected_status: int = 200):
    """Проверяет статус-код ответа"""
    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}. Response: {response.text}"
    return response.json()