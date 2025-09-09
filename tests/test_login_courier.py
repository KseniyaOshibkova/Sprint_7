import pytest
import allure
from data.create_courier_data import CreateCourierData

class TestCourierLogin:
    """Тесты на логин курьера"""

    @allure.title("Позитивная авторизация курьера")
    @allure.description("Проверить успешный логин курьера")
    def test_login_success(self, courier_api, random_courier):
        creds = {"login": random_courier["login"], "password": random_courier["password"]}

        with allure.step("Авторизоваться под созданным курьером"):
            response = courier_api.login_courier(creds)

        with allure.step("Проверить код ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что в ответе есть ключ 'id'"):
            assert "id" in response.json()


    @pytest.mark.parametrize(
        "description, creds, expected_status, expected_message",
        [
            ("Неправильный логин",
             {"login": "wrong_login", "password": CreateCourierData.LOGIN_COURIER["password"]},
             404, "Учетная запись не найдена"),

            ("Неправильный пароль",
             {"login": CreateCourierData.LOGIN_COURIER["login"], "password": "wrong_pass"},
             404, "Учетная запись не найдена"),

            ("Без логина",
             {"password": CreateCourierData.LOGIN_COURIER["password"]},
             400, "Недостаточно данных для входа"),

            ("Без пароля",
             {"login": CreateCourierData.LOGIN_COURIER["login"]},
             400, "Недостаточно данных для входа"),

            ("Несуществующий пользователь",
             {"login": CreateCourierData.NON_EXISTENT_USER["login"],
              "password": CreateCourierData.NON_EXISTENT_USER["password"]},
             404, "Учетная запись не найдена")
        ])
    @allure.title("Авторизация курьера — проверка ошибок")
    @allure.description("Проверка авторизации негативными сценариями")
    def test_login_errors(self, courier_api, description, creds, expected_status, expected_message):
        with allure.step(f"Сценарий: {description}"):
            response = courier_api.login_courier(creds)

        with allure.step("Проверить код ответа"):
            assert response.status_code == expected_status

        with allure.step("Проверить сообщение об ошибке"):
            assert expected_message in response.text
