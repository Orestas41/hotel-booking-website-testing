
from selenium.webdriver.common.by import By

class CheckoutPageLocators:

    ARRIVAL = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]')

    STAY = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]')

    DEPARTURE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[3]/div[2]')

    TYPE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[5]/div[2]')

    RATE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[6]/div[2]')

    EXTRAS = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[9]/div[2]')

    TOTAL = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[11]/div[2]/h3')

    EMAIL = (By.XPATH, '//*[@id="booking_guest_attributes_e_mail"]')

    LAST_NAME = (By.XPATH, '//*[@id="booking_guest_attributes_last_name"]')

    FIRST_NAME = (By.XPATH, '//*[@id="booking_guest_attributes_first_name"]')

    PHONE = (By.XPATH, '//*[@id="booking_guest_attributes_phone_number"]')

    CC = (By.XPATH, '//*[@id="booking_payment_service_credit_card_collect"]')

    AGREE = (By.XPATH, '//*[@id="booking_agreed"]')

    CREATE = (By.XPATH, '//*[@id="new_booking"]/div[5]/div[2]/div[3]/input')
