from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from object_classes import LoginPage
from dotenv import load_dotenv
import os


binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary)
browser.implicitly_wait(5)

load_dotenv()
username = os.getenv('INSTA_USER')
password = os.getenv('INSTA_PASS')
print(username, password)

login_page = LoginPage(browser)
login_page.login(username, password)


sleep(20)

browser.close()
