import requests
import time
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")


api_key='RGAPI-759f1a19-8ab7-4808-b83a-d10e998b5a23'  #본인의 라이엇 api key입력 (https://developer.riotgames.com/ 에서 발급)

my_name="april2901"  #본인 롤 닉네임 입력
namelist=["로지택키보드","세모네모동그라미","롤체나해야지", "AnWall"] #친구들 롤 닉네임 입력


def print_namelist_status():
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
    print()


def runeId_to_print_rune(a):
    if(a==8112):
        return '감전'
    elif(a==8124):
        return '포식자'
    elif(a==8128):
        return '어둠의 수확'
    elif(a==9923):
        return '칼날비'
    elif(a==8126):
        return '비열한 한방'
    elif(a==8139):
        return '피의 맛'
    elif(a==8143):
        return '돌발일격'
    elif(a==8136):
        return '좀비와드'
    elif(a==8120):
        return '유령포로'
    elif(a==8138):
        return '사냥의 증표'
    elif(a==8135):
        return '굶주린 사냥꾼'
    elif(a==8134):
        return '영리한 사냥꾼'
    elif(a==8105):
        return '끈질긴 사냥꾼'
    elif(a==8106):
        return '궁극의 사냥꾼'
    elif(a==8351):
        return '빙결강화'
    elif(a==8360):
        return '봉인풀린 주문서'
    elif(a==8358):
        return '프로토타입: 만능의 돌'
    elif(a==8306):
        return '마법공학 점멸기'
    elif(a==8304):
        return '마법의 신발'
    elif(a==8313):
        return '완벽한 타이밍'
    elif(a==8321):
        return '외상'
    elif(a==8316):
        return '미니언 해체분석기'
    elif(a==8345):
        return '비스킷 배달'
    elif(a==8347):
        return '우주적 통찰력'
    elif(a==8410):
        return '쾌속 접근'
    elif(a==8352):
        return '시간 왜곡 물약'
    elif(a==8005):
        return '집중공격'
    elif(a==8008):
        return '치명적속도'
    elif(a==8021):
        return '기민한 발놀림'
    elif(a==8010):
        return '정복자'
    elif(a==9101):
        return '과다치유'
    elif(a==9111):
        return '승전보'
    elif(a==8009):
        return '침착'
    elif(a==9104):
        return '전설: 민첩함'
    elif(a==9105):
        return '전설: 강인함'
    elif(a==9103):
        return '전설: 핏빛 길'
    elif(a==8014):
        return '최후의 일격'
    elif(a==8017):
        return '체력차 극복'
    elif(a==8299):
        return '최후의 저항'
    elif(a==8437):
        return '착취의 손아귀'
    elif(a==8439):
        return '여진'
    elif(a==8465):
        return '수호자'
    elif(a==8446):
        return '철거'
    elif(a==8463):
        return '생명의 샘'
    elif(a==8401):
        return '보호막 강타'
    elif(a==8429):
        return '사전준비'
    elif(a==8444):
        return '재생의 바람'
    elif(a==8473):
        return '뼈 방패'
    elif(a==8451):
        return '과잉성장'
    elif(a==8453):
        return '소생'
    elif(a==8242):
        return '불굴의 의지'
    elif(a==8214):
        return '콩콩이 소한'
    elif(a==8229):
        return '신비로운 유성'
    elif(a==8230):
        return '난입'
    elif(a==8224):
        return '무효화 구체'
    elif(a==8226):
        return '마나순환 팔찌'
    elif(a==8275):
        return '빛의 망토'
    elif(a==8210):
        return '깨달음'
    elif(a==8234):
        return '기민함'
    elif(a==8233):
        return '절대집중'
    elif(a==8237):
        return '주문작열'
    elif(a==8232):
        return '물 위를 걷는 자'
    elif(a==8236):
        return '폭풍의 결집'
    elif(a==5008):
        return '적응형능력치+9'
    elif(a==5003):
        return '마법저항력+8'
    elif(a==5005):
        return '공격속도+10%'
    elif(a==5002):
        return '방어력+6'
    elif(a==5007):
        return '스킬가속+8'
    elif(a==5001):
        return '체력+15~90'


while(1):
    a="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+my_name+'?api_key='+api_key
    r=requests.get(a)
    id=r.json()['id']
    b="https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+id+"?api_key="+api_key
    r=requests.get(b)
    try:
        r.json()['gameId']
    except KeyError:
        print_namelist_status()
        continue

    a=r.json()['participants']
    teamId=0
    for i in range(10):
        if(a[i]['summonerName']==my_name):
            teamId=a[i]['teamId']
    opponent_runeId_list=[]
    opponent_name_list=[]
    if(teamId==200):
        for i in range(0, 5):
            opponent_runeId_list.append(a[i]['perks']['perkIds'])
            opponent_name_list.append(a[i]['summonerName'])
        for i in range(0,5):
            for j in range(0,9):
                opponent_runeId_list[i][j]=runeId_to_print_rune(opponent_runeId_list[i][j])
    if(teamId==100):
        for i in range(5, 10):
            opponent_runeId_list.append(a[i]['perks']['perkIds'])
            opponent_name_list.append(a[i]['summonerName'])
        for i in range(0, 5):
            for j in range(0,9):
                opponent_runeId_list[i][j]=runeId_to_print_rune(opponent_runeId_list[i][j])
    for i in range(5):
        print(opponent_name_list[i])
        print(opponent_runeId_list[i])
    print("신발: 4m 28s  우통: 4m 14s  둘다: 3m 51s")
    break
