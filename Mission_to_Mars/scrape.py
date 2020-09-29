#copy all dependencies
from time import sleep
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pymongo
import requests

#create function for each website we scrape
def scrape_info():
    



def title():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 2)