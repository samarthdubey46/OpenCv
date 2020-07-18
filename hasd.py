import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/forms/d/e/1FAIpQLSdvmeBW5HI9jVYbaVVfgphOFNRWCKIrTcqMfptnpja44bj3MA/viewform"
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
print(soup.prettify1())
id = "quantumWizTextinputPaperinputEl freebirdFormviewerViewItemsTextShortText freebirdFormviewerViewItemsTextEmail"
f = soup.find(class_=id)
