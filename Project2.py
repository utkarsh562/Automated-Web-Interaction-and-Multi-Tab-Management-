from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

Service = Service(r"C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=Service)

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selemium")

driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(5)

result_links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")
    
    
print(f"Number of links found: {len(result_links)}")

for link in result_links:
    # Get the href attribute of the link
    href = link.get_attribute('href')
    
    # Open the link in a new browser tab
    driver.execute_script("window.open(arguments[0]);", href)
   
time.sleep(5)

win = driver.window_handles

for windid in win:
    driver.switch_to.window(windid)
    print(driver.title)





