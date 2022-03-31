from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import csv
import pandas as pd

options=webdriver.ChromeOptions()
# options.add_argument("--safebrowsing-disable-download-protection")
# options.add_argument("--window-size=1920,1080")

# options.headless = True
prefs = {'download.default_directory' : 'E:\Zigram\Django-Projects','safebrowsing.enabled': "false"}
# prefs = {
#     "download.default_directory":"E:\Zigram\Django-Projects\telusko\Data",
#     "download.prompt_for_download": False,
#     "download.directory_upgrade": True,
#     "plugins.always_open_pdf_externally": True}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(service=Service(r"E:\Zigram\Django-Projects\telusko\Data\chromedriver.exe"),options=options)

driver.get("https://www.stats.govt.nz/large-datasets/csv-files-for-download/")
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='main']/section/div/div/div/article/div/div[2]/article/ul/li[2]/div/div/h3/a").click()
time.sleep(3)

    


    

