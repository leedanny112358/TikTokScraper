# from requests_html import HTMLSession
# from bs4 import BeautifulSoup
#
# session = HTMLSession()
#
# r = session.get('https://www.tiktok.com/tag/bestfandom')
# r.html.render()
#
# soup = BeautifulSoup(r.html.text, 'lxml')
# print(soup.prettify())


# soup = BeautifulSoup(webpage, 'html.parser')
#
# print(soup.prettify())

from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=Naverbot")

class TikTokScraper:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=opts)
        self.driver.get('https://www.tiktok.com/tag/bestfandom')
        sleep(4)
        videos = self.driver.find_element_by_xpath('//a[@href="<a href="https://www.tiktok.com/@rachmartino/video/6813508636950678790" class="jsx-1792501825 video-feed-item-wrapper"><div class="jsx-1464109409 image-card" style="border-radius: 4px; background-image: url(&quot;https://p16-va-default.akamaized.net/obj/tos-maliva-p-0068/49a0e50f403c410db3f33ead817b9557_1586393606&quot;);"><div class="jsx-3355072868 video-card default"><div class="jsx-3355072868 video-card-mask"></div></div></div></a>"]').click()
        # individual class markers are jsx-1410658769 video-feed-item
TikTokScraper()

