

import pytest
from playwright.sync_api import Page

from topMarket_project.pages.cart_page import CartPage
from topMarket_project.pages.checkout_page import CheckoutPage
from topMarket_project.pages.item_page import ItemPage
from topMarket_project.pages.main_page import MainPage
from topMarket_project.pages.order_page import OrderPage
from topMarket_project.pages.register_page import RegisterPage
from topMarket_project.pages.search_page import SearchPage
from topMarket_project.pages.terms_condition_page import TermsAndConditionPage



@pytest.fixture(scope="class")     #autouse=True
def setup_page_class(request, browser):
    page = browser.new_page()
    page.set_default_timeout(15000)
    page.goto("https://www.topmarket.co.il/en/")
    request.cls.cart_page = CartPage(page)
    request.cls.item_page = ItemPage(page)
    request.cls.main_page = MainPage(page)
    request.cls.register_page = RegisterPage(page)
    request.cls.search_page = SearchPage(page)
    request.cls.terms_condition_page = TermsAndConditionPage(page)
    request.cls.checkout_Page = CheckoutPage(page)
    request.cls.order_page = OrderPage(page)


    yield
    page.close()



@pytest.fixture(scope="function" )   #autouse=True
def setup_page_function(request, page: Page):
    page.set_default_timeout(15000)
    page.goto("https://www.topmarket.co.il/en/")
    request.cls.cart_page = CartPage(page)
    request.cls.item_page = ItemPage(page)
    request.cls.main_page = MainPage(page)
    request.cls.register_page = RegisterPage(page)
    request.cls.search_page = SearchPage(page)
    request.cls.terms_condition_page = TermsAndConditionPage(page)
    request.cls.checkout_Page = CheckoutPage(page)
    request.cls.order_page = OrderPage(page)
    yield
    page.close()


