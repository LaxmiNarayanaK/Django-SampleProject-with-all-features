import os
from django.shortcuts import render
from . serializers  import ScrapSerializer
from rest_framework.response import Response
from .models import ScrapModel


# def cmlt(request):

#     tables = camelot.read_pdf("Data/MA Hemp Licenses 10.01.21.pdf",pages="1-end",flavor="stream")
#     li=[]
#     for i in tables:
#         l=i.df.values.tolist()
#         print(l)
#         l=l[6:]
#         for j in range(len(l)):
#             li.append(l[j])
        
#     print((len(li)))

#     df=pd.DataFrame(li,columns=["LicenseType","LicenseNumber","Licensee","MailingAddress"])
#     print(df)
#     df.to_csv("Data/camelot.csv")
#     df_records = df.to_dict('records')

#     for item in df_records:
#         LicenseType =  item['LicenseType']
#         LicenseNumber =  item['LicenseNumber']
#         Licensee =  item['Licensee']
#         MailingAddress =  item['MailingAddress']
        
#         cl = CamelotModel(LicenseType=LicenseType,LicenseNumber=LicenseNumber,Licensee=Licensee,MailingAddress=MailingAddress)
#         cl.save()
#     return render(request,'scrap.html')
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import sys
sys.path.append("E:\Zigram\Training\Django-Files")        
from globalfuns.ScrapbyId import scrapNdump

def download(request):

    options=webdriver.ChromeOptions()
    prefs = {'download.default_directory' : 'E:\Zigram\Django-Files','safebrowsing.enabled': "false"}
    # options.add_argument("--safebrowsing-disable-download-protection")
    # options.add_argument("--window-size=1920,1080")
    # options.headless = True
    # prefs = {
    # "download.default_directory":"E:\Zigram\Django-Projects\telusko\Data",
    # "download.prompt_for_download": False,
    # "download.directory_upgrade": True,
    # "plugins.always_open_pdf_externally": True}
    options.add_experimental_option('prefs',prefs)
    driver = webdriver.Chrome(service=Service(r"E:\Zigram\Django-Files\Data\chromedriver.exe"),options=options)
    driver.get("https://www.stats.govt.nz/large-datasets/csv-files-for-download/")
    time.sleep(3)
    # import pdb; pdb.set_trace()
    driver.find_element(By.XPATH,"//*[@id='main']/section/div/div/div/article/div/div[2]/article/ul/li[2]/div/div/h3/a").click()
    time.sleep(3)
    return render(request,'scrap.html')

from rest_framework import status
from rest_framework.response import Response
from .models import ScrapModel
from .serializers import ScrapSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
    
class scrap_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        snippets = ScrapModel.objects.all()
        serializer = ScrapSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ScrapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class scrap_detail(APIView):

    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, format=None):
    
        # snippet = ScrapModel.objects.get(id=data['id'])
        # serializer = ScrapSerializer(snippet)
        # filename=serializer.data['filename']+'.py'
        # exec(open(os.getcwd()+'\\Data\\'+filename).read())
        scrapNdump(data=request.data,model=ScrapModel,serializer=ScrapSerializer)
        return Response("Data Scrapped and Strored in Database", status=status.HTTP_201_CREATED)


# {"id":20}