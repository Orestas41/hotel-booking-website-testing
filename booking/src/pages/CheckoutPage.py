
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.helpers.generic_helpers import generate_random_email_and_password
from booking.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def arrival(self):
        arrival = self.sl.wait_get_elements(self.ARRIVAL).text
        return arrival

    def stay(self):
        stay = self.sl.wait_get_elements(self.STAY).text
        return stay

    def departure(self):
        departure = self.sl.wait_get_elements(self.DEPARTURE).text
        return departure

    def type(self):
        type = self.sl.wait_get_elements(self.TYPE).text
        return type

    def rate(self):
        rate = self.sl.wait_get_elements(self.RATE).text
        return rate

    def extra(self):
        extra = self.sl.wait_get_elements(self.EXTRAS).text
        return extra

    def total(self):
        total = self.sl.wait_get_elements(self.TOTAL).text
        return total

    def email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.EMAIL, email)

    def last_name(self, last_name=None):
        last_name = last_name if last_name else 'TestLastName'
        self.sl.wait_and_input_text(self.LAST_NAME, last_name)

    def first_name(self, first_name=None):
        first_name = first_name if first_name else 'TestFirstName'
        self.sl.wait_and_input_text(self.FIRST_NAME, first_name)

    def phone(self, phone=None):
        phone = phone if phone else '0000000000'
        self.sl.wait_and_input_text(self.PHONE, phone)

    def cc(self):
        self.sl.wait_and_click(self.CC)

    def agree(self):
        self.sl.wait_and_click(self.AGREE)

    def create(self):
        self.sl.wait_and_click(self.CREATE)
