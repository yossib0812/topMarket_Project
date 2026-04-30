from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __SEARCH_RESULT_TITLE = ".ty-mainbox-title__left"
    __PRODUCT_TITLE = ".ut2-gl__name > a"
    __NO_PRODUCT_TITLE = ".ty-no-items"
    __CART_BTN = ".ut2-top-cart-content"
    __PRODUCT_TITLE_LABEL = ".product_icon_lnk"



    def choose_item(self):
        item= self.page.locator(self.__PRODUCT_TITLE_LABEL).first
        item.wait_for(state="visible")
        item.click()

    def verify_page(self):
        return self.get_text(self.__SEARCH_RESULT_TITLE)

    def verify_item(self):
        return self.get_text(self.__PRODUCT_TITLE)

    def product_not_found(self):
        return self.get_text( self.__NO_PRODUCT_TITLE)

    def get_num_of_cart_item(self):
        self.page.wait_for_selector(self.__CART_BTN)
        text = self.get_text(self.__CART_BTN)
        return int(text) if text else 0






