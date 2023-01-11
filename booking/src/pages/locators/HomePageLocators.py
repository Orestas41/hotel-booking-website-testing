
from selenium.webdriver.common.by import By


class HomePageLocators:

    DATE_FIELD = (By.ID, 'date-start')
    DAY = (By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr[6]/td[7]')

    NIGHTS = (By.ID, 'to-place')

    BOOK_BTN = (By.XPATH, '//*[@id="flights"]/form/div/div[5]/input')
