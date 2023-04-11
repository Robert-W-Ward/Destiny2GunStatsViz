from selenium import webdriver
import requests
from bs4 import BeautifulSoup
url = "https://destinytracker.com/destiny-2/db/insights"


driver = "C:\\Users\\Robert Ward\\Desktop\\chromedriver_win32"
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome()


# Navigate to the webpage
driver.get(url)


with open("Kills-Comp.html",'w') as file:
    file.write(driver.page_source)