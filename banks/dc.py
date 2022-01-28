from requests_html import  HTMLSession
import time
session =  HTMLSession()
global dc_rub
def get_dc():
	r1 = session.get('https://online.dc.tj/index.php')
	r1.html.render()
	rubl1 = r1.html.find('#adv > form > div:nth-child(4) > div.col-md-8.mt-2.mt-sm-4.d-sm-flex.rate.justify-content-between > div:nth-child(1) > div')	
	r1 = rubl1[0].text.split()
	rubl1 = float(r1[2])*1000
	return rubl1

dc_rub = get_dc()



