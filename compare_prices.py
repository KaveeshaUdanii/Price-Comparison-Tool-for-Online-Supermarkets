import requests
import json
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):

  # Fetch HTML content for both websites
  response_laughs = requests.get(product_laughs, headers = user_agent)
  response_glomark = requests.get(product_glomark, headers = user_agent )

  # Parse Laughs Super's price
  soup_laughs = BeautifulSoup(response_laughs.text, 'html.parser')
  price_laughs = soup_laughs.find('span', {'class':'regular-price'}).text.strip()  
  product_name_laughs = soup_laughs.find('h1').text.strip()

  # Parse Glomark's price
  soup_glomark = BeautifulSoup(response_glomark.text, 'html.parser')
  script_glomark = soup_glomark.find('script', {'type':'application/ld+json'}).text
  data_glomark = json.loads(script_glomark)  
  price_glomark = data_glomark['offers'][0]['price']  
  product_name_glomark= data_glomark['name']

  # Print formatted prices
  price_laughs= float(price_laughs.replace("Rs.",""))
  price_glomark = float(price_glomark)
  print('Laughs  ', product_name_laughs,'Rs.: ', price_laughs)
  print('Glomark ' , product_name_glomark,'Rs.: ', price_glomark)

  # Compare prices
  if price_laughs < price_glomark :
    print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
  elif price_laughs > price_glomark :
    print('Glomark is cheaper Rs.:', price_laughs - price_glomark )
  else:
    print('Price ais the same')














