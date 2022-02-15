from imports import *

session =  HTMLSession() 

class DCity:
    
	def __init__(self, url):
		self.url = url
        
	def get_dc_rub(self):
		r1 = session.get(self.url)
		r1.html.render()
		rubl1 = r1.html.find('#adv > form > div:nth-child(4) > div.col-md-8.mt-2.mt-sm-4.d-sm-flex.rate.justify-content-between > div:nth-child(1) > div')	
		r1 = rubl1[0].text.split()
		rubl1 = float(r1[2])*1000
  
		return rubl1





