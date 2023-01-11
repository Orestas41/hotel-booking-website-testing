
from selenium.webdriver.common.by import By


class PaymentPageLocators:

    NUMBER = (By.ID, 'cardNumber')

    BRAND = (By.ID, 'credit_card_collect_purchase_brand')

    VISA = (By.XPATH, '//option[. = "VISA"]')

    EXPIRE_MONTH = (By.ID, 'cardExpirationMonth')

    MONTH = (By.XPATH, '//option[. = "01"]')

    EXPIRE_YEAR = (By.ID, 'cardExpirationYear')

    YEAR = (By.XPATH, '//option[. = "2023"]')

    ADDRESS = (By.ID, 'credit_card_collect_purchase_address')

    ZIP = (By.ID, 'credit_card_collect_purchase_zip')

    CITY = (By.ID, 'credit_card_collect_purchase_city')

    STATE = (By.ID, 'credit_card_collect_purchase_state')

    COUNTRY = (By.ID, 'credit_card_collect_purchase_country')

    AFGHANISTAN = (By.XPATH, '//option[. = "Afghanistan"]')

    SUBMIT = (By.CSS_SELECTOR, '.btn-success')
