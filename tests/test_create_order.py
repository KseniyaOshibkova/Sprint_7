import allure
import pytest

from data.create_order_data import CreateOrderData


class TestListOrders:
    """Тесты на создание заказов"""

    @allure.title("Создание заказа самоката")
    @allure.description("Проверяем, что можно сделать заказ c разными параметрами выбора цвета самоката")
    @pytest.mark.parametrize("color", CreateOrderData.COLORS)
    def test_create_order_with_color(self, orders_api, color):
        with allure.step("Отправка запроса на заказ самоката"):
            order_data = {**CreateOrderData.BASE_ORDER, "color": color}

            with allure.step("Отправка запроса на создание заказа"):
                response = orders_api.create_order(order_data)

            with allure.step("Проверка кода ответа"):
                assert response.status_code == 201

            with allure.step("Десериализация ответа"):
                data = response.json()

            with allure.step("Проверка, что в ответе есть track"):
                assert "track" in data
                assert isinstance(data["track"], int)

            with allure.step("Проверка корректности цвета"):
                for c in color:
                    assert c in {"BLACK", "GREY"}
