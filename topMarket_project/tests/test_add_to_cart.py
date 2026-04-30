import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestAddToCart(BaseTest):

    def test_add_to_cart(self, page):
        self.main_page.search_product("DELL Latitude 3450 L3450-5086 - 14")
        self.search_page.choose_item()
        num_in_cart = int(self.item_page.get_num_of_cart_item())
        self.item_page.add_to_cart()

        assert int(self.item_page.get_num_of_cart_item()) == num_in_cart+1  , f"Test add_to_cart1- Failed"


    def test_add_to_cart2(self, page):
        self.main_page.search_product("Dyson V15s Detect Submarine - Wireless Vacuum Cleaner, Yellow/Grey")
        self.search_page.choose_item()
        num_in_cart = int(self.item_page.get_num_of_cart_item())
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.search_product("Apple iPhone 17 Pro Max MFYN4 - 6.9")
        self.search_page.choose_item()
        self.item_page.add_to_cart()

        assert int(self.item_page.get_num_of_cart_item()) == num_in_cart+2  , f"Test add_to_cart1- Failed"




