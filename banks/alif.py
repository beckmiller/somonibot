from socket import TCP_NODELAY
from imports import *


class Alif:
    def __init__(self, url):
        self.url = url
    
    def get_alif_rub(self):
        r = requests.get(self.url)
        data = r.json()
        alif_rub = float(data['money_transfer_buy_value'])*1000
        
        return alif_rub
