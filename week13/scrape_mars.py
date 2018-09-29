from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import requests



def mars_news(browser):   
    # use selenium control google chromedriver
    url ='https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'lxml')
    
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'rollover_description_inner').text
    
    return (news_title, news_p)

def featured_image(browser):
    # use splinter control google chromedriver
    # Find and click the full image button
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    browser.quit()
    soup = bs(html, "lxml")
    # print(soup.prettify())


    image_url = soup.findAll('a', class_="fancybox")
    addresslist = []
    for address in image_url:
        addresslist.append(address['data-fancybox-href'])
        
    # print(addresslist)
    matching = [s for s in addresslist if "largesize" in s]
    # print(matching[0])

    featured_image_url = "https://www.jpl.nasa.gov" + matching[0]
    # print(featured_image_url)  

    return featured_image_url


def hemispheres():
    # use requests and beautifulsoup
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    imgname = []
    pageurls = []
    for a in soup.find_all('a', class_= 'itemLink product-item'):
        if a.find('h3') != None:
            imgname.append(a.h3.text)
            pageurls.append('https://astrogeology.usgs.gov' + a['href'])
    #print(imgname)
    #print(pageurls)

    imgurls = []
    for url in pageurls:
        response = requests.get(url)
        soup = bs(response.text, 'lxml')
        # print(soup.prettify())
        for a in soup.find_all('a', {'target': '_blank'}, href =True):
            if a.text == 'Original':
                # print(a['href'])
                imgurls.append(a['href'])
    # print(imgurls)

    hemisphere_image_urls = []
    for i in range(len(imgurls)):
        hemisphere_image_urls.append({
            "title":imgname[i], "img_url":imgurls[i]
        })
    return hemisphere_image_urls
    

def twitter_weather():
    # use requests and beautifulsoup
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    # print(response.url)
    soup = bs(response.text, 'lxml')
    # print(soup.prettify())

    mars_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    return mars_weather


def mars_facts():
    # use pandas
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)[0]
    tables.columns = ['description', 'value']
    tables.set_index('description', inplace=True)
    # html_table = tables.to_html()
    return tables.to_html()
def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path = "/usr/local/bin/chromedriver", headless=True)

    # 1. mars_news
    news_title, news_p = mars_news(browser)    
    # print(news_title)
    # print(news_p)

    # 2. featured_image
    featured_image_url = featured_image(browser)
    # print(featured_image_url)

    # 3. hemispheres
    hemisphere_image_urls = hemispheres()
    # print(hemisphere_image_urls)

    # 4. mars_weather
    mars_weather = twitter_weather()
    # print(mars_weather)

    # 5. mars_facts
    mars_facts_table = mars_facts()
    # print(mars_facts_table)

    # Stop webdriver and return data
    browser.quit()
    # return data
    final_data = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': featured_image_url, 
        'hemisphere_image_urls': hemisphere_image_urls, 
        'mars_weather': mars_weather, 
        'mars_facts': mars_facts_table
    }
    return final_data


if __name__ == "__main__":
    # If running as script, print scraped data
    pdscrape_all()