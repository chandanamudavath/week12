import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup_teardown():
    options = webdriver.ChromeOptions()
    options.binary_location = (
        r"C:\Users\Chandana\AppData\Local\Google\Chrome\Application\chrome.exe"
    )
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()

    yield driver

    driver.quit()


def test_registration_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")

    assert driver.title == "Registration Form"
    assert driver.find_element(By.TAG_NAME, "h2").text == \
        "Student Registration Form"
