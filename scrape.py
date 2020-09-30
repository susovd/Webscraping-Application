from splinter import Browser
from bs4 import BeautifulSoup 
import pandas as pd
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


#CREATE FUNCTION FOR EACH WEBSITE THAT WE SCRAPE
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    data_scraped = {}

    #retrieve news article
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 2)
    #create a beautiful soup object, parse with html parser
    soup = bs(browser.html, "html.parser")
    section_element = soup.select_one("ul.item_list li.slide")
    news_title = section_element.find("div", class_ = "content_title").get_text()
    description = section_element.find("div", class_ = "article_teaser_body").get_text()

    #store news title and description in a dictionary
    news_data = {"news_title": news_title,
                 "description": description}

    
    












    #data{ "Title":title(browser)
    #    "Excerpt":paragraph(browser)
     #    "Featured_image":
    #   "mars_facts":
      #   "hemisphere image":
    #}
    #return data


#def title(browser):
 #   url = 'https://mars.nasa.gov/news/'
  #  browser.visit(url)
   # news_title = soup.find("div", class_= "bottom_gradient").get_text()
    #return news_title

#def paragraph(browser):
 #   url = 'https://mars.nasa.gov/news/'
  #  browser.visit(url)
  #  news_paragraph = soup.find("div", class_ = "article_teaser_body").get_text()
   # return news_paragraph