# author: Jiaying He
# email: helen827@126.com
# about: This program uses Wechat API to access the amount of new users and their sources.Then extract the data to cvs file which could be saved as excel file.

import requests
from collections import defaultdict
import json
import datetime

def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

csvfile = open('extractData.csv', 'a')

data = nested_dict(2, int)

start_date = datetime.date(2016, 12, 13)
    
for wholeyear in range(0,5):


    end_date = start_date + datetime.timedelta(days=6)

    payload = {"begin_date": start_date.strftime("%Y-%m-%d"), "end_date": end_date.strftime("%Y-%m-%d")}
    print(payload)

    url = 'https://api.weixin.qq.com/datacube/getusersummary?access_token=Zg2yRPetGLVGBjZwDNe4kOr2Dw2JoU6lhSdWZH74aOtzGQ9D4Nt-RRlGu9obEmGpLvE331_DfkqA5MTkEBc6x_84JkE4yx9sGQprCJ8fgRsABMgAIARSD'
    r = requests.post(url, json=payload)
    f = r.json()
    #print(r.json())
    #with open("test.json") as file:
    #    f = json.load(file)

    for line in f['list']:
        data[line['ref_date']][line['user_source']] = line['new_user']


    for numdays in range(0, 7):
        date = start_date + datetime.timedelta(days=numdays)
        date_text = date.strftime("%Y-%m-%d")
        row = date_text + "," + str(data[date_text][0]) + "," + str(data[date_text][1]) + "," + str(data[date_text][17])+"," +  str(data[date_text][30]) + "," + str(data[date_text][43]) + "," + str(data[date_text][51]) + "," + str(data[date_text][57]) + "," + str(data[date_text][75]) + "," + str(data[date_text][78])
        print(row)
        csvfile.write(row + '\r\n')

    start_date = start_date + datetime.timedelta(days = 7)
  
  
  
