from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class TermsAndConditionPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)



    def get_tittle_page(self):
        return self.page.get_by_role("heading", name="Terms and Conditions").inner_text()



