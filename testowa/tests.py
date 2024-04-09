import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importuj By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url='http://127.0.0.1:8000/admin')


def element_is_clickable():
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("admin")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="user-tools"]/a[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/nav/div[2]/a').click()

#element_is_clickable()

def respons_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)


respons_check(900, "test_900.png")
respons_check(1200, "test_1200.png")
respons_check(1800, "test_1800.png")
respons_check(600, "test_600.png")