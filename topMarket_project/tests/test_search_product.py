import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestSearchProduct(BaseTest):

    def test_is_search_page(self):
        self.main_page.search_product("NVIDIA GeForce RTX 5060")
        title_page = self.search_page.verify_page()

        assert title_page == "Search results"  ,  f"Test Failed- you are in the wrong page "



    def test_search_product(self, page):
        one_result = self.main_page.search_product("ACER PREDATOR HELIOS NEO 16S AI NH.QX7EC.006 - 16")

        assert one_result , f"test failed- product does not found"

    def test_product_not_found(self):
        self.main_page.search_product_not_found("abcdefg")
        no_result = self.search_page.product_not_found()

        assert no_result == "No products found matching the search criteria", f"Test Failed-the product found"



