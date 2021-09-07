import requests
import time

api_key='RGAPI-7d0b0900-f58c-4de8-8e95-4d6eb2fc959a'


namelist=["로지택키보드","샘호네모동그라미"]

while(1):
    for name in namelist:
        a="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+'?api_key='+api_key
        r=requests.get(a)
        id=r.json()['id']
        b="https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+api_key
        r=requests.get(b)
        try:
            r.json()['gameId']
        except KeyError:
            print(name+': X    ', end='')
            time.sleep(3)
            continue
    
        gamemode=r.json()['gameMode']
        if(gamemode=='ARAM'):
            gm='칼바람'
        elif(gamemode=="CLASSIC"):
            gm='협곡'
        elif(gamemode=="URF"):
            gm='우르프'
        else:
            gm='??'
        print(name+': '+gm+'     ', end='')
        time.sleep(3)
        print()
