import requests
from bs4 import BeautifulSoup


"""FULL PAGE LAYOUT HTML"""

print("*******************FULL HTML LAYOUT*******************")
for i in range(1,10):
    url = "https://www.aajtak.in/"
    page = requests.get(url)
    if(page.status_code==200):
        print('Data Fetched Successfully', i)
        page = BeautifulSoup(page.content,'html.parser')
        print(page)



        """BREAKING NEWS"""
        print("*****************BREAKING NEWS*********************")
        breaking_news = page.findAll(attrs = {'class': 'brack-text-rigt'})

        breaking_news = breaking_news[0].text.replace('[<div class="brack-text-rigt"><a href="https://www.aajtak.in/breakingnews/story/20th-january-2024-breaking-news-latest-news-in-hindi-ntc-1863067-2024-01-20" title=',"")


        headline = page.findAll(attrs = {'class': 'story-listing'})
        headline = headline[0].text.replace('',"")
        print(breaking_news)

        print("**********HEADLINES**********")
        print(headline )
else:
    print("URL Not Found", i)



