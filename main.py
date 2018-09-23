import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
turo_sfo = "https://turo.com/search?airportCode=SFO&customDelivery=true&defaultZoomLevel=11&endDate=10%2F07%2F2018&endTime=22%3A00&international=true&isMapSearch=false&itemsPerPage=200&location=SFO%20%E2%80%94%20San%20Francisco%20International%20Airport%2C%20San%20Francisco%2C%20CA&locationType=Airport&maximumDistanceInMiles=30&sortType=RELEVANCE&startDate=10%2F06%2F2018&startTime=10%3A00"
page = requests.get(turo_sfo)

browser = webdriver.Chrome()
browser.get(turo_sfo)
time.sleep(5)
page = browser.page_source
# browser.close()
soup = BeautifulSoup(page, 'html.parser')
print (soup.prettify())
# for a_link in soup.findAll("a", {"class":"vehicleCard"}):    
#     print(a_link)



# print(soup.prettify())

# outfile = open('out.txt', 'w')
# print len(soup.find_all('span', attrs={'class':'sx-price-whole'}))
# print len(soup.find_all('h2'))
# print soup.find('div', attrs={"class":"searchResultsList"})
# for each in soup.find_all('h2'):
#     print each.string