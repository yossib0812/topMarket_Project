import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestAddQuantityInCart(BaseTest):

    def test_add_quantity_in_cart(self):
        self.main_page.search_product("Dyson Cyclone V10 Absolute - Wireless Vacuum Cleaner, Blue/Grey")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.page.wait_for_load_state("networkidle")
        self.main_page.search_product("Apple iPad Mini 2021 - 8.3 Display, 4GB RAM, 64GB Storage, Wi-Fi + Cellular")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        count_before = self.item_page.get_num_of_cart_item()   #2

        self.cart_page.increase_quantity("Dyson Cyclone V10 Absolute - Wireless Vacuum Cleaner, Blue/Grey")
        count_after = self.item_page.get_num_of_cart_item()    #3
        assert count_after  == count_before + 1   , f"Test Failed- The quantity not increase"


