from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text= "$")w3-=ecx 99/*
parent = prices[0].parent
strong = parent.find("strong")
strong_string = strong.string
comma = strong_string.replace(',', '')
price = int(comma)
if price < 1500:
     print(True)
