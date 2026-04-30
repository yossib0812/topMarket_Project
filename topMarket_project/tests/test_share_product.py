import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestShareProduct(BaseTest):

    def test_share_product(self):
        self.main_page.search_product("Apple iPad Air 11 (2024) - 11")
        self.search_page.choose_item()
        self.item_page.share_product()
        result = self.item_page.contains_social()


        assert result , "Test Failed: No social share option was found"

