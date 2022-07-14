#packages
from autoscraper import AutoScraper
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

#Web Scraping from E-commerce website Amazon
reviewlist =[]

def get_soup(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    return soup

def get_reviews(soup):
    reviews=soup.find_all('div',{'data-hook':'review'})
    for item in reviews:
        review={'body':item.find('span',{'data-hook':'review-body'}).text.strip()}
        reviewlist.append(review)
        
for x in range(1,499):
    soup=get_soup(f'https://www.amazon.in/Fire-TV-Stick-Alexa-Voice-Remote-3rd-Gen/product-reviews/B08R6QR863/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(x))
    #we are using product link to scrape the data 
    print(f'Getting page:{x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-pagination a-last'}):
        pass
    else:
        break
        
df=pd.DataFrame(reviewlist)
df.to_csv('Firestick.csv',index=False)


