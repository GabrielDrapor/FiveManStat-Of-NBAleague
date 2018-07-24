# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

result = pd.DataFrame(columns=['name', 'price', 'score', 'rms_cnt', 'url'])

for page in range(1,387):
    formdata={  "__VIEWSTATEGENERATOR": "DB1FBB6D",
                "cityName": "%e8%a5%bf%e5%ae%89",
                "RoomGuestCount": "1,1,0",
                "operationtype": "NEWHOTELORDER",
                "cityId": "10",
                "cityPY": "xi‘an",
                "cityCode": "029",
                "checkIn": "2018-03-14",
                "checkOut": "2018-03-15",
                "page": page}

    pg = requests.post("http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx", data=formdata).content.decode('utf-8')
    soup = BeautifulSoup(pg)

    for hotel in  soup.find_all('ul', class_='\\"hotel_item\\"'):
        score = (hotel.findChild('span', class_='\\"hotel_value\\"')).text
        price = (hotel.findChild('span', class_='\\"J_price_lowList\\"')).text
        title = hotel.findChild('a').attrs['title'][2:-2]
        hotel_id = test.findChild('a').attrs['data-hotel'][2:-2]
        url = 'http://hotels.ctrip.com/hotel/' + hotel_id + '.html'
        htl_page = requests.get(url).content.decode('utf-8')
        rms_cnt = re.findall('\d*(?=间房)', htl_page)[0]

        result = result.append(pd.DataFrame([title, price, score, rms_cnt, url], columns=result.columns))
