import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestRemoveFromCart(BaseTest):

    def test_remove_product_from_cart(self):
        self.main_page.search_product("Apple iPad Air 11 (2024) - 11")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.search_product("Apple iPhone 17 Pro Max MFYT4 - 6.9")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.search_product("Lenovo Tab TB311XU - 10.1")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()

        num_product_before = self.item_page.get_num_of_cart_item()

        self.cart_page.decrease_quantity("Apple iPhone 17 Pro Max MFYT4 - 6.9")

        num_product_after = self.item_page.get_num_of_cart_item()

        assert num_product_after  == num_product_before - 1    , "Test Failed, "




