import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestViewCart(BaseTest):

    def test_view_cart(self ):

        self.main_page.search_product("Apple iPad Mini 2021 - 8.3")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.page.wait_for_load_state("networkidle")
        self.main_page.search_product("Apple iPhone 17 Pro Max MFYT4 - 6.9")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.page.wait_for_load_state("networkidle")
        self.main_page.search_product("DELL Pro 14 Essential PV14250-5271 - 14")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()

        count_product_in_cart = self.cart_page.count_product()

        assert count_product_in_cart == 3 , f"Test Failed- you dont have all the products"








