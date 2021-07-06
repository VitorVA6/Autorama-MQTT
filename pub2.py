import paho.mqtt.client as mqtt
import time
from datetime import datetime, timedelta
import _thread as thread
import mercury

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

voltaCarro1 = -1
voltaCarro2 = -1
voltaCarro3 = -1
voltaCarro4 = -1

tags = []
raceTags = []
tagBuffer = []
r = True

#Método que adiciona uma tag ao buffer
def add_buffer(carro, tempo, volta):
    tagBuffer.append({'tag':carro, 'time': tempo, 'sent':'false', 'volta':volta})
    raceTags.append(carro)

#Filtragem de tags para preenchimento do buffer
def tag_filter(tag, tempo):
    global voltaCarro1
    global voltaCarro2
    global voltaCarro3
    global voltaCarro4
    if(tag not in raceTags and tag == tags[0]):
        voltaCarro1+=1
        tagBuffer.append({'tag':tags[0], 'time': tempo, 'sent':'false', 'volta':str(voltaCarro1)})
        raceTags.append(tags[0])
    if(tag not in raceTags and tag == tags[1]):
        voltaCarro2+=1
        tagBuffer.append({'tag':tags[1], 'time': tempo, 'sent':'false', 'volta':str(voltaCarro2)})
        raceTags.append(tags[1])
    if(tag not in raceTags and tag == tags[2]):
        voltaCarro3+=1
        tagBuffer.append({'tag':tags[2], 'time': tempo, 'sent':'false', 'volta':str(voltaCarro3)})
        raceTags.append(tags[2])
    if(tag not in raceTags and tag == tags[3]):
        voltaCarro4+=1
        tagBuffer.append({'tag':tags[3], 'time': tempo, 'sent':'false', 'volta':str(voltaCarro4)})
        raceTags.append(tags[3])

#Instanciamento do leitor e início do looping de ativação do leitor
def reader_thread_qualify(tempo):
    reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
    reader.set_region("NA2")
    reader.set_read_plan([1], "GEN2", read_power=1500)
    reader.start_reading(lambda tag: tag_filter(tag.epc.decode(), datetime.fromtimestamp(tag.timestamp)))
    time.sleep(tempo)
    reader.stop_reading()

#Instanciamento do leitor e início do looping de ativação do leitor
def reader_thread_race():
    reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
    reader.set_region("NA2")
    reader.set_read_plan([1], "GEN2", read_power=1500)
    reader.start_reading(lambda tag: tag_filter(tag.epc.decode(), datetime.fromtimestamp(tag.timestamp)))
    time.sleep(240)
    reader.stop_reading()

#Método que irá receber as mesnagens do publicador e decodificá-las
def on_message(client, userdata, message):
    global settings
    settings = str(message.payload.decode('utf-8')).split('/')
    tags.append(settings[0])
    tags.append(settings[1])
    tags.append(settings[2])
    tags.append(settings[3])
    print(settings)
    
#Método que se inscreve no tópico "Settings" para receber as configurações da corrida e qualificatória
def get_settings():
    global run
    global settings    
    client.loop_start()
    client.subscribe('Settings')
    client.on_message = on_message
    time.sleep(15)
    client.loop_stop()
        
#Método responsável por públicar os dados da qualificatória, quando o produtor/consumidor for atualizado
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
            time2 = timedelta(seconds = 20)
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

#Método responsável por públicar os dados da corrida, quando o produtor/consumidor for atualizado
def reader_race():
    global voltaCarro1
    global voltaCarro2
    global voltaCarro3
    global voltaCarro4
    voltaCarro1 = -1
    voltaCarro2 = -1
    voltaCarro3 = -1
    voltaCarro4 = -1
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
            time2 = timedelta(seconds = 20)
            if(time1 > time2):
                del(tagBuffer[0])
                del(raceTags[0])
        
    print('Terminando a corrida')
    print(tagBuffer)

#Looping responsável por controlar a leitura de tags para cadastro dos carros
while True:
    confirm = input("Deseja ler uma tag?(y/n):")
    if(confirm == 'n'):
        break
    else:
        reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
        reader.set_region("NA2")
        reader.set_read_plan([1], "GEN2", read_power=1500)
        epcs = map(lambda t: t.epc.decode(), reader.read())
        tag = list(epcs)
        if(len(tag)>0):
            client.publish('Tag', tag[0])
a = input('Pressione para receber settings')
get_settings()
a = input('Pressione pra iniciar Qualify:')
reader_qualify()
a = input('Pressione pra iniciar Corrida:')
reader_race()