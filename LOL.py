import requests
import time

api_key='RGAPI-7dbe35da-b14f-415b-8d05-9c6867ac5cf3'


name="april2901"
a="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+name+'?api_key='+api_key
r=requests.get(a)
id=r.json()['id']
while(1):
    b="https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+api_key
    r=requests.get(b)
    sta=r.json()['status']
    print(sta)
    time.sleep(3)
