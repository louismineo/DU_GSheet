from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--fullscreen")


PATH = r"/usr/local/bin/chromedriver"


print("Running webdriver for chrome")
driver = webdriver.Chrome(PATH,options=chrome_options)

driver.get("https://www.dayuse.sg/s/singapore/singapore?selectedAddress=Singapore&sluggableAddress=Singapore")
print(driver.title)
print(driver.current_url)
