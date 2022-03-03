from typing import final
from urllib import request
from attr import attrs
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
headers=["V_Mag(mv)","proper_name","bayer_designation","Distance(ly)","Spectral_class","hyperlink","Mass(M)","Radius(R)","Luminosity(L)"]
starsdata=[]
brightest_star_data=[]

def scrape():
    for i in range(0,428):

        soup=BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("ul",attrs={"class","stars"}):
            th_tags=ul_tag.find_all("th")
            temp_list=[]
            for index,th_tag in enumerate(th_tags):
                if index==0:
                    temp_list.append(th_tag.find_all("a")[0].contents[0])
                else:
                    try:

                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_th_tag=th_tags[0]
            temp_list.append("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"+hyperlink_th_tag.find_all("a",href=True)[0]["href"])
            planetdata.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()