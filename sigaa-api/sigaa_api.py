from selenium.webdriver.common.by import By
from selenium import webdriver
import os

with open(".env", "r") as f:
    for line in f.readlines():
        data = line.strip().split("=")
        os.environ[data[0]] = data[1]


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://sig.iffarroupilha.edu.br/sigaa/verTelaLogin.do")

driver.find_element(By.NAME, "user.login").send_keys(os.environ.get("LOGIN"))
driver.find_element(By.NAME, "user.senha").send_keys(os.environ.get("PASSWORD"))
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

trs = [
    i.get_attribute("innerText")
    for i in driver.find_elements(By.CSS_SELECTOR, "#turmas-portal .descricao a")
]

print(trs)

# with open("img.png", "wb") as f:
#     f.write(driver.get_screenshot_as_png())

driver.quit()
