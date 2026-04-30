

from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)


    __PRODUCT_LIST_AREA = ".ty-column6"
    __PRODUCT_TITLE_LABEL = "[class='product-title']"
    __ADD_TO_WISHLIST_BTN = "[id^='button_wishlist']"
    __X_BTN_OF_WISHLIST =".cm-notification-close"
    __WISHLIST_BTN = "[class$='favorite-border']"
    __FAVORITE_BTN = "[class$='favorite-border']"
    __ACCOUNT_BTN = "[id^='sw_dropdown_1'] > a"
    __REGISTER_BTN = "[class='ty-btn ty-btn__primary']"
    __SEARCH_FILL = "#search_input"
    __SEARCH_PRODUCT_BTN = "[title='Search']"
    __SEARCH_PRODUCT_TITLE = ".searched-categories"
    __SUBSCRIBE_FILL = "[id^='subscr_email']"
    __SUBSCRIBE_BTN = "[class^='ty-btn__subscribe']"
    __SUBSCRIBE_CHECKBOX_BTN = "[id$='agreements_newsletters_subscribe']"
    __SUBSCRIBE_MSG_INVALID_EMAIL = "[id^='subscr_email275_error']"
    __SUBSCRIBE_SUCCESS_ALERT = "[class^='cm-notification-content']"
    __SUBSCRIBE_ERROR_MSG_REDIO_BTN = "[id$='error_message']"
    __CART_BTN = ".ut2-top-cart-content"
    __VIEW_CART_BTN = ".ty-btn.ty-btn__outline"
    __POPUP_BTN = "[class$='btn-success']"
    __LIST_MENU_AREA = "[class$='footer-menu__item']"
    __TERMS_CONDITION_BTN = "[href$='privacy-policy/']"


    def choose_item(self, index=0):
        self.page.wait_for_selector(self.__PRODUCT_TITLE_LABEL)
        titles = self.page.locator(self.__PRODUCT_TITLE_LABEL)

        target_item = titles.nth(index)
        item_name = target_item.inner_text()
        target_item.click()

        return item_name


    def search_product(self, name):
        self.fill_text(self.__SEARCH_FILL, name)
        self.click(self.__SEARCH_PRODUCT_BTN)
        self.page.wait_for_selector(self.__SEARCH_PRODUCT_TITLE)
        count = self.page.locator(self.__SEARCH_PRODUCT_TITLE).count()
        return count == 1

    def search_product_not_found(self, name):
        self.fill_text(self.__SEARCH_FILL, name)
        self.click(self.__SEARCH_PRODUCT_BTN)


    def close_cookie_popup(self):
        popup_button = self.page.locator(self.__POPUP_BTN)
        if popup_button.is_visible():
            popup_button.click()

    def add_to_wishlist(self, name):
        product_list_area = self.page.locator(self.__PRODUCT_LIST_AREA)
        count = product_list_area.count()

        for i in range(count):
            title = product_list_area.nth(i).locator(self.__PRODUCT_TITLE_LABEL)

            if name in title.inner_text():
                product = product_list_area.nth(i)
                product.hover()
                wishlist_btn = product.locator(self.__ADD_TO_WISHLIST_BTN)
                wishlist_btn.click()
                self.page.wait_for_timeout(1000)
                close_btn = self.page.locator(self.__X_BTN_OF_WISHLIST)
                close_btn.click()
                self.page.wait_for_timeout(5000)
                break


    def get_num_of_wishlist_item(self):
        self.page.wait_for_selector(self.__WISHLIST_BTN)
        return self.get_text(self.__WISHLIST_BTN)

    def get_num_of_cart_item(self):
        self.page.wait_for_selector(self.__CART_BTN)
        text = self.get_text(self.__CART_BTN)

        if text:
            clean_text = text.split()[0]
            return int(clean_text)
        return 0


    def subscription_registration(self, userMail):
        self.fill_text(self.__SUBSCRIBE_FILL, userMail)
        self.click(self.__SUBSCRIBE_CHECKBOX_BTN)
        self.click(self.__SUBSCRIBE_BTN)

    def subscribe_success_alert(self):
        return self.get_text(self.__SUBSCRIBE_SUCCESS_ALERT)

    def subscribe_msg_invalid_email(self):
        return self.get_text(self.__SUBSCRIBE_MSG_INVALID_EMAIL)

    def subscribe_without_radio(self, userMail ):
        self.fill_text(self.__SUBSCRIBE_FILL, userMail)
        self.click(self.__SUBSCRIBE_BTN)

    def get_error_radio_btn_must(self ):
        return self.get_text(self.__SUBSCRIBE_ERROR_MSG_REDIO_BTN)


    def is_terms_conditions_page(self):
        list_menu_area = self.page.locator(self.__LIST_MENU_AREA)
        count = list_menu_area.count()

        for i in range(count):
            title = list_menu_area.nth(i)
            text = title.inner_text()

            if text == "Terms & Conditions":
                terms_condition_btn = list_menu_area.nth(i).locator(self.__TERMS_CONDITION_BTN)
                terms_condition_btn.click()
                break











