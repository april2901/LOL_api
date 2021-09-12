import requests
import time
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


api_key='RGAPI-47839727-1f0b-48bc-b869-56964bde85d8'

my_name=["april2901"]
namelist=["로지택키보드","샘호네모동그라미", "롤체나해야지"] #need full name

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
            #color.write(name+": X    ","COMMENT")
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
        #print(name+': '+gm+'     ', end='')
        color.write(name+":"+gm+"    ","COMMENT")
        time.sleep(3)

    
        a="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+'?api_key='+api_key
        r=requests.get(a)
        id=r.json()['id']
        b="https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+api_key
        r=requests.get(b)
        try:
            a=r.json()['gameId']
        except KeyError:
            continue
        print(a)
    print()
