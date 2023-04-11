import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
url = "https://destinytracker.com/destiny-2/db/insights"


driver = "C:\\Users\\Robert Ward\\Desktop\\chromedriver_win32"
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)


# Navigate to the webpage
driver.get(url)
dropdowns = driver.find_elements(By.CLASS_NAME,"dropdown__selected")
dropdowns[1].click()
choices = [choice for choice in driver.find_elements(By.CLASS_NAME,"dropdown__item") if choice.text != '']
for choice in choices:
    text = choice.text
    choice.click()
    with open(text+'.html','w') as file:
        file.write(driver.page_source)
    dropdowns[1].click()