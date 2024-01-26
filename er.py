from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

# Find "Store" link
driver.find_element(By.XPATH, "//a[contains(text(),'Store')]")

# Find "About" link
driver.find_element(By.XPATH, "//a[contains(text(),'About')]")

driver.find_element(By.XPATH, '//img[@alt="Google"]')
driver.find_element(By.XPATH, "(//input[@name='btnK'])[2]")

GoogleIcon = driver.find_element(By.XPATH, '//img[@alt="Google"]')
# driver.find_element(By.ID, "hplogo")
# GoogleIcon = driver.find_element(By.XPATH, "//img[@id='hplogo']")
# GoogleIcon = driver.find_element(By.ID, "hplogo")

if GoogleIcon:
    print("Google Logo is OK")
else:
    print("NO Google Logo")

driver.quit()