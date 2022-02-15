# **Telegram bot**  based on aiogram
This is my first expirience to create telegram bot based on aiogram.
This bot scrapes exchange rate of Russian rubles and Tajikistans somoni
from xe.com, National Bank of Tajikistan and money transfer rate from 
top Tajik banks then it shows to users.


## 1. Requirements: 

![python](https://img.shields.io/badge/python-3.10.0-red)
 
> You need install all packeges from requirements.txt


### 2. Problem that I solved

There is exist local telegram group which I follow 
and where everytime people were asked about money transfer rate of RUB/TJS. 
It's Tajikistan local currency somoni. Everytime somebody telling for everyone who asked the rate of the currency.
So that's why I dicided automate this procces with getting top local banks money tranfer rate.
Cause of those Banks didn't have API, I dicided scrap web pages of banks 
by using `requests, BeautifulSoup`. Then I created Telegram bot where people can just press the button to know ex rate of currency.

### 3. Structure
In `banks` module located all related scripts that scrape data from webpages of Banks

### 4. How to run?
After install all requirments and get API from BotFather of Telegram run it in terminal `python bot.py`

### 5. How bot and response looks like: 
<img src="assets/sm.png" width="372" height="353" />


