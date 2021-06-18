This small python script allows you to open links from [PartAlert.net](https://partalert.net/) in the case you need a new GPU  (or any hardware alert from PartAlert) like I did. This allowed me to buy a RTX 3090 in Europe, so I want to shared it with the people since the others alternatives out there (much more complex than mine) did not help me at all. This script subscribes to PartAlert telegram channels using the Telegram API and automatically open the links and beeps hard.

Happy hunting!
## Table of contents
- [Requirements](#Requirements)
- [Telegram channels](#telegram-Channels)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)



## Requirements

- Python (Tested with 3.8.9 64bit on Windows)
- Telegram account subscribed to Telegram channels
- Telegram api credentials (check [this](https://core.telegram.org/api/obtaining_api_id))

## Telegram Channels

- [INVITE LINK: PartAlert for Radeon 6000 series GPUs](https://pa.function.workers.dev/tg/rtx3060ti)

- [INVITE LINK: PartAlert for RTX 3060 Ti
Note: this channel includes alerts for RTX 3060 Ti FE](https://pa.function.workers.dev/tg/rtx3070)

- [INVITE LINK: PartAlert for RTX 3070
Note: this channel includes alerts for RTX 3070 FE](https://pa.function.workers.dev/tg/rtx3070)

- [INVITE LINK: PartAlert for RTX 3080
Note: this channel includes alerts for RTX 3080 FE](https://pa.function.workers.dev/tg/rtx3080)

- [INVITE LINK: PartAlert for RTX 3090
Note: this channel includes alerts for RTX 3090 FE](https://pa.function.workers.dev/tg/rtx3090)

- [INVITE LINK: PartAlert for Founders Edition RTX 3070, 3080 & 3090](https://pa.function.workers.dev/tg/rtxfe)

- [INVITE LINK: PartAlert for Zen3 CPUs](https://pa.function.workers.dev/tg/zen3)

- [INVITE LINK: ConsoleAlert for PS5 & Xbox Series X/S consoles](https://pa.function.workers.dev/tg/console)

- [INVITE LINK: Group chat ](https://pa.function.workers.dev/tg/console)
## Quick start

1. Get your App api_id and app api_hash from Telegram and modify them on the code (Step #3)
2. Subscribe to the desired [telegram channels](#telegram-channels) (this example is ready for RTX 3080 and RTX 3090 channels).

3. Modify main.py API variables

```py
############################### TO BE CHANGED -> check https://core.telegram.org/api/obtaining_api_id  ###################################################

api_id = 123456
api_hash = "CHANGEME"

##########################################################################################################################################################

```

4. If you need to change the channels you want to subscribe, you need to search for them to get their ID, please check out that you write the channels well (e.g. you could have two channel with have 3080 keyword in it, in this case inser the full channel title)


```py
 ########################################################## Search your channels like those examples for RTX 3080 and RTX 3090 ######################################


        if '3080' in dialog.name: # <-- This keyword has to be unique in your telegram chats
            print(f"PartAlert 3080 channel id: {dialog.id}")
            channel3080Id = dialog.id
        if '3090' in dialog.name: #<-- This keyword has to be unique in your telegram chats
            print(f"PartAlert 3090 channel id: {dialog.id}")
            channel3090Id = dialog.id        

    ##########################################################################################################################################################

```

5. If you changed the channels to look for, assign them to a variable and subscribe in this line

```py
    @client.on(events.NewMessage(chats=[channel3080Id,channel3090Id])) 
```
6. Get the required libraries with pip

``` 
pip install -r ./requirements.txt
```

7. Run and be fast! Stock won't last! **The first time you run this application telegram with require your credentials to store a session locally in a file**
```
python ./main.py
```
## Thanks

- PartAlert.Net for its wonderful alerts

## Copyright and license
Code released under the MIT License

