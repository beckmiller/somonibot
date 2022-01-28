from requests_html import  HTMLSession

session =  HTMLSession()

#Setting urls xe.com and nbt.tj
url_xe = 'https://www.xe.com/currencyconverter/convert/?Amount=1000&From=RUB&To=TJS'
url_nbt = 'https://nbt.tj/ru/kurs/kurs.php'

#getting exchange rate rub/tjs from xe.com
def get_xe_data():
	"""This function returns exchange rate of RUB/TJS from xe.com

	Returns:
		[float]: [144.000]
	"""
	r = session.get(url_xe)
	r.html.render()
 
	x_r = r.html.find('.result__BigRate-sc-1bsijpp-1')[0].text.split()
	x_r = round(float(x_r[0]),3)

	return x_r

#extracting exchange rate of RUB/TJS from National bank of Tajikistan
def get_nbt_data():
	"""This function returns local exchange rate of RUB/TJS from nbt.tj

	Returns:
		[float]: [144.000]
	"""
	nbt = session.get(url_nbt)
	nbt.html.render()
 
	nbt_r = nbt.html.find('#myTable > tbody > tr:nth-child(28) > td:nth-child(5)')[0].text
	nbt_r = round(float(nbt_r)*1000, 3)

	return nbt_r

#Trying predict exchange rate of pair RUB/TJS 
#Cause of local exchange rate RUB/TJS follows global exhange rate pair of RUB/TJS
#We try predict it just with some simple calculations
def prediction():
	"""This function trying predict exchange rate of RUB/TJS with simple calculations
		It's just for testing, not for actually predicting

	Returns:
		[str]: [trying predict with simple calculations]
	"""
	x_r = get_xe_data()
	nbt_r = get_nbt_data()
    
    #The National Bank of Tajikistan raises his local exchange rate mostly like this
    #If in xe.com rate of RUB/TJS higher than local rate to 1-1.5 somoni, NBT raises its local rate to 50 diram with 70% and etc.
	if 1.0 <= x_r - nbt_r < 1.5:
		return 'Курс повыситься: на 50 дирам.\nС вероятностью: 70%'
	elif 1.5 <= x_r - nbt_r < 1.8:
		return 'Курс повыситься: на 50 дирам.\nС вероятностью 100%.\nКурс повыситься: на 1 сомони.\nС вероятностью: 60%.'
	elif  x_r - nbt_r > 1.8:
		return 'Курс повыситься: на 1 сомони и больше.\nС вероятностью:100%.'
	elif 0.5 <= x_r - nbt_r < 1.0:
		return 'Курс повыситься: на 50 дирам.\nС вероятностью: 45%'
	else:
		return 'Пока не ожидаем изменение курса:('


predict = prediction()
