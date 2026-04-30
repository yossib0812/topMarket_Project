from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    __TITLE_PAGE = ".ty-checkout-complete__order-success"
    __MSG_MANDATORY_FIELD = "#password1_error_message"


    def get_title_page(self):
        return self.get_text(self.__TITLE_PAGE)

    def get_msg_mandatory_field(self):
        return self.get_text(self.__MSG_MANDATORY_FIELD)


