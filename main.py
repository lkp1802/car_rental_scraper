import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, sys
turo_sfo = "https://turo.com/search?airportCode=SFO&endDate=10%2F07%2F2018&endTime=22%3A00&itemsPerPage=200&locationType=Airport&sortType=RELEVANCE&startDate=10%2F06%2F2018&startTime=10%3A00"
page = requests.get(turo_sfo)

browser = webdriver.Chrome()
browser.get(turo_sfo)
time.sleep(5)
page = browser.page_source
# browser.close()

soup = BeautifulSoup(page, 'html.parser')
# print (soup.prettify())
list_1 = soup.findAll("a", {"class":"vehicleCard"})
if (len(list_1) == 0):
    list_1 = soup.findAll("a", {"class":"vehicleWithDetails searchResult"})
if (len(list_1) == 0):
    print("Cannot fetch list of results")
    sys.exit(0)
for element in list_1:
    print("https://turo.com"+element['href'])
    # print(element)
# for a_link in soup.findAll("a", {"class":"vehicleCard"}):    
#     print(a_link)



# print(soup.prettify())

# outfile = open('out.txt', 'w')
# print len(soup.find_all('span', attrs={'class':'sx-price-whole'}))
# print len(soup.find_all('h2'))
# print soup.find('div', attrs={"class":"searchResultsList"})
# for each in soup.find_all('h2'):
#     print each.string