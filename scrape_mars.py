from splinter import Browser
from bs4 import BeautifulSoup as bs 
import pandas as pd
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


#CREATE FUNCTION FOR EACH WEBSITE THAT WE SCRAPE
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    #create an emptry dictionary to append information as we scrape the web
    web_scrape_data = {}

    #retrieve news article
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 2)
    #create a beautiful soup object, parse with html parser
    soup = bs(browser.html, "html.parser")
    section_element = soup.select_one("ul.item_list li.slide")
    news_title = section_element.find("div", class_ = "content_title").get_text()
    news_p = section_element.find("div", class_ = "article_teaser_body").get_text()

    #store news title and description in a dictionary
    web_scrape_data = {"news_title": news_title,
                 "news_p": news_p}

    #JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    sleep(2)
    button_element = browser.find_by_id("full_image")
    button_element.click()
    browser.is_element_present_by_text("more info", wait_time = 2)

    button_more_info = browser.links.find_by_partial_text("more info")
    button_more_info.click()


    #create a beautiful soup object, parse with html parser
    soup = bs(browser.html, "html.parser")
    relative_image_url = soup.select_one("figure.lede a img").get("src")
    featured_image = f"https://www.jpl.nasa.gov{relative_image_url}"
    web_scrape_data["featured_image_url"] = featured_image
    

    #Mars facts
    url = "https://space-facts.com/mars/"
    df = pd.read_html(url, header = 0)
    #select the correct table to convert to html
    df= df[0]
    #Use Pandas to convert the data to a HTML table string
    html = df.to_html()
    web_scrape_data["Mars_facts"] = html 

    #mars hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    sleep(2)
    html = browser.html
    soup = bs(html, "html.parser")
    #find number of links to scrape, each hemisphere is under div with class item
    results = soup.find_all("div", class_ = "item")
    #find number of links to loop through 
    num_to_scrape = len(results)
    print(num_to_scrape)
    #create a list to append hemisphere image url information after scraping
    hemi_url = []
    #loop through range of num_to_scrape 
    for i in range(len(results)):
        #extract image link
        image_link = results[i].a["href"]
        #click on the image link
        browser.find_by_css("img.thumb")[i].click()
        #get title, from h2 section
        title= browser.find_by_css("h2.title").text
        #src from img tag and class wide-image
        src = browser.find_by_css("img.wide-image")["src"]
        #append the scraped information to hemi_url
        hemi_url.append({"title":title, "url":src})
    
    web_scrape_data["Mars_hemispheres"] = hemi_url

    #quit the browser
    browser.quit()

    return web_scrape_data

# if running from command line, show the scraped data results
if __name__ == "__main__":
    result = scrape()
    print(result)