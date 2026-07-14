import pytest
import allure
from utils.data_generators import DataGenerator


@allure.feature('Comments')
@allure.story('Read Operations')
class TestComments:
    """Тесты для работы с комментариями"""

    @allure.title('GET /comments - получить все комментарии')
    def test_get_all_comments(self, api_client):
        """Проверка получения списка всех комментариев"""
        with allure.step('Отправляем GET запрос /comments'):
            response = api_client.get('/comments')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что вернулся список'):
            comments = response.json()
            assert isinstance(comments, list)
            assert len(comments) > 0

        allure.attach(
            f"Найдено комментариев: {len(comments)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /comments/{id} - получить комментарий по ID')
    @pytest.mark.parametrize('comment_id', [1, 2, 3, 4, 5])
    def test_get_comment_by_id(self, api_client, comment_id):
        """Проверка получения комментария по ID"""
        with allure.step(f'Отправляем GET запрос /comments/{comment_id}'):
            response = api_client.get(f'/comments/{comment_id}')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем структуру комментария'):
            comment = response.json()
            assert comment['id'] == comment_id
            assert 'name' in comment
            assert 'email' in comment
            assert 'body' in comment

        allure.attach(
            f"Комментарий: {comment['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /comments - фильтрация комментариев по посту')
    def test_filter_comments_by_post(self, api_client):
        """Проверка фильтрации комментариев по postId"""
        post_id = 1

        with allure.step(f'Отправляем GET запрос /comments?postId={post_id}'):
            response = api_client.get('/comments', params={'postId': post_id})

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем фильтрацию'):
            comments = response.json()
            if comments:
                assert all(comment['postId'] == post_id for comment in comments)

        allure.attach(
            f"Найдено комментариев для поста {post_id}: {len(comments)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('POST /comments - создать комментарий')
    def test_create_comment(self, api_client):
        """Проверка создания комментария"""
        comment_data = DataGenerator.generate_comment()

        with allure.step(f'Отправляем POST запрос /comments с данными: {comment_data}'):
            response = api_client.post('/comments', data=comment_data)

        with allure.step('Проверяем статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверяем, что комментарий создан'):
            comment = response.json()
            assert 'id' in comment
            assert comment['name'] == comment_data['name']

        allure.attach(
            f"Создан комментарий: ID={comment['id']}, {comment['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )