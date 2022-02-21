from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,json
import time
import xlsxwriter

class Twitter:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
       

    def yonlendirme(self):
        self.browser.get("https://twitter.com/search?q=%23AzKald%C4%B1&src=trend_click&f=live&vertical=trends")
        time.sleep(10)
        list1 = []
       

        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")

        while True:
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(3)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            tweets = self.browser.find_elements(By.CLASS_NAME,"css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
            
            for tweet in tweets:
                tweet_txt = tweet.text
                list1.append(tweet_txt)
                print(list1)

        asd = xlsxwriter.Workbook("tweet.xlsx")
        workSheet =asd.add_worksheet()

        for satir,veri in enumerate(list1):
            workSheet.write(satir,0,veri)

        asd.close()


twitter = Twitter()
twitter.yonlendirme()

