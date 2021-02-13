from selenium import webdriver
from bs4 import BeautifulSoup
import re
driver = webdriver.Firefox()
driver.get("https://old.reddit.com/r/wallstreetbets/top/")
soup = BeautifulSoup(driver.page_source,'html.parser')
print(re.findall(r'[A-Z][A-Z][A-Z][A-Z]*',soup.get_text()))