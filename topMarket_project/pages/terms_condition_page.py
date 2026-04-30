from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class TermsAndConditionPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)


    __TITLE_PAGE = "[role='heading']"


    def get_title_page(self):
        return self.get_text(self.__TITLE_PAGE)

    def is_not_the_right_page(self):
        return self.get_text(self.__)



