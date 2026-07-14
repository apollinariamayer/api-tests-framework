import pytest
import allure
from models.user import User


@allure.feature('Users')
@allure.story('CRUD Operations')
class TestUsers:
    """Тесты для работы с пользователями (API: JSONPlaceholder)"""

    @allure.title('GET /users - получить всех пользователей')
    def test_get_all_users(self, api_client):
        """Проверка получения списка всех пользователей"""
        with allure.step('Отправляем GET запрос /users'):
            response = api_client.get('/users')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что вернулся список'):
            users = response.json()
            assert isinstance(users, list)
            assert len(users) > 0

        with allure.step('Проверяем структуру первого пользователя'):
            user = users[0]
            assert 'id' in user
            assert 'name' in user
            assert 'email' in user
            assert 'username' in user

        allure.attach(
            f"Найдено пользователей: {len(users)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /users/{id} - получить пользователя по ID')
    @pytest.mark.parametrize('user_id', [1, 2, 3, 4, 5])
    def test_get_user_by_id(self, api_client, user_id):
        """Проверка получения пользователя по ID"""
        with allure.step(f'Отправляем GET запрос /users/{user_id}'):
            response = api_client.get(f'/users/{user_id}')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем структуру пользователя'):
            user = response.json()
            assert user['id'] == user_id
            assert 'name' in user
            assert 'email' in user
            assert 'username' in user

        allure.attach(
            f"Пользователь: {user['name']} ({user['email']})",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('POST /users - создать нового пользователя')
    def test_create_user(self, api_client):
        """Проверка создания нового пользователя"""
        user_data = {
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@example.com",
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org"
        }

        with allure.step(f'Отправляем POST запрос /users с данными: {user_data}'):
            response = api_client.post('/users', data=user_data)

        with allure.step('Проверяем статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверяем, что пользователь создан'):
            user = response.json()
            assert 'id' in user
            assert user['name'] == user_data['name']
            assert user['email'] == user_data['email']

        allure.attach(
            f"Создан пользователь: ID={user['id']}, {user['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('POST /users - создать пользователя с разными данными')
    @pytest.mark.parametrize('name, email', [
        ('Alice Johnson', 'alice@example.com'),
        ('Bob Smith', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com')
    ])
    def test_create_user_with_different_data(self, api_client, name, email):
        """Проверка создания пользователей с разными данными"""
        user_data = {
            "name": name,
            "username": name.lower().replace(' ', ''),
            "email": email,
            "phone": "1-800-555-1234",
            "website": f"{name.lower().replace(' ', '')}.com"
        }

        with allure.step(f'Отправляем POST запрос /users с данными: {user_data}'):
            response = api_client.post('/users', data=user_data)

        with allure.step('Проверяем статус-код 201'):
            assert response.status_code == 201

        with allure.step('Проверяем, что пользователь создан'):
            user = response.json()
            assert user['name'] == name
            assert user['email'] == email

        allure.attach(
            f"Создан пользователь: {user['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('PUT /users/{id} - обновить существующего пользователя')
    @pytest.mark.parametrize('user_id', [1, 2, 3])
    def test_update_user(self, api_client, user_id):
        """Проверка обновления существующего пользователя"""
        update_data = {
            "id": user_id,
            "name": f"Updated User {user_id}",
            "username": f"updateduser{user_id}",
            "email": f"updated{user_id}@example.com",
            "phone": "1-800-555-0000",
            "website": "updated.com"
        }

        with allure.step(f'Отправляем PUT запрос /users/{user_id} с данными: {update_data}'):
            response = api_client.put(f'/users/{user_id}', data=update_data)

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что данные обновлены'):
            updated_user = response.json()
            assert updated_user['name'] == update_data['name']
            assert updated_user['email'] == update_data['email']

        allure.attach(
            f"Обновлён пользователь: {updated_user['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('DELETE /users/{id} - удалить пользователя')
    @pytest.mark.parametrize('user_id', [1, 2])
    def test_delete_user(self, api_client, user_id):
        """Проверка удаления пользователя"""
        with allure.step(f'Отправляем DELETE запрос /users/{user_id}'):
            response = api_client.delete(f'/users/{user_id}')

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        allure.attach(
            f"Пользователь {user_id} удалён",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /users/{id} - пользователь не найден')
    def test_user_not_found(self, api_client):
        """Проверка получения несуществующего пользователя"""
        user_id = 9999

        with allure.step(f'Отправляем GET запрос /users/{user_id}'):
            response = api_client.get(f'/users/{user_id}')

        with allure.step('Проверяем статус-код 404'):
            assert response.status_code == 404

        allure.attach(
            f"Пользователь {user_id} не найден (код {response.status_code})",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('PATCH /users/{id} - частично обновить пользователя')
    @pytest.mark.parametrize('user_id', [1, 2])
    def test_patch_user(self, api_client, user_id):
        """Проверка частичного обновления пользователя"""
        patch_data = {
            "name": f"Patched User {user_id}"
        }

        with allure.step(f'Отправляем PATCH запрос /users/{user_id} с данными: {patch_data}'):
            response = api_client.patch(f'/users/{user_id}', data=patch_data)

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что только имя обновлено'):
            updated_user = response.json()
            assert updated_user['name'] == patch_data['name']

        allure.attach(
            f"Частично обновлён пользователь: {updated_user['name']}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )

    @allure.title('GET /users - фильтрация по полю')
    def test_filter_users_by_email(self, api_client):
        """Проверка фильтрации пользователей по email"""
        target_email = 'Sincere@april.biz'

        with allure.step(f'Отправляем GET запрос /users?email={target_email}'):
            response = api_client.get('/users', params={'email': target_email})

        with allure.step('Проверяем статус-код 200'):
            assert response.status_code == 200

        with allure.step('Проверяем фильтрацию'):
            users = response.json()
            if users:
                assert users[0]['email'] == target_email

        allure.attach(
            f"Найдено пользователей: {len(users)}",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )