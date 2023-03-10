
from booking.src.SeleniumExtended import SeleniumExtended
from booking.src.pages.locators.PaymentPageLocators import PaymentPageLocators


class PaymentPage(PaymentPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def cc_number(self, cc_number=None):
        cc_number = cc_number if cc_number else '4321432112341234'
        self.sl.wait_and_input_text(self.NUMBER, cc_number)

    def brand(self):
        self.sl.wait_and_click(self.BRAND)

    def visa(self):
        self.sl.wait_and_click(self.VISA)

    def exp_month(self):
        self.sl.wait_and_click(self.EXPIRE_MONTH)

    def month(self):
        self.sl.wait_and_click(self.MONTH)

    def exp_year(self):
        self.sl.wait_and_click(self.EXPIRE_YEAR)

    def year(self):
        self.sl.wait_and_click(self.YEAR)

    def address(self, address=None):
        address = address if address else 'TestAddress'
        self.sl.wait_and_input_text(self.ADDRESS, address)

    def zip(self, zip=None):
        zip = zip if zip else 'TestZip'
        self.sl.wait_and_input_text(self.ZIP, zip)

    def city(self, city=None):
        city = city if city else 'TestCity'
        self.sl.wait_and_input_text(self.CITY, city)

    def state(self, state=None):
        state = state if state else 'TestState'
        self.sl.wait_and_input_text(self.STATE, state)

    def country(self):
        self.sl.wait_and_click(self.COUNTRY)

    def afghanistan(self):
        self.sl.wait_and_click(self.AFGHANISTAN)

    def submit(self):
        self.sl.wait_and_click(self.SUBMIT)
