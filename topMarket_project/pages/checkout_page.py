from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    __CHECKOUT_PAGE_TITLE = ".ty-sidebox.ty-order-summary  [class^='ty-sidebox__title-wrapper h']"
    __EMAIL_FILL = "[name='user_data[email]']"
    __PASSWORD_FILL = "#password1"
    __CONFIRM_PASSWORD_FILL = "#password2"
    __FIRST_NAME_FILL = "[name='user_data[b_firstname]']"
    __LAST_NAME_FILL = "[name='user_data[b_lastname]']"
    __PHONE_FILL = "[name='user_data[b_phone]']"
    __ADDRESS_FILL = "[name='user_data[b_address]']"
    __CITY_FILL = "[name='user_data[b_city]']"
    __ZIP_FILL = "[name='user_data[b_zipcode]']"
    __ADDRESS_TO_SHIPPING_RADIO_BTN_NO = "[for='sw_sa_suffix_no']"
    __ADDRESS_TO_SHIPPING_RADIO_BTN_YES = "[for='sw_sa_suffix_yes']"
    __TERMS_AND_CONDITIONS_RADIO_BTN = "#id_accept_termstab1"
    __PERSONAL_DATA_RADIO_BTN = ".cm-field-container  #gdpr_agreements_checkout_place_order_tab1"
    __SUBMIT_MY_ORDER_BTN = ".litecheckout__submit-btn__caption"
    __SUMMARY_ITEM_TITLE= "[id^='checkout_info_summary_']"




    def verify_page(self):
        return self.get_text(self.__CHECKOUT_PAGE_TITLE)


    def entering_purchase_details(self, email, password, confirmPassword, firstName, lastName, phone, address, city, state, zip):
        self.fill_text(self.__EMAIL_FILL, email)
        self.fill_text(self.__PASSWORD_FILL, password)
        self.fill_text(self.__CONFIRM_PASSWORD_FILL, confirmPassword)
        self.fill_text(self.__FIRST_NAME_FILL, firstName)
        self.fill_text(self.__LAST_NAME_FILL, lastName)
        self.fill_text(self.__PHONE_FILL, phone)
        self.fill_text(self.__ADDRESS_FILL, address)
        self.fill_text(self.__CITY_FILL, city)
        self.fill_text(self.__ZIP_FILL, zip)
        self.click(self.__ADDRESS_TO_SHIPPING_RADIO_BTN_YES)
        self.click(self.__TERMS_AND_CONDITIONS_RADIO_BTN)
        self.click(self.__PERSONAL_DATA_RADIO_BTN)
        self.click(self.__SUBMIT_MY_ORDER_BTN)


    def get_summary_item(self):
        return self.get_text(self.__SUMMARY_ITEM_TITLE)








