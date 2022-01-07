import telegram
import requests
import json
import schedule
from time import sleep


def telegram_bot_sendtext(bot_message):
    
    bot_token = ""
    bot_chatID = ""

    f = open("config.txt")
    bot_token,bot_chatID=f.read().split()
    f.close()

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    response.json()


def check_cloudsea():
    r = requests.get("https://www.hko.gov.hk/out_photo/ascent/ascent_table.xml")
    data = json.loads(r.text)
    cloud_lv=[]
    available = False
    if len(cloud_lv)>0 and max(cloud_lv)<900:
        available = True
        for i in data["Graph_rh"]:
            if i["Value"]>=95:
                cloud_lv+=i["Height"]
        for i in data["Graph_wind"]:
            if i["Height"] in cloud_lv:
                if i["Spd"]>19:
                    available = False
                if 30>i["dir"] or i["dir"]>160:
                    available = False
    if available == True:
        telegram_bot_sendtext("Gogogogogogogogogogogogogogogogogogogogogogogogoogogogogogogogogogogogo")
        
    
schedule.every().day.at("03:00").do(check_cloudsea)

while True:
    
    schedule.run_pending()
    sleep(1)