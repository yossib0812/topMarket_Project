from playwright.sync_api import Page, expect

from topMarket_project.pages.base_page import BasePage


class ItemPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    __PRODUCT_TITLE_LABEL = "[class^='ut2-pb__title']"
    __NEW_BUY_BTN = "button.ty-btn__add-to-cart"
    __CLOSE_BAY_BTN = "[class$='btn__secondary cm-notification-close ']"
    __CART_BTN = ".ut2-top-cart-content"
    __VIEW_CART_BTN = ".ty-btn__outline:has-text('View cart')"
    __BACK_TO_HOME_PAGE_BTN = "div.top-logo > div > a"
    __SHARE_BTN = ".ut2-icon-share"
    __SHARE_LIST_AREA = ".social-buttons"
    __FEATURE_BTN = "#features"
    __FEATURE_LIST_AREA = ".ty-product-feature-group"


    def add_to_cart(self):
        self.page.locator(self.__NEW_BUY_BTN).first.click()
        self.page.locator(self.__CLOSE_BAY_BTN)

    def get_title_item(self):
        return self.get_text(self.__PRODUCT_TITLE_LABEL)

    def go_to_cart_page(self):
        self.click(self.__CART_BTN)
        self.click(self.__VIEW_CART_BTN)

    def back_to_home_page(self):
        self.click(self.__BACK_TO_HOME_PAGE_BTN)

    def share_product(self):
        self.click(self.__SHARE_BTN)

    def contains_social(self):
        share_buttons = self.page.locator(".social-buttons a")
        count = share_buttons.count()
        share_buttons.first.wait_for()

        social_keywords = {  "whatsapp", "facebook", "telegram","twitter", "mailto"  }
        found = set()

        for i in range(count):
            href = (share_buttons.nth(i).get_attribute("href") or "").lower()
            for keyword in social_keywords:
                if keyword in href:
                    found.add(keyword)
        return len(found) >= 3

    def feature_product(self):
        self.click(self.__FEATURE_BTN)
        feature_list_area = self.page.locator(self.__FEATURE_LIST_AREA)
        count = feature_list_area.count()

        for i in range(count):
            detail_product = feature_list_area.nth(i).locator(".ty-subheader")
            detail_product = detail_product.inner_text()

            if "Performance" in detail_product or "Software" in detail_product:
                return True
                break

        return False


    def get_num_of_cart_item(self):
        cart_locator = self.page.locator(self.__CART_BTN)
        expect(cart_locator).not_to_have_text("0", timeout=5000)
        text = self.get_text(self.__CART_BTN)

        if text:
            parts = text.split()
            if parts and parts[0].isdigit():
                return int(parts[0])
        return 0









