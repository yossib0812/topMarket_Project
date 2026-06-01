
import time

from playwright.sync_api import Page

class BasePage:

    def __init__(self, page:Page):
        self.__page = page

    @property
    def page(self):
        return self.__page

    # __CART_BTN = ".ut2-top-cart-content"


    def click(self, locator):
        self.__page.locator(locator).highlight()
        self.__page.locator(locator).click()


    def fill_text (self, locator, text):
        self.__page.locator(locator).highlight()
        #time.sleep(1)
        self.__page.locator(locator).fill(text)

    def get_text(self, locator):
        self.__page.locator(locator).highlight()
        return self.__page.locator(locator).inner_text()

