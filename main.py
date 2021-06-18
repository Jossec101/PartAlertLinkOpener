from telethon import TelegramClient, events, sync
import winsound, webbrowser
import urllib.parse as urlparse
from urllib.parse import parse_qs
import re
from bs4 import BeautifulSoup
import requests

############################### TO BE CHANGED -> check https://core.telegram.org/api/obtaining_api_id  ###################################################
api_id = CHANGEME
api_hash = CHANGEME
##########################################################################################################################################################

def open_url(url):
    webbrowser.get().open(url)
    print(f'Opened {url}')
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 5000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def main():

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()
    # Declare your channel id variables here
    channel3080Id = None
    channel3090Id = None
    
    for dialog in client.iter_dialogs():
    ########################################################## Search your channels like those examples for RTX 3080 and RTX 3090 ######################################


        if '3080' in dialog.name:
            print(f"PartAlert 3080 channel id: {dialog.id}")
            channel3080Id = dialog.id
        if '3090' in dialog.name:
            print(f"PartAlert 3090 channel id: {dialog.id}")
            channel3090Id = dialog.id        

    ##########################################################################################################################################################

    @client.on(events.NewMessage(chats=[channel3080Id,channel3090Id]))
    async def my_event_handler(event):
            url = event.message.message
            url = re.findall(r'(https?://\S+)', url)[0]
            # Change this in the case the change the url
            if("alert.partalert.net" in url):
                req = requests.get(url)
                soup = BeautifulSoup(req.text, "html.parser")
                
                for link in soup.find_all('a'):
                    href = link.get("href")

                    if("amazon") in href:
                        url = href.split('?')[0]

                        open_url(url)
            
            else:
                open_url(url)

    client.run_until_disconnected()

main()
