import requests
from bs4 import BeautifulSoup as BS
from datetime import date

today = date.today()

def currency():
	r = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1000&From=RUB&To=TJS').text

	soup = BS(r, 'lxml')

	c = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod').text.split()
	c = (float(c[0]))

	return ('Число: {}.\nНархи: {} сомони'.format(today, c))

