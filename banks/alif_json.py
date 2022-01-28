import requests 
from datetime import date

today = date.today()

url = 'https://alif.tj/api/currency/index.php?currency=rub&date={}'.format(today)

r = requests.get(url)
data = r.json()
alif_rub = float(data['money_transfer_buy_value'])*1000
