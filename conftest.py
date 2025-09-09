import pytest
from api.api_client import ApiClient

from api.courier_api import CourierApi
from api.orders_api import OrdersApi
from helpers import register_new_courier_and_return_login_password


@pytest.fixture
def orders_api():
    client = ApiClient()
    return OrdersApi(client)

@pytest.fixture
def courier_api():
    client = ApiClient()
    return CourierApi(client)

@pytest.fixture
def cleanup_courier(courier_api):
    """Фикстура для удаления курьера после теста"""
    couriers = []
    yield couriers
    for creds in couriers:
        login_response = courier_api.login_courier({
            "login": creds["login"],
            "password": creds["password"]
        })
        courier_id = login_response.json().get("id")
        if courier_id:
            courier_api.delete_courier(courier_id)

@pytest.fixture
def random_courier():
    """Создаёт уникального курьера и возвращает его логин, пароль и имя"""
    login, password, first_name = register_new_courier_and_return_login_password()
    return {"login": login, "password": password, "firstName": first_name}
