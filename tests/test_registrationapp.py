
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def setup_teardown():
    options = Options()
    options.binary_location = (
        r"C:\Users\Chandana\AppData\Local\Google\Chrome\Application\chrome.exe"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
def test_registration_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    assert driver.title == "Registration Form"
