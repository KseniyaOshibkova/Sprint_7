


class CreateOrderData:
    """Тестовые данные для создания заказов"""

    BASE_ORDER = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "Saske, come back to Konoha"
    }

    COLORS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []  # без указания цвета
    ]