import pytest

from topMarket_project.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_function")
class TestRegister(BaseTest):

    def test_register_success(self):
        random_email = self.generate_random_email()
        self.main_page.subscription_registration(random_email)
        alert_success = self.main_page.subscribe_success_alert()


        assert "CONGRATULATIONS!" in alert_success ,  f"Test Failed- The email not registered"


    def test_invalid_email(self):
        random_name = self.generate_random_name()
        self.main_page.subscription_registration(random_name)
        error_invalid_email = self.main_page.subscribe_msg_invalid_email()

        assert error_invalid_email == "The email address in the Email field is invalid."  , f"Test Failed- no validation on email address"


    def test_radio_btn_must(self):
        random_email = self.generate_random_email()
        self.main_page.subscribe_without_radio(random_email)
        error_msg = self.main_page.get_error_radio_btn_must()

        assert error_msg == "Your agreement is required to proceed." , f"test Failed- radio btn is required"


