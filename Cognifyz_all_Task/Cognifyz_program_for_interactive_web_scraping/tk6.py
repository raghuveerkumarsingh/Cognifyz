#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to fetch URL. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching URL:", e)
        return None

def scrape_info(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Scraping the title of the webpage
        title = soup.title.string
        print("Title:", title)

        # Example: Scraping all the links on the webpage
        links = soup.find_all('a', href=True)
        print("\nLinks:")
        for link in links:
            print(link['href'])

        # You can add more scraping logic here based on your requirements

def main():
    url = input("Enter URL to scrape: ")
    html_content = fetch_url(url)
    if html_content:
        scrape_info(html_content)

if __name__ == "__main__":
    main()


# In[ ]:




