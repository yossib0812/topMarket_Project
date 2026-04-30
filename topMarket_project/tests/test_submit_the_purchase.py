import pytest

from topMarket_project.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_function")
class TestSubmitThePurchase(BaseTest):


    def test_verify_checkout_page(self):
        self.main_page.search_product("Lenovo ThinkBook 14 2-in-1 G4 21MX0019IV - 14")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.proceed_to_checkout()
        title = self.checkout_Page.verify_page()

        assert "order summary" in title.lower()   ,f"Test Failed: The page not found"


    def test_submit_successfully(self, page):
        self.main_page.search_product("ACER PREDATOR HELIOS NEO 16S AI NH.QX7EC.006 - 16")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.proceed_to_checkout()
        random_email = self.generate_random_email()
        random_phone = self.generate_random_phone()
        self.checkout_Page.entering_purchase_details( random_email, "12345!", "12345!", "Yo", "Bu", random_phone, "Herzel", "Tlv", "Center", "6100")
        title = self.order_page.get_title_page()

        assert  "congratulations! your order has been successfully placed"   in title.lower() , f"Test Failed- your order decline!"


    def test_mandatory_field(self):
        self.main_page.search_product("ACER PREDATOR HELIOS NEO 16S AI NH.QX7EC.006 - 16")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.proceed_to_checkout()
        random_email = self.generate_random_email()
        random_phone = self.generate_random_phone()
        self.checkout_Page.entering_purchase_details(random_email, "", "", "Yo", "Bu", random_phone, "Herzel", "Tlv", "Center", "6100")
        title = self.order_page.get_msg_mandatory_field()

        assert "field is mandatory" in title.lower()  , f"Test Failed- the email is not mandatory"


    def test_summary_item(self):
        self.main_page.search_product("Dyson Cyclone V10 Absolute - Wireless Vacuum Cleaner")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.search_product("ACER PREDATOR HELIOS NEO 16S AI NH.QX7EC.006 - 16")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.back_to_home_page()
        self.main_page.search_product("Lenovo ThinkBook 14 2-in-1 G4 21MX0019IV - 14")
        self.search_page.choose_item()
        self.item_page.add_to_cart()
        self.item_page.go_to_cart_page()
        self.cart_page.proceed_to_checkout()
        summary_item = self.checkout_Page.get_summary_item()

        assert  "3" in summary_item , f"Test Failed, there is no items here"