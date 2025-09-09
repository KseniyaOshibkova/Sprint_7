import allure



class TestListOrders:
    """Тесты на список заказов"""

    @allure.title("Получение списка заказов")
    @allure.description("Проверяем, что эндпоинт получения списка заказов возвращает список заказов и статус код 200")
    def test_get_order_list(self, orders_api):
        with allure.step("Отправка запроса на получение списка"):
            response = orders_api.get_order_list()
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Десереализайция ответа"):
            data = response.json()
        with allure.step("Проверка содержания ответа по ключу 'orders'"):
            assert "orders" in data
        with allure.step("Проверка типа ответа на 'list'"):
            assert isinstance(data["orders"], list)
