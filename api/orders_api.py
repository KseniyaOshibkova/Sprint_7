from api.urls import Urls



class OrdersApi:
    def __init__(self, client):
        self.client = client

    def create_order(self, data):
        """Создать заказ"""
        return self.client.post(Urls.CREATE_ORDER, json=data)

    def get_order_list(self, params=None):
        """Получить список заказов"""
        return self.client.get(Urls.LIST_ORDERS,  params=params)
