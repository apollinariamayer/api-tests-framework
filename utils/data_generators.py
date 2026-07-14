from faker import Faker
import random

fake = Faker('ru_RU')  # Русскоязычные данные


class DataGenerator:
    """Генератор тестовых данных"""

    @staticmethod
    def generate_user():
        """Генерирует случайного пользователя"""
        return {
            'name': fake.name(),
            'username': fake.user_name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'website': fake.url()
        }

    @staticmethod
    def generate_post(user_id: int = None):
        """Генерирует случайный пост"""
        return {
            'userId': user_id or random.randint(1, 10),
            'title': fake.sentence(nb_words=5),
            'body': fake.paragraph(nb_sentences=3)
        }

    @staticmethod
    def generate_comment(post_id: int = None):
        """Генерирует случайный комментарий"""
        return {
            'postId': post_id or random.randint(1, 10),
            'name': fake.sentence(nb_words=3),
            'email': fake.email(),
            'body': fake.paragraph(nb_sentences=2)
        }

    @staticmethod
    def generate_todo(user_id: int = None):
        """Генерирует случайную задачу"""
        return {
            'userId': user_id or random.randint(1, 10),
            'title': fake.sentence(nb_words=4),
            'completed': random.choice([True, False])
        }