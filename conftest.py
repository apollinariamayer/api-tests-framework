import pytest
from core.api_client import APIClient
from config.settings import settings
from utils.data_generators import DataGenerator
from utils.helpers import ensure_dir
import allure

# Создаём папку для отчётов
ensure_dir(settings.REPORTS_DIR)
ensure_dir(settings.SCREENSHOTS_DIR)

@pytest.fixture(scope='session')
def api_client():
    """Фикстура для клиента API"""
    return APIClient()

@pytest.fixture
def test_user_data():
    """Фикстура с данными тестового пользователя"""
    return DataGenerator.generate_user()

@pytest.fixture
def test_post_data():
    """Фикстура с данными тестового поста"""
    return DataGenerator.generate_post()

@pytest.fixture
def created_user(api_client):
    """Создаёт пользователя для тестов и удаляет после"""
    user_data = DataGenerator.generate_user()
    response = api_client.post('/users', data=user_data)
    user = response.json()
    yield user
    # Очистка после теста
    api_client.delete(f'/users/{user["id"]}')

@pytest.fixture
def created_post(api_client):
    """Создаёт пост для тестов и удаляет после"""
    post_data = DataGenerator.generate_post()
    response = api_client.post('/posts', data=post_data)
    post = response.json()
    yield post
    # Очистка после теста
    api_client.delete(f'/posts/{post["id"]}')