
from booking.src.helpers.config_helpers import get_base_url
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_date_field(self):
        self.sl.wait_and_click(self.DATE_FIELD)

    def click_date(self):
        self.sl.wait_and_click(self.DAY)

    def input_nights(self, nights=None):
        self.sl.wait_and_input_text(self.NIGHTS, nights)

    def click_book(self):
        self.sl.wait_and_click(self.BOOK_BTN)