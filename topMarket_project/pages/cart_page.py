from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)


    __LIST_ITEM = "[class$='product-title']"
    __PRODUCT_LIST =  "[class^='ty-cart-content__product-elem ty-cart-content__i']"
    __DESCRIPTION_ITEM = "[class$='description__in']"
    __INCREASE_BTN = "[class$='increase']"
    __DECREASE_BTN = "[class$='decrease']"
    __CART_BTN = ".ut2-top-cart-content"
    __CLEAR_CART_BTN = "[class*='btn__outline ']"
    __EMPTY_PAGE_TITLE = ".ty-no-items"
    __CLOSE_CART_BTN = "#cart_main > div.buttons-container.ut2-cart-content__bottom-buttons.clearfix > div.ut2-cart-content__left-buttons > a.ty-btn.ty-btn__secondary > bdi"
    __GO_TO_MAIN_PAGE_BTN = ".top-logo > .ty-logo-container"
    __PROCEED_TO_CHECKOUT_BTN = "#cart_main > div.buttons-container.ut2-cart-content__bottom-buttons.clearfix > div.ut2-cart-content__right-buttons > a"
    __NEW_PRODUCT_LIST = "#cart_items > table > tbody > tr"
    __NEW_PRODUCT_TITLE = "[class$='product-title']"


    def count_product(self):
        product_list_area = self.page.locator(self.__LIST_ITEM)
        return product_list_area.count()


    def get_cart_items_names(self,name):
        product_list_area = self.page.locator(self.__LIST_ITEM)
        count = product_list_area.count()
        for i in range(count):
            title_product = product_list_area.nth(i).inner_text()
            if name in title_product:
                return True

        return  False

    def increase_quantity(self, name):
        self.page.wait_for_selector(self.__NEW_PRODUCT_LIST)
        product_list_area = self.page.locator(self.__NEW_PRODUCT_LIST)
        count = product_list_area.count()
        print("COUNT:", product_list_area.count())
        for i in range(count):
            product_title = product_list_area.nth(i).locator(self.__NEW_PRODUCT_TITLE).inner_text()
            if name.lower() in product_title.lower():
                increase_btn = product_list_area.nth(i).locator(self.__INCREASE_BTN)
                increase_btn.click()
                break


    def decrease_quantity(self, name):
        self.page.wait_for_selector(self.__NEW_PRODUCT_LIST)
        product_list_area = self.page.locator(self.__NEW_PRODUCT_LIST)
        count = product_list_area.count()

        for i in range(count):
            product_title = product_list_area.nth(i).locator(self.__NEW_PRODUCT_TITLE).inner_text()
            if name in product_title:
                decrease_btn = product_list_area.nth(i).locator(self.__DECREASE_BTN)
                decrease_btn.click()
                break


    def clear_cart(self):
        self.click(self.__CLEAR_CART_BTN)

    def close_cart(self):
        self.click(self.__CLOSE_CART_BTN)

    def get_empty_page_title(self):
        return self.get_text(self.__EMPTY_PAGE_TITLE)

    def go_to_home_page(self):
        self.click(self.__GO_TO_MAIN_PAGE_BTN)


    def proceed_to_checkout(self):
        return self.click(self.__PROCEED_TO_CHECKOUT_BTN)








