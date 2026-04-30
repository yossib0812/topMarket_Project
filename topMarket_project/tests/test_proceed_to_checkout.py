import pytest

from topMarket_project.tests.base_test import BaseTest



@pytest.mark.usefixtures("setup_page_function")
class TestProceedToCheckout(BaseTest):

    def test_proceed_to_checkout(self):
        self.main_page.search_product("Apple iPad Mini 2021 - 8.3")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.proceed_to_checkout()


        assert self.checkout_Page.verify_page().lower() == "order summary"    , "Test Failed- this is not the page"





