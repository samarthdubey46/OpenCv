import requests
from bs4 import BeautifulSoup

url = 'https://onedrive.live.com/edit.aspx?action=editnew&resid=7C7F3785513334E7!1433&ithint=file%2cxlsx&wdNewAndOpenCt=1592834076974&wdPreviousSession=81d0a01f-0998-49ef-a710-7149d0664d41&wdOrigin=OFFICECOM-HWA.START.NEW'
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
soup = BeautifulSoup(r.content,'lxml')
# print(soup.prettify())
url1 = 'https://login.live.com/login.srf?wa=wsignin1.0&amp;rpsnv=13&amp;ct=1592834507&amp;rver=7.3.6962.0&amp;wp=MBI_SSL_SHARED&amp;wreply=https:%2F%2Fonedrive.live.com%2Fedit.aspx%3Faction%3Deditnew%26resid%3D7C7F3785513334E7!1433%26ithint%3Dfile%252Cxlsx%26wdNewAndOpenCt%3D1592834076974%26wdPreviousSession%3D81d0a01f-0998-49ef-a710-7149d0664d41%26wdOrigin%3DOFFICECOM-HWA.START.NEW&amp;lc=1033&amp;id=250206&amp;cbcxt=sky&amp;cbcxt=sky'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content,'lxml')
# print(soup1.prettify())
