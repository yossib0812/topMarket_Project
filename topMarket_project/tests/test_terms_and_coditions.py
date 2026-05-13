import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestTermsAndConditions(BaseTest):

    def test_is_terms_and_conditions_page(self):
        self.main_page.is_terms_conditions_page()

        title_page = self.terms_condition_page.get_tittle_page()

        assert title_page == "Terms and Conditions" ,f"Test Failed, the page not found"










