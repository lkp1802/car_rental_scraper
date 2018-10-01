import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, sys
turo_sfo = "https://turo.com/search?airportCode=SFO&endDate=10%2F07%2F2018&endTime=22%3A00&itemsPerPage=200&locationType=Airport&sortType=RELEVANCE&startDate=10%2F06%2F2018&startTime=10%3A00"
page = requests.get(turo_sfo)

browser = webdriver.Chrome()
default_size = browser.get_window_size()
browser.set_window_size(2000, default_size['height'])

browser.get(turo_sfo)
time.sleep(10)

def handleSingleCardFormat():
    print ("handleSingleCard called")
    try:
        # Test whether it's single card format
        browser.find_element_by_css_selector('a.vehicleWithDetails.searchResult')
        # Fetch all a tags
        links = browser.find_elements_by_css_selector('a.vehicleWithDetails.searchResult')
        if (len(links) == 0):
            print ("list is empty")
            return
        for each in links:
            print (each.get_attribute('href'))
        # scroll to last card on page
        browser.execute_script("arguments[0].scrollIntoView();", links[-1])
        time.sleep(1)
        # get next batch
        links = browser.find_elements_by_css_selector('a.vehicleWithDetails.searchResult')
        print (len(links))
        for each in links:
            print (each.get_attribute('href'))
    except:
        raise LookupError('a.vehicleWithDetails.searchResult')

def handleMultipleCardsFormat():
    print ("handleMultipleCards called")
    try:
        browser.find_element_by_css_selector('a.vehicleCard')
        # Fetch all a tags
        links = browser.find_elements_by_css_selector('a.vehicleCard')
        if (len(links) == 0):
            print ("list is empty")
            return
        for each in links:
            print (each.get_attribute('href'))
        # scroll to last card on page
        browser.execute_script("arguments[0].scrollIntoView();", links[-1])
        time.sleep(1)
        # get next batch
        new_links = browser.find_elements_by_css_selector('a.vehicleCard')
        print (len(new_links))
        for each in new_links:
            print (each.get_attribute('href'))
    except:
        raise LookupError('a.vehicleCard')

# Determine which format being return by turo
try:
    handleSingleCardFormat()
except:
    print ("Trying option 2..")
    try:        
        handleMultipleCardsFormat()
    except:
        print ("Both options fail. Terminating..")
        browser.quit()
        sys.exit(0)
# browser.quit()


# if (len(links) == 0):
#     print("Executing option 2...")
#     links = browser.find_elements_by_css_selector("a.vehicleCard")
# if (len(links) == 0):
#     print ("Both options fail. Terminating...")
#     sys.exit(0)
# print (len(links))
# for each in links:
#     print(each.get_attribute("href"))

# scroll to last card on page
# browser.execute_script("arguments[0].scrollIntoView();", links[-1])


# page = browser.page_source
# soup = BeautifulSoup(page, 'html.parser')
# list_1 = soup.findAll("a", {"class":"vehicleCard"})
# if (len(list_1) == 0):
#     list_1 = soup.findAll("a", {"class":"vehicleWithDetails searchResult"})
# if (len(list_1) == 0):
#     print("Cannot fetch list of results")
#     sys.exit(0)
# for element in list_1:
#     print("https://turo.com"+element['href'])