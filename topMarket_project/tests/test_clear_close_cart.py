import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestClearCart(BaseTest):

    def test_clear_cart(self):

        self.main_page.search_product("Apple iPad Mini (2021) - 8.3")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.clear_cart()

        assert self.cart_page.get_empty_page_title() == "Your cart is empty"   , "Test Failed, the cart not empty"


    def test_close_cart(self):
        self.main_page.search_product("Apple iPad Mini (2021) - 8.3")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.close_cart()

        assert self.main_page.get_num_of_cart_item()  == 1 , "Test Failed"
