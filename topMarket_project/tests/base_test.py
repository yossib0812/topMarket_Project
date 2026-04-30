import random
import string


from topMarket_project.pages.cart_page import CartPage
from topMarket_project.pages.checkout_page import CheckoutPage
from topMarket_project.pages.item_page import ItemPage
from topMarket_project.pages.main_page import MainPage
from topMarket_project.pages.order_page import OrderPage
from topMarket_project.pages.register_page import RegisterPage
from topMarket_project.pages.search_page import SearchPage
from topMarket_project.pages.terms_condition_page import TermsAndConditionPage


class BaseTest:
    cart_page : CartPage
    item_page : ItemPage
    main_page : MainPage
    register_page : RegisterPage
    search_page : SearchPage
    terms_condition_page : TermsAndConditionPage
    checkout_Page : CheckoutPage
    order_page : OrderPage

    def generate_random_email(self, length=8):
        letters_and_digits = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return f"{random_string}@gmail.com"


    def generate_random_phone(self, length=8):
        first_digits = "05"
        rest_of_the_number = ''.join(random.choice(string.digits) for i in range(8))
        return first_digits + rest_of_the_number

    def generate_random_name(self, length=5):
        letters_and_digits = string.ascii_lowercase
        random_string = ''.join(random.choice(letters_and_digits) for i in range(length))
        return random_string





