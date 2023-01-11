
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.pages.locators.ExtrasPageLocators import ExtrasPageLocators


class ExtrasPage(ExtrasPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_cleaning(self, number='1'):
        self.sl.wait_and_input_text(self.CLEANING, number)

    def input_fitness(self, number='1'):
        self.sl.wait_and_input_text(self.FITNESS, number)

    def click_add(self):
        self.sl.wait_and_click(self.ADD_EXTRAS_BTN)
