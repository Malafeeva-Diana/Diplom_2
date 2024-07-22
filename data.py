class Data:
    Url_main_page = 'https://stellarburgers.nomoreparties.site/'
    Url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    Url_login_user = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    Url_changing_user_data = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    Url_create_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    Url_orders_from_user = 'https://stellarburgers.nomoreparties.site/api/orders'


class DataMy:

    name = 'Диана'
    email = "malafeeva_diana_06089@ya.ru"
    password = 'malafeeva_06'
    incorrect_password = 'TFJjw'
    incorrect_login = 'vasilii_1234444@ya.ru'


class BurgerIngredients:
    burger_existing = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    non_existent_burger = {'ingredients': ['35c0c5d1fр82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f']}
    burger_empty = {'ingredients': ''}
