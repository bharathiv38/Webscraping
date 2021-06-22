#!/usr/bin/env python
# coding: utf-8

# In[10]:


from bs4 import BeautifulSoup
import pandas as pd


# In[11]:


def amazon_mob(url):
    driver=webdriver.Chrome(r"C:\Users\SYS1\Downloads\chromedriver_win32\chromedriver.exe")
    start_page=0
    end_page=4
    urls = []
    name=[]
    price=[]
    image=[]
    rating=[]
    #loop to fetch urls of each mobile till page 5
    for page in range(start_page,end_page+1):
        driver.get(url)
        soup= BeautifulSoup(driver.page_source, 'html.parser')
        prod_urls = soup.find_all('a', attrs ={'class':'a-link-normal a-text-normal'})
        for prod in prod_urls:
            urls.append('https://www.amazon.in'+prod.get('href'))
    
    #loop to scrap required details from each mobile page
    for url in urls:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        n = soup.find('h1',attrs={'id':'title'})
        if n is not None:
            name.append(n.find('span').text.replace('\n',''))
        else:
            name.append('-')
        rat = soup.find('div', attrs = {'id':'averageCustomerReviews'})
        if rat is not None:
            rating.append(rat.find('i').find('span').text)
        else:
            rating.append('-')
        p = soup.find('span', attrs = {'class':'a-size-medium a-color-price priceBlockDealPriceString'})
        if p is not None:
            price.append(p.text[2:])
        else:
            p = soup.find('div', attrs = {'id':'price'})
            if p is not None:
                price.append(p.find('span').text[2:])
            else:
                price.append('-')
        img = soup.find('div', attrs = {'class':'imgTagWrapper'})
        if img is not None:
            image.append(img.find('img').get('src'))
        else:
            image.append('-')
    mob_df = df=pd.DataFrame({'Name':name,
                              'Price':price,
                              'Rating':rating,
                              'Image_link':image})
    print(mob_df)
    mob_df.to_csv('Amazon Mobiles.csv', index = False)
    
    
# Calling Function
amazon_mob('https://www.amazon.in/s?k=mobile+phones+under+20000&rh=n%3A1389432031&dc&qid=1604132579&rnid=3576079031&ref=sr_nr_n_1')


# In[ ]:




