import requests 

url = 'https://www.orienpay.tj/api/CardInfo'

r = requests.post(url, json={"CardNo":"992927081817"})
data = r.json()
orien_rub = float(data['currencyRate'])*1000 
