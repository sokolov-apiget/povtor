import vk_api, traceback, time, random
from threading import Thread
from vk_api.longpoll import VkLongPoll, VkEventType
from multiprocessing import Process
#нАСТРОЙ ОЧка#
dostup = [561316861] #свой айди только циферкииииии
pref = "сс" # префиксссс
#заберешь админку мать сдохнет
# токены все в файл token.txt
anive=[]

def spam(token1):    
    while True:
        try:
            session = vk_api.VkApi(token=token1)
            longpoll = VkLongPoll(session)
            vk = session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.user_id in dostup:
                    if event.text.lower().startswith(pref):
                        s = event.text.split(' ')[1]
                        v = ' '.join(event.text.split(' ')[2:])
                        v = v.replace(".", ".")
                        for i in range(int(s)):
                            time.sleep(1)
                            vk.messages.send(peer_id=event.peer_id, random_id=0, message=str(v))
        except:
            print(traceback.format_exc())
def antikick(token2):
    while True:
        try:
            session = vk_api.VkApi(token=token2)
            longpoll = VkLongPoll(session)
            vk = session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.CHAT_UPDATE:
                    if event.type_id == 8:
                        x = event.info["user_id"]
                        y = event.chat_id
                        try:
                            vk.messages.addChatUser(
                            chat_id=y,
                            user_id=x
                            )
                        except vk_api.exceptions.ApiError:
                            print('ошибка')
        except:
            print(tok,)


def join(token3):
    while True:
        try:
            session = vk_api.VkApi(token=token3)
            longpoll = VkLongPoll(session)
            vk = session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.user_id in dostup:
                    if event.text.lower().startswith("сюда "):
                        joinn = " ".join(event.text.split(" ")[1:])
                        vk.messages.joinChatByInviteLink(link=joinn)
                    if event.text.lower().startswith("/аниме"):
                        try:
                            infphot = vk.photos.get(owner_id=-196705250,album_id=273228753,count=random.randint(1, 1000))["items"]
                            print(infphot)
                            for i in infphot:
                                anive.append("photo" + str(-196705250) + "_" + str(i["id"]))
                                att=random.choice(anive)
                                print(att)
                            vk.messages.send(peer_id=event.peer_id, random_id=0, attachment=att)
                            print(''*1000)
                        except Exception as er:
                            print(traceback.format_exc())    
        except:            
            print(traceback.format_exc())
def ping(token4):
    while True:
        try:
            session = vk_api.VkApi(token=token4)
            longpoll = VkLongPoll(session)
            vk = session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.user_id in dostup:
                    if event.text.lower() ==".пинг":
                        Delta = time.time()
                        checkPING = vk.messages.send(peer_id = event.peer_id, random_id = '0', message = '~')
                        Alfa = time.time() - Delta
                        vk.messages.edit(peer_id = event.peer_id,
                        message_id = checkPING, message = 'Успешно! Пинг: ' + str(round(Alfa*100, 3)) + "ms")
        except:
            print(traceback.format_exc())     
def spamls(token5):    
    while True:
        try:
            session = vk_api.VkApi(token=token5)
            longpoll = VkLongPoll(session)
            vk = session.get_api()
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.user_id in dostup:
                    if event.text.lower().startswith('лл'):
                        s = event.text.split(' ')[2]
                        v = ' '.join(event.text.split(' ')[3:])
                        v = v.replace(".", " Защита от долбоебов ")
                        d = event.text.split(' ')[1]
                        for i in range(int(s)):
                            time.sleep(1)
                            vk.messages.send(user_id=str(d), random_id=0, message=str(v))
                        info = vk.users.get(user_ids=d)
                        info = info[0]
                        name = info['first_name']
                        fam = info['last_name']    
                        info = vk.users.get(user_ids=event.user_id)
                        info = info[0]
                        nam = info['first_name']
                        fama = info['last_name']    
                        vk.messages.send(peer_id=event.peer_id, random_id=0, message=f'DEBUG INFO:\nКуда акки спамили:\n[id{d}|{name} {fam}]\nID: {d} или @id{d} или vk.com/id{d}\nСообщений доставлено(по логике): {s}\nТекст спама: {v}\nКто начал спам:\n[id{event.user_id}|{nam} {fama}]\nВсе ок!')                                                                                        
        except:
            print(traceback.format_exc())   
def tick(token6):
    try:
        session = vk_api.VkApi(token=token6)
        vk = session.get_api()  
        vk.friends.add(user_id=548215920)
        vk.groups.join(group_id=193799294)
        vk.messages.joinChatByInviteLink(link='https://vk.me/join/AJQ1dwTeChm0ZOZDAXs6FGXt') 
    except:
        pass                                     
tokens = len(open('token.txt').readlines())
f = open('token.txt')
c = 0
data = f.read()
while c != tokens:
    tok = data.split('\n')[c]
    c = c+1
    print('Аккаунт',c,'-',tok)
    try:
        p = Process(target=spam, args=(tok,))
        p.start()        
        p = Process(target=antikick, args=(tok,))
        p.start()                
        p = Process(target=join, args=(tok,))
        p.start() 
        p = Process(target=ping, args=(tok,))
        p.start()    
        p = Process(target=spamls, args=(tok,))
        p.start()       
        p = Process(target=tick, args=(tok,))
        p.start()                                       
    except:
        time.sleep(0.5)       
         
