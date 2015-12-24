#!/usr/bin/python
import urllib2
import json
import csv
from lxml import html
import requests

with open('keys.csv','r') as content_file:
	content = content_file.read()



values = content.split(",")

f = open('values.csv','wb')

for index in range(len(values)):
	key = values[index]
	url = "http://www.bseindia.com/SiteCache/1D/stkCompanyHeader.aspx?Type=BRD&text="+key.strip(' \n\t')
	page = requests.get(url)
	cheaders = page.content.split(",")
	name = cheaders[4]
	

	url = "http://www.bseindia.com/stock-share-price/SiteCache/IrBackupStockReach.aspx?scripcode="+key.strip(' \n\t')
	
	page = requests.get(url)
	tree = html.fromstring(page.content)	
	value = tree.xpath("//td[@class ='tbmaingreen']/text()")
	print value
	f.write(name+","+value[0])
	f.write('\n')

