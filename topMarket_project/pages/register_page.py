from playwright.sync_api import Page

from topMarket_project.pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)

    __ACCOUNT_WINDOW = ".ut2-account-info__avatar"
    __PHONE_FILL = "[name='user_data[phone]']"
    __EMAIL_FILL = "#email"
    __PASSWORD_FILL = "#password1"
    __CONFIRM_PASSWORD_FILL = "#password2"
    __I_AGREE_BTN = "[class$='agreement checkbox']"
    __REGISTER_BTN = "[class='ty-btn__secondary ty-btn']"


    def registered_success(self,phone, email, password, secondPassword ):
        self.fill_text(self.__PHONE_FILL, phone)
        self.fill_text(self.__EMAIL_FILL, email)
        self.fill_text(self.__PASSWORD_FILL, password)
        self.fill_text(self.__CONFIRM_PASSWORD_FILL, secondPassword)
        self.click(self.__I_AGREE_BTN)
        frame = self.page.frame_locator("recaptcha_6910e9bcc7886 > iframe")
        frame.locator("#recaptcha-anchor > div.recaptcha-checkbox-border").click()
        self.click(self.__REGISTER_BTN)



