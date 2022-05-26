from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import xml


def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content,'xml')
  
  result = soup.find_all('data')

  return result
