import paho.mqtt.client as mqtt
import time
from datetime import datetime, timedelta
import _thread as thread

#Configuração do broker
#mqttBroker = 'broker.emqx.io'
#port = 1883
mqttBroker = 'broker.emqx.io'
port = 1883
client = mqtt.Client("Pub")
client.connect(mqttBroker, port)
settings=''
run = True
r = True
#Configuração da corrida

tags = []
raceTags = []
tagBuffer = []
r = True

def add_buffer(carro, tempo, volta):
    tagBuffer.append({'tag':carro, 'time': tempo, 'sent':'false', 'volta':volta})
    raceTags.append(carro)

def reader_thread_qualify(tempo):
    print('entrei na thread')
    c=0
    voltaCarro1 = -1
    voltaCarro2 = -1
    voltaCarro3 = -1
    voltaCarro4 = -1
    while c<tempo*10:
        if(len(tags)>0):
            if(tags[0] not in raceTags):
                voltaCarro1+=1
                thread.start_new_thread(add_buffer, (tags[0], datetime.fromtimestamp(time.time()), str(voltaCarro1)))
        if(len(tags)>1):
            if(tags[1] not in raceTags):
                voltaCarro2+=1
                thread.start_new_thread(add_buffer, (tags[1], datetime.fromtimestamp(time.time()), str(voltaCarro2)))
        if(len(tags)>2):
            if(tags[2] not in raceTags):
                voltaCarro3+=1
                thread.start_new_thread(add_buffer, (tags[2], datetime.fromtimestamp(time.time()), str(voltaCarro3)))
        if(len(tags)>3):
            if(tags[3] not in raceTags):
                voltaCarro4+=1
                thread.start_new_thread(add_buffer, (tags[3], datetime.fromtimestamp(time.time()), str(voltaCarro4)))
        time.sleep(0.1)
        c+=1
    print('Thread encerrada')
    return

def reader_thread_race():
    global r
    print('entrei na thread')
    print(tagBuffer)
    c=0
    voltaCarror1 = -1
    voltaCarror2 = -1
    voltaCarror3 = -1
    voltaCarror4 = -1
    while r:
        if(len(tags)>0):
            if(tags[0] not in raceTags):
                voltaCarror1+=1
                thread.start_new_thread(add_buffer, (tags[0], datetime.fromtimestamp(time.time()), str(voltaCarror1)))
        if(len(tags)>1):
            if(tags[1] not in raceTags):
                voltaCarror2+=1
                thread.start_new_thread(add_buffer, (tags[1], datetime.fromtimestamp(time.time()), str(voltaCarror2)))
        if(len(tags)>2):
            if(tags[2] not in raceTags):
                voltaCarror3+=1
                thread.start_new_thread(add_buffer, (tags[2], datetime.fromtimestamp(time.time()), str(voltaCarror3)))
        if(len(tags)>3):
            if(tags[3] not in raceTags):
                voltaCarror4+=1
                thread.start_new_thread(add_buffer, (tags[3], datetime.fromtimestamp(time.time()), str(voltaCarror4)))
        time.sleep(0.1)
        c+=1
    print('Thread encerrada')
    return

def on_message(client, userdata, message):
    global settings
    settings = str(message.payload.decode('utf-8')).split('/')
    tags.append(settings[0])
    tags.append(settings[1])
    tags.append(settings[2])
    tags.append(settings[3])
    print(settings)
    

def get_settings():
    global run
    global settings    
    client.loop_start()
    client.subscribe('Settings')
    client.on_message = on_message
    time.sleep(15)
    client.loop_stop()
        
def reader_qualify():
    global settings
    print('Começando qualify')    
    a = datetime.fromtimestamp(time.time())
    thread.start_new_thread(reader_thread_qualify, (int(settings[5]),))
    while True:         
        if(len(tagBuffer)>0 and tagBuffer[0]['sent'] == 'false'):
            info =  raceTags[0]+ '/'+ str(tagBuffer[0]['time'])+ '/'+ tagBuffer[0]['volta']
            client.publish('Corrida/Carro1', info)            
            tagBuffer[0]['sent'] = 'true'
        if(len(tagBuffer)>1 and tagBuffer[1]['sent'] == 'false'):
            info =  raceTags[1]+ '/'+ str(tagBuffer[1]['time'])+ '/'+ tagBuffer[1]['volta']
            client.publish('Corrida/Carro2', info)            
            tagBuffer[1]['sent'] = 'true'
        if(len(tagBuffer)>2 and tagBuffer[2]['sent'] == 'false'):
            info =  raceTags[2]+ '/'+ str(tagBuffer[2]['time'])+ '/'+ tagBuffer[2]['volta']
            client.publish('Corrida/Carro3', info)            
            tagBuffer[2]['sent'] = 'true'        
        if(len(tagBuffer)>3 and tagBuffer[3]['sent'] == 'false'):
            info =  raceTags[3]+ '/'+ str(tagBuffer[3]['time'])+ '/'+ tagBuffer[3]['volta']
            client.publish('Corrida/Carro4', info)            
            tagBuffer[3]['sent'] = 'true'
        if (len(tagBuffer)>0):
            time1 = datetime.fromtimestamp(time.time()) - tagBuffer[0]['time']
            time2 = timedelta(seconds = 70)
            if(time1 > time2):
                del(tagBuffer[0])
                del(raceTags[0])
        time3 = datetime.fromtimestamp(time.time()) - a
        time4 = timedelta(seconds = int(settings[5]))
        if(time3>time4):
            break
    print('terminando a qualify')
    tagBuffer.clear()
    raceTags.clear()

def reader_race():
    global raceTags
    global tagBuffer
    raceTags.clear()
    tagBuffer.clear()
    global r
    global settings
    r = True
    print('Começando corrida')    
    thread.start_new_thread(reader_thread_race, ())
    while True:         
        if(len(tagBuffer)>0 and tagBuffer[0]['sent'] == 'false'):
            info = 'race' + '/' + raceTags[0]+ '/'+ str(tagBuffer[0]['time'])+ '/'+ tagBuffer[0]['volta']
            client.publish('Corrida/Carro1', info)            
            tagBuffer[0]['sent'] = 'true'
        elif(len(tagBuffer)>1 and tagBuffer[1]['sent'] == 'false'):
            info = 'race' + '/' + raceTags[1]+ '/'+ str(tagBuffer[1]['time'])+ '/'+ tagBuffer[1]['volta']
            client.publish('Corrida/Carro2', info)            
            tagBuffer[1]['sent'] = 'true'
        elif(len(tagBuffer)>2 and tagBuffer[2]['sent'] == 'false'):
            info = 'race' + '/' + raceTags[2]+ '/'+ str(tagBuffer[2]['time'])+ '/'+ tagBuffer[2]['volta']
            client.publish('Corrida/Carro3', info)            
            tagBuffer[2]['sent'] = 'true'        
        elif(len(tagBuffer)>3 and tagBuffer[3]['sent'] == 'false'):
            info = 'race' + '/' + raceTags[3]+ '/'+ str(tagBuffer[3]['time'])+ '/'+ tagBuffer[3]['volta']
            client.publish('Corrida/Carro4', info)            
            tagBuffer[3]['sent'] = 'true'
        elif (len(tagBuffer)>3):
            if(int(tagBuffer[0]['volta'])>=int(settings[4]) and int(tagBuffer[1]['volta'])>=int(settings[4])and\
                int(tagBuffer[2]['volta'])>=int(settings[4]) and int(tagBuffer[3]['volta'])>=int(settings[4])):
                time.sleep(2)
                tagBuffer.clear()
                raceTags.clear()
                tags.clear()
                r = False
                break
        if (len(tagBuffer)>0):
            time1 = datetime.fromtimestamp(time.time()) - tagBuffer[0]['time']
            time2 = timedelta(seconds = 6)
            if(time1 > time2):
                del(tagBuffer[0])
                del(raceTags[0])
        
    print('Terminando a corrida')
    print(tagBuffer)

while True:
    confirm = input("Deseja ler uma tag?(y/n):")
    if(confirm == 'n'):
        break
    else:
        client.publish('Tag', 'Tome aqui sua tag')
a = input('Pressione para receber settings')
get_settings()
a = input('Pressione pra iniciar Qualify:')
reader_qualify()
a = input('Pressione pra iniciar Corrida:')
reader_race()