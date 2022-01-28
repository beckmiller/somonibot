import requests
from bs4 import BeautifulSoup as BS
from datetime import date
from alif_json import alif_rub
from dc import dc_rub
from orien import orien_rub

today = date.today()

def somoni_rub():
	r = requests.get('https://eskhata.com', verify=False).text

	soup = BS(r, 'lxml')

	sell = soup.find_all('td', class_='curs_value')[12].text
	#buy = soup.find_all('td', class_='curs_value')[13].text
	#buy = float(buy.replace(',','.'))*1000
	be_rub = float(sell.replace(',','.'))*1000
	return ('Рубль:\nДата: {}.\nДенежные переводы:\nБанк Эсхата: {} сомони.\nАлиф: {} сомони.\nDCity: {} сомони.\nOrienPay: {} сомони'.format(today, be_rub, alif_rub,dc_rub, orien_rub))
