
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.pages.locators.ConfirmationPageLocators import ConfirmationPageLocators

class ConfirmationPage(ConfirmationPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def confirmation(self):
        confirmation = self.sl.wait_get_elements(self.CONFIRMATION).text
        return confirmation