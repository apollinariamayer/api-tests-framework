import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Настройки приложения"""

    # Используем JSONPlaceholder (не требует API-ключа)
    BASE_URL = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com')

    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 30))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    REPORTS_DIR = 'reports'
    SCREENSHOTS_DIR = f'{REPORTS_DIR}/screenshots'


settings = Settings()