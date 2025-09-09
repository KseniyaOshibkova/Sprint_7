

class CreateCourierData:
    VALID_COURIER = {
        "login": "login_user_45677",
        "password": "pass456",
        "firstName": "Petya"
    }

    LOGIN_COURIER = {
        "login": "login_user_456",
        "password": "pass456",
        "firstName": "Petya"
    }

    DUPLICATE_COURIER = {
        "login": "duplicate_user2",
        "password": "123",
        "firstName": "Petya"
    }

    WITHOUT_LOGIN = {
        "password": "12345",
        "firstName": "NoLogin"
    }

    WITHOUT_PASSWORD = {
        "login": "nologin_user",
        "firstName": "NoPass"
    }

    WITHOUT_FIRST_NAME = {
        "login": "nofirstname_user",
        "password": "12345"
    }

    NON_EXISTENT_USER = {
        "login": "nonexistent_user",
        "password": "12345"
    }
