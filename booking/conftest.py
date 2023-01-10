import os

import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):

    driver = webdriver.Chrome(executable_path='C:\\Users\\orestas.dulinskas\\Anaconda3\\chromedriver.exe')

    request.cls.driver = driver
    yield