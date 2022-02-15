from imports import *

today = date.today()
#setting urls
URL_ALIF = f'https://alif.tj/api/currency/index.php?currency=rub&date={today}'
URL_DCITY = 'https://online.dc.tj/index.php' 
URL_ESKHATA = 'https://eskhata.com'
URL_ORIEN = 'https://www.orienpay.tj/api/CardInfo'

class Eskhata:
    
	def __init__(self, url):
		self.url = url
        
	def get_eskhata_rub(self):
		r = requests.get(self.url, verify=False).text
		soup = BS(r, 'lxml')
		sell = soup.find_all('td', class_='curs_value')[12].text
		be_rub = float(sell.replace(',','.'))*1000

		return be_rub
		

def main():
     
    alif_rub = Alif(URL_ALIF)
    dc_rub = DCity(URL_DCITY)
    eskhta_rub = Eskhata(URL_ESKHATA)
    orien_rub = Orien(URL_ORIEN)
    
    return (f'Рубль:\nДата: {today}.\nДенежные переводы:\nБанк Эсхата: {eskhta_rub.get_eskhata_rub()} сомони.\
        	\nАлиф: {alif_rub.get_alif_rub()} сомони.\nDCity: {dc_rub.get_dc_rub()} сомони.\nOrienPay: {orien_rub.get_orien_rub()} сомони')

if __name__ == '__main__':
	main()