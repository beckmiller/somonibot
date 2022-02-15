from imports import * 


class Orien:
    
    def __init__(self, url):
        self.url = url
        
    def get_orien_rub(self):
        r = requests.post(self.url, json={"CardNo":"992927081817"})
        data = r.json()
        orien_rub = float(data['currencyRate'])*1000 
        
        return orien_rub