import pytest
import allure
from utils.helpers import validate_response
from models.post import Post


@allure.feature('Posts')
@allure.story('CRUD Operations')
class TestPosts:
    """Тесты для работы с постами"""

    @allure.title('GET /posts - получить все посты')
    def test_get_all_posts(self, api_client):
        """Проверка получения списка всех постов"""
        with allure.step('Отправляем GET запрос /posts'):
            response = api_client.get('/posts')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что вернулся список'):
            posts = response.json()
            assert isinstance(posts, list)
            assert len(posts) > 0

        allure.attach(
            f"Найдено постов: {len(posts)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /posts/{id} - получить пост по ID')
    @pytest.mark.parametrize('post_id', [1, 2, 3, 4, 5])
    def test_get_post_by_id(self, api_client, post_id):
        """Проверка получения поста по ID"""
        with allure.step(f'Отправляем GET запрос /posts/{post_id}'):
            response = api_client.get(f'/posts/{post_id}')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем структуру поста'):
            post = response.json()
            assert post['id'] == post_id
            assert 'title' in post
            assert 'body' in post

        allure.attach(
            f"Пост: {post['title'][:50]}...",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('POST /posts - создать новый пост')
    def test_create_post(self, api_client, test_post_data):
        """Проверка создания нового поста"""
        with allure.step(f'Отправляем POST запрос /posts с данными: {test_post_data}'):
            response = api_client.post('/posts', data=test_post_data)

        with allure.step('Проверяем статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверяем, что пост создан'):
            post = response.json()
            assert 'id' in post
            assert post['title'] == test_post_data['title']
            assert post['body'] == test_post_data['body']

        with allure.step('Преобразуем в модель Post'):
            post_model = Post.from_dict(post)
            assert post_model.title == test_post_data['title']

        allure.attach(
            f"Создан пост: ID={post['id']}, {post['title'][:50]}...",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /posts - фильтрация постов по пользователю')
    def test_filter_posts_by_user(self, api_client):
        """Проверка фильтрации постов по userId"""
        user_id = 1

        with allure.step(f'Отправляем GET запрос /posts?userId={user_id}'):
            response = api_client.get('/posts', params={'userId': user_id})

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем фильтрацию'):
            posts = response.json()
            if posts:
                assert all(post['userId'] == user_id for post in posts)

        allure.attach(
            f"Найдено постов для пользователя {user_id}: {len(posts)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )