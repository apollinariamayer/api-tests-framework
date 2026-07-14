# 🚀 API Testing Framework

Профессиональный фреймворк для автоматизированного тестирования REST API.

## 📌 Описание
Фреймворк разработан для тестирования REST API с использованием Python, pytest и Allure. Все тесты проходят успешно.

## 🛠 Технологии
- Python 3.10
- pytest 8.0
- requests
- Allure Reports
- Faker
- Loguru

## 🧪 Что тестируется
- GET /users — получение всех пользователей
- GET /users/{id} — получение пользователя по ID
- POST /users — создание пользователя
- PUT /users/{id} — обновление пользователя
- PATCH /users/{id} — частичное обновление
- DELETE /users/{id} — удаление пользователя
- GET /posts — получение постов
- GET /comments — получение комментариев
- Фильтрация данных
- Обработка ошибок (404)

## 📊 Результаты
| Показатель | Значение |
|------------|----------|
| Всего тестов | 35 |
| Пройдено | 35 |
| Успешность | 100% |

## 🚀 Запуск
```bash
# 1. Установка зависимостей
pip install -r requirements.txt

# 2. Запуск всех тестов
pytest -v

# 3. Создание Allure отчёта
pytest --alluredir=reports/allure
allure serve reports/allure
```

##  📁 Структура проекта
```
api-tests-framework/
├── config/          # Настройки
├── core/            # Ядро (клиент, логгер)
├── models/          # Модели данных
├── tests/           # Тесты (35 штук)
├── utils/           # Утилиты
└── reports/         # Отчёты
```

## 📸 Скриншоты
https://allure-report.png

