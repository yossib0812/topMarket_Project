import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestFeaturesProduct(BaseTest):

    def test_feature_product(self, page):
        self.main_page.search_product("Apple iPhone 17 Pro Max MFYU4A")
        self.search_page.choose_item()
        result = self.item_page.feature_product()


        assert result , f"Test Failed"





