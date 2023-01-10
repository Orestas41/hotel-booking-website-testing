
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.pages.locators.RoomPageLocators import RoomPageLocators

class RoomPage(RoomPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_most_expensive_option(self):
        self.driver.switch_to.frame(0)
        self.sl.wait_and_click(self.MOST_EXPENSIVE_OPTION_SELECT_BTN)
