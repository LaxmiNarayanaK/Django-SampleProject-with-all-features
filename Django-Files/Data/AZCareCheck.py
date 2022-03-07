from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
# from scrap.models import SeleniumModel


options=webdriver.ChromeOptions()

prefs = {'download.default_directory' : 'E:\Zigram\Training\Django-Files\Data\\','safebrowsing.enabled': "false"}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(service=Service(r"E:\Zigram\Training\Django-Files\Data\chromedriver.exe"),options=options)

driver.get("https://azcarecheck.azdhs.gov/s/?facilityId=001t000000bI4Y4AAK")
time.sleep(5)
link=[]
data=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
table=driver.find_elements(By.XPATH,".//div[@class='slds-scrollable_y']/div")
time.sleep(3)
for i in range(table.__len__()):
    a=table[i].find_elements(By.XPATH,".//div[@class='slds-media__body']/div")
    link.append(a[4].find_element(By.TAG_NAME,"a").get_attribute("href"))

for j in range(1,5,1):
    driver.get(link[j])
    time.sleep(3)
    #LegalName
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[1]").text)!=0):
        data[0].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[1]").text)
    else:
        data[0].append("NA")
    #print(data[0][j])

    #Address
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/a[1]/lightning-formatted-text").text)!=0):
        data[1].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/a[1]/lightning-formatted-text").text)
    else:
        data[1].append("NA")
    #print(data[1][j])

    #Mailing Address
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/a[2]/lightning-formatted-text").text)!=0):
        data[2].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/a[2]/lightning-formatted-text").text)
    else:
        data[2].append("NA")
    #print(data[2][j])

    #Offsite Cultivation Address
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[2]").text)!=0):
        data[3].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[2]").text)
    else:
        data[3].append("NA")        
    #print(data[3][j])

    #Manufacture Address
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[3]").text)!=0):
        data[4].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-text[3]").text)
    else:
        data[4].append("NA")
    #print(data[4][j])

    #Phone
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-phone/a").text)!=0):
        data[5].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-phone/a").text)
    else:
        data[5].append("NA")
    #print(data[5][j])

    #Email
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-email").text)!=0):
        Email=driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[1]/slot/lightning-formatted-email").text
        Email=Email.split()
        data[6].append(Email[1])
    else:
        data[6].append("NA")
    #print(data[6][j])

    #License
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/a/lightning-formatted-text").text)!=0):
        data[7].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/a/lightning-formatted-text").text)
    else:
        data[7].append("NA")
    #print(data[7][j])

    #License Effective
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[1]").text)!=0):
        data[8].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[1]").text)
    else:
        data[8].append("NA")
    #print(data[8][j])

    #License Expires
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[2]").text)!=0):
        data[9].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[2]").text)
    else:
        data[9].append("NA")
    #print(data[9][j])

    #Owner / License
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[3]").text)!=0):
        data[10].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[3]").text)
    else:
        data[10].append("NA")
    #print(data[10][j])

    #Services
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[4]").text)!=0):
        data[11].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/lightning-formatted-text[4]").text)
    else:
        data[11].append("NA")
    #print(data[11][j])

    #Hours of Operation
    if(len(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/table/tbody").text)!=0):
        data[12].append(driver.find_element(By.XPATH,"//*[@id='tab-1']/slot/c-azcc-facility-details-tab/div/lightning-layout/slot/lightning-layout-item[2]/slot/table/tbody").text)
    else:
        data[12].append("NA")

df = pd.DataFrame({'LegalName': data[0],'Address': data[1],'MailingAddress': data[2],"OffsiteCultivationAddress":data[3],'ManufactureAddress': data[4],'Phone': data[5],'Email': data[6],'License': data[7],'LicenseEffective': data[8],'LicenseExpires': data[9],'OwnerLicense': data[10],'Services': data[11]})
# print(data)
# print(df)
df.to_csv("E:\Zigram\Django-Files\Data\\AZCareCheck.csv")
# df_records = df.to_dict('records')

# for item in df_records:
#     LegalName =  item['LegalName']
#     Address =  item['Address']
#     MailingAddress =  item['MailingAddress']
#     OffsiteCultivationAddress =  item['OffsiteCultivationAddress']
#     ManufactureAddress =  item['ManufactureAddress']
#     Phone =  item['Phone']
#     Email =  item['Email']
#     License =  item['License']
#     LicenseEffective =  item['LicenseEffective']
#     OwnerLicense =  item['OwnerLicense']
#     Services =  item['Services']
    
#     sm = SeleniumModel(LegalName=LegalName,Address=Address,MailingAddress=MailingAddress,OffsiteCultivationAddress=OffsiteCultivationAddress,ManufactureAddress=ManufactureAddress,Phone=Phone,Email=Email,License=License,LicenseEffective=LicenseEffective,OwnerLicense=OwnerLicense,Services=Services)
#     sm.save()

from globalfuns.Dumpdata import dump

dump(df,table="scrap_seleniummodel")