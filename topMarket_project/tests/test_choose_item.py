import time

import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestChooseItem(BaseTest):

    def test_choose_item(self, page):

        item_name = self.main_page.choose_item()
        time.sleep(2)
        item_page = self.item_page.get_title_item()


        assert item_name in item_page , f"Test failed- The product not found"


