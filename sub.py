import paho.mqtt.client as mqtt
import time
from datetime import date, datetime, timedelta

piloto1 = {'tag':'carro1', 'record':300, 'time':0, 'position':'', 'anterior':0, 'atual':0, 'volta':''}
piloto2 = {'tag':'carro2', 'record':300, 'time':0, 'position':'' , 'anterior':0, 'atual':0, 'volta':''}
piloto3 = {'tag':'carro3', 'record':300, 'time':0, 'position':'' , 'anterior':0, 'atual':0, 'volta':''}
piloto4 = {'tag':'carro4', 'record':300, 'time':0, 'position':'' , 'anterior':0, 'atual':0, 'volta':''}
run = True

def on_message(client, userdata, message):
    msg = str(message.payload.decode('utf-8')).split('/')
    qualifyCars = [piloto1, piloto2, piloto3, piloto4]
    if(msg[0]=='carro1'):
        if(msg[2]=='0'):
            piloto1['anterior'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto1['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto1['time'] = float(str(piloto1['atual'] - piloto1['anterior'])[5:])
            if(piloto1['time']<piloto1['record']):
                piloto1['record'] = piloto1['time']
            piloto1['anterior'] = piloto1['atual']
            piloto1['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            print(piloto1['tag'], piloto1['position'], piloto1['time'], piloto1['record'], piloto1['volta'])
    if(msg[0]=='carro2'):
        if(msg[2]=='0'):
            piloto2['anterior'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto2['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto2['time'] = float(str(piloto2['atual'] - piloto2['anterior'])[5:])
            if(piloto2['time']<piloto2['record']):
                piloto2['record'] = piloto2['time']
            piloto2['anterior'] = piloto2['atual']
            piloto2['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            print(piloto2['tag'], piloto2['position'], piloto2['time'], piloto2['record'], piloto2['volta'])
    if(msg[0]=='carro3'):
        if(msg[2]=='0'):
            piloto3['anterior']=datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto3['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto3['time'] = float(str(piloto3['atual'] - piloto3['anterior'])[5:])
            if(piloto3['time']<piloto3['record']):
                piloto3['record'] = piloto3['time']
            piloto3['anterior'] = piloto3['atual']
            piloto3['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            print(piloto3['tag'], piloto3['position'], piloto3['time'], piloto3['record'], piloto3['volta'])
    if(msg[0]=='carro4'):
        if(msg[2]=='0'):
            piloto4['anterior']=datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto4['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto4['time'] = float(str(piloto4['atual'] - piloto4['anterior'])[5:])
            if(piloto4['time']<piloto4['record']):
                piloto4['record'] = piloto4['time']
            piloto4['anterior'] = piloto4['atual']
            piloto4['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            print(piloto4['tag'], piloto4['position'], piloto4['time'], piloto4['record'], piloto4['volta'])
        


    

mqttBroker = 'broker.emqx.io'
port = 1883
client = mqtt.Client("Sub")
client.connect(mqttBroker, port)
while run:
    client.loop()
    client.subscribe('Corrida/#')
    client.on_message = on_message
    if(piloto1['volta']=='3' and piloto2['volta']=='3' and piloto3['volta']=='3' and piloto4['volta']=='3'):
        run = False