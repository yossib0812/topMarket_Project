import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestSearchProductInCart(BaseTest):

    def test_names_item_in_cart(self):
        self.main_page.page.wait_for_load_state("networkidle")
        self.main_page.search_product("DELL Pro 14 Essential PV14250-5271 - 14")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()

        result = self.cart_page.get_cart_items_names("Essential PV14250-5271")

        assert result, f"Test Failed, the name item not fount in the cart"