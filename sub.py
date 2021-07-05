import paho.mqtt.client as mqtt
import time
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
import _thread as thread
from itertools import groupby
from functools import reduce

piloto1 = {'tag':'', 'nome':'', 'record':timedelta(minutes=10), 'time':timedelta(), 'position':'_', 'anterior':0, 'atual':0, 'volta':'0'}
piloto2 = {'tag':'', 'nome':'', 'record':timedelta(minutes=10), 'time':timedelta(), 'position':'_', 'anterior':0, 'atual':0, 'volta':'0'}
piloto3 = {'tag':'', 'nome':'', 'record':timedelta(minutes=10), 'time':timedelta(), 'position':'_', 'anterior':0, 'atual':0, 'volta':'0'}
piloto4 = {'tag':'', 'nome':'', 'record':timedelta(minutes=10), 'time':timedelta(), 'position':'_', 'anterior':0, 'atual':0, 'volta':'0'}
run = True
check_sub_car1 = True
check_sub_car2 = True
check_sub_car3 = True
check_sub_car4 = True
config = []

def on_message(client, userdata, message):
    global config
    groups = []
    msg = str(message.payload.decode('utf-8')).split('/')
    qualifyCars = [piloto1, piloto2, piloto3, piloto4]
    if(msg[-1]=='set' and len(config)==0):
        piloto1['tag'] = msg[0]        
        piloto2['tag'] = msg[1]        
        piloto3['tag'] = msg[2]        
        piloto4['tag'] = msg[3]        
        piloto1['nome'] = msg[6]
        piloto2['nome'] = msg[7]
        piloto3['nome'] = msg[8]
        piloto4['nome'] = msg[9]
        config.append(msg[4])
        config.append(msg[5])
        label_settings.configure(text='Configs obtidas')
        print(config)
    elif(msg[0]==piloto1['tag'] and msg[-1]!='set'):
        if(msg[2]=='0'):
            label_nome2_car1.configure(text=piloto1['nome'])
            piloto1['anterior'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto1['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto1['time'] = piloto1['atual'] - piloto1['anterior']
            if(piloto1['time']<piloto1['record']):
                piloto1['record'] = piloto1['time']
            piloto1['anterior'] = piloto1['atual']
            piloto1['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_time2_car1.configure(text=str(piloto1['time'])[3:11])
            label_record2_car1.configure(text=str(piloto1['record'])[3:11])
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_volta2_car1.configure(text=piloto1['volta'])
            print(piloto1['tag'], piloto1['position'], piloto1['time'], piloto1['record'], piloto1['volta'])
            client.publish('Qualify/Pil1','carro1'+'-'+ piloto1['nome']+'-'+piloto1['position']+'-'+str(piloto1['time'])[3:11]+'-'+\
                str(piloto1['record'])[3:11]+'-'+piloto1['volta'])
    elif(msg[0]==piloto2['tag']):
        if(msg[2]=='0'):
            label_nome2_car2.configure(text=piloto2['nome'])
            piloto2['anterior'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto2['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto2['time'] = piloto2['atual'] - piloto2['anterior']
            if(piloto2['time']<piloto2['record']):
                piloto2['record'] = piloto2['time']
            piloto2['anterior'] = piloto2['atual']
            piloto2['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_time2_car2.configure(text=str(piloto2['time'])[3:11])
            label_record2_car2.configure(text=str(piloto2['record'])[3:11])
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_volta2_car2.configure(text=piloto2['volta'])
            print(piloto2['tag'], piloto2['position'], piloto2['time'], piloto2['record'], piloto2['volta'])
            client.publish('Qualify/Pil2', 'carro2'+'-'+piloto2['nome']+'-'+piloto2['position']+'-'+str(piloto2['time'])[3:11]+'-'+\
                str(piloto2['record'])[3:11]+'-'+piloto2['volta'])
    elif(msg[0]==piloto3['tag']):
        if(msg[2]=='0'):
            label_nome2_car3.configure(text=piloto3['nome'])
            piloto3['anterior']=datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto3['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto3['time'] = piloto3['atual'] - piloto3['anterior']
            if(piloto3['time']<piloto3['record']):
                piloto3['record'] = piloto3['time']
            piloto3['anterior'] = piloto3['atual']
            piloto3['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_time2_car3.configure(text=str(piloto3['time'])[3:11])
            label_record2_car3.configure(text=str(piloto3['record'])[3:11])
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_volta2_car3.configure(text=piloto3['volta'])
            print(piloto3['tag'], piloto3['position'], piloto3['time'], piloto3['record'], piloto3['volta'])
            client.publish('Qualify/Pil3', 'carro3'+'-'+piloto3['nome']+'-'+piloto3['position']+'-'+str(piloto3['time'])[3:11]+'-'+\
                str(piloto3['record'])[3:11]+'-'+piloto3['volta'])
    elif(msg[0]==piloto4['tag']):
        if(msg[2]=='0'):
            label_nome2_car4.configure(text=piloto4['nome'])
            piloto4['anterior']=datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto4['atual'] = datetime.strptime(msg[1], '%Y-%m-%d %H:%M:%S.%f')
            piloto4['time'] = piloto4['atual'] - piloto4['anterior']
            if(piloto4['time']<piloto4['record']):
                piloto4['record'] = piloto4['time']
            piloto4['anterior'] = piloto4['atual']
            piloto4['volta']=msg[2]
            qualifyCars.sort(key = lambda c: c['record'])
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_time2_car4.configure(text=str(piloto4['time'])[3:11])
            label_record2_car4.configure(text=str(piloto4['record'])[3:11])
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_volta2_car4.configure(text=piloto4['volta'])
            print(piloto4['tag'], piloto4['position'], piloto4['time'], piloto4['record'], piloto4['volta'])
            client.publish('Qualify/Pil4', 'carro4'+'-'+piloto4['nome']+'-'+piloto4['position']+'-'+str(piloto4['time'])[3:11]+'-'+\
                str(piloto4['record'])[3:11]+'-'+piloto4['volta'])
    elif(msg[0]=='race' and msg[1]==piloto1['tag']):
        if(msg[3]=='0'):
            label_nome2_car1.configure(text=piloto1['nome'])
            piloto1['anterior']=datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto1['atual'] = datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
            piloto1['time'] += piloto1['atual'] - piloto1['anterior']
            piloto1['anterior'] = piloto1['atual']
            piloto1['volta']=msg[3]
            qualifyCars.sort(key = lambda x:x['volta'], reverse=True)
            for (key, group) in groupby(qualifyCars, key=lambda x:x['volta']):
                aux = list(group)
                aux.sort(key= lambda x:x['time'])
                groups.append(aux)
            qualifyCars = reduce(lambda x,y: x+y, groups)
            groups.clear()
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_time2_car1.configure(text=str(piloto1['time'])[3:11])
            label_volta2_car1.configure(text=piloto1['volta'])
            print(piloto1['tag'], piloto1['position'], piloto1['time'], piloto1['volta'])
            client.publish('Qualify/Pil1', 'carro1'+'-'+piloto1['nome']+'-'+piloto1['position']+'-'+str(piloto1['time'])[3:11]+'-'+\
                '_'+'-'+ piloto1['volta'])
    elif(msg[0]=='race' and msg[1]==piloto2['tag']):
        if(msg[3]=='0'):
            label_nome2_car2.configure(text=piloto2['nome'])
            piloto2['anterior']=datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto2['atual'] = datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
            piloto2['time'] += piloto2['atual'] - piloto2['anterior']
            piloto2['anterior'] = piloto2['atual']
            piloto2['volta']=msg[3]
            qualifyCars.sort(key = lambda x:x['volta'], reverse=True)
            for (key, group) in groupby(qualifyCars, key=lambda x:x['volta']):
                aux = list(group)
                aux.sort(key= lambda x:x['time'])
                groups.append(aux)
            qualifyCars = reduce(lambda x,y: x+y, groups)
            groups.clear()
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_time2_car2.configure(text=str(piloto2['time'])[3:11])            
            label_volta2_car2.configure(text=piloto2['volta'])
            print(piloto2['tag'], piloto2['position'], piloto2['time'], piloto2['volta'])
            client.publish('Qualify/Pil2', 'carro2'+'-'+piloto2['nome']+'-'+piloto2['position']+'-'+str(piloto2['time'])[3:11]+'-'+\
                '_'+'-'+piloto2['volta'])
    elif(msg[0]=='race' and msg[1]==piloto3['tag']):
        if(msg[3]=='0'):
            label_nome2_car3.configure(text=piloto3['nome'])
            piloto3['anterior']=datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto3['atual'] = datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
            piloto3['time'] += piloto3['atual'] - piloto3['anterior']
            piloto3['anterior'] = piloto3['atual']
            piloto3['volta']=msg[3]         
            qualifyCars.sort(key = lambda x:x['volta'], reverse=True)
            for (key, group) in groupby(qualifyCars, key=lambda x:x['volta']):
                aux = list(group)
                aux.sort(key= lambda x:x['time'])
                groups.append(aux)
            qualifyCars = reduce(lambda x,y: x+y, groups)
            groups.clear()
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_time2_car3.configure(text=str(piloto3['time'])[3:11])
            label_volta2_car3.configure(text=piloto3['volta'])
            print(piloto3['tag'], piloto3['position'], piloto3['time'], piloto3['volta'])
            client.publish('Qualify/Pil3', 'carro3'+'-'+piloto3['nome']+'-'+piloto3['position']+'-'+str(piloto3['time'])[3:11]+'-'+\
                '_'+'-'+piloto3['volta'])
    elif(msg[0]=='race' and msg[1]==piloto4['tag']):
        if(msg[3]=='0'):
            label_nome2_car4.configure(text=piloto4['nome'])
            piloto4['anterior']=datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
        else:
            piloto4['atual'] = datetime.strptime(msg[2], '%Y-%m-%d %H:%M:%S.%f')
            piloto4['time'] += piloto4['atual'] - piloto4['anterior']
            piloto4['anterior'] = piloto4['atual']
            piloto4['volta']=msg[3]
            qualifyCars.sort(key = lambda x:x['volta'], reverse=True)
            for (key, group) in groupby(qualifyCars, key=lambda x:x['volta']):
                aux = list(group)
                aux.sort(key= lambda x:x['time'])
                groups.append(aux)
            qualifyCars = reduce(lambda x,y: x+y, groups)
            groups.clear()
            qualifyCars[0]['position']='1'
            qualifyCars[1]['position']='2'
            qualifyCars[2]['position']='3'
            qualifyCars[3]['position']='4'
            label_pos2_car1.configure(text=piloto1['position'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_time2_car4.configure(text=str(piloto4['time'])[3:11])            
            label_volta2_car4.configure(text=piloto4['volta'])
            print(piloto4['tag'], piloto4['position'], piloto4['time'], piloto4['volta'])
            client.publish('Qualify/Pil4', 'carro4'+'-'+piloto4['nome']+'-'+piloto4['position']+'-'+str(piloto4['time'])[3:11]+'-'+\
                '_'+'-'+piloto4['volta'])

def qualify():
    client.subscribe('Corrida/#')
    client.loop_start()
    client.on_message = on_message
    time.sleep(int(config[1])+10)
    client.loop_stop()     
    race()   

def race():
    global piloto1
    global piloto2
    global piloto3
    global piloto4
    piloto1['time'] = timedelta()
    piloto2['time'] = timedelta()
    piloto3['time'] = timedelta()
    piloto4['time'] = timedelta()
    label_qualify.configure(text='Corrida')
    client.subscribe('Corrida/#')
    client.loop_start()
    client.on_message = on_message
    time.sleep(500)
    client.loop_stop()

def get_settings():
    client.loop_start()
    client.subscribe('Settings')
    client.on_message = on_message
    time.sleep(10)
    client.loop_stop()
    label_settings.configure(text='Tudo pronto!')

def get_set():
    thread.start_new_thread(get_settings, ())

def quali():
    start_screen.forget()
    label_qualify.pack(pady=20)
    screen_car1.pack(pady=30)
    screen_car2.pack(pady=30)
    screen_car3.pack(pady=30)
    screen_car4.pack(pady=30)
    screen_buttons.pack(pady=20, side=BOTTOM)
    screen.pack()
    thread.start_new_thread(qualify, ())
    
s = Tk()
s.title('Calculador')
s.geometry('680x570')

mqttBroker = 'broker.emqx.io'
port = 1883
client = mqtt.Client("Sub")
client.connect(mqttBroker, port)

screen = Frame(s)
start_screen = Frame(s)
screen_car1 = Frame(screen)
screen_car2 = Frame(screen)
screen_car3 = Frame(screen)
screen_car4 = Frame(screen)
screen_buttons = Frame(s)

label_qualify = Label(screen, text='Qualificatória', font = 'verdana 16 bold')
label_nome_car1 = Label(screen_car1, text='Nome:', font = 'verdana 11 bold')
label_nome_car1.grid(row = 0, column = 0, padx = 25)
label_nome2_car1 = Label(screen_car1, text=piloto1['nome'], font = 'verdana 11')
label_nome2_car1.grid(row = 1, column = 0, padx = 25)

label_pos_car1 = Label(screen_car1, text='Pos:', font = 'verdana 11 bold')
label_pos_car1.grid(row = 0, column = 1, padx = 25)
label_pos2_car1 = Label(screen_car1, text=piloto1['position'], font = 'verdana 11')
label_pos2_car1.grid(row = 1, column = 1, padx = 25)

label_time_car1 = Label(screen_car1, text='Tempo:', font = 'verdana 11 bold')
label_time_car1.grid(row = 0, column = 2, padx = 25)
label_time2_car1 = Label(screen_car1, text=piloto1['time'], font = 'verdana 11')
label_time2_car1.grid(row = 1, column = 2, padx = 25)

label_record_car1 = Label(screen_car1, text='Record:', font = 'verdana 11 bold')
label_record_car1.grid(row = 0, column = 3, padx = 25)
label_record2_car1 = Label(screen_car1, text=piloto1['record'], font = 'verdana 11')
label_record2_car1.grid(row = 1, column = 3, padx = 25)

label_volta_car1 = Label(screen_car1, text='Volta:', font = 'verdana 11 bold')
label_volta_car1.grid(row = 0, column = 4, padx = 25)
label_volta2_car1 = Label(screen_car1, text=piloto1['volta'], font = 'verdana 11')
label_volta2_car1.grid(row = 1, column = 4, padx = 25)


label_nome_car2 = Label(screen_car2, text='Nome:', font = 'verdana 11 bold')
label_nome_car2.grid(row = 0, column = 0, padx = 25)
label_nome2_car2 = Label(screen_car2, text=piloto2['nome'], font = 'verdana 11')
label_nome2_car2.grid(row = 1, column = 0, padx = 25)

label_pos_car2 = Label(screen_car2, text='Pos:', font = 'verdana 11 bold')
label_pos_car2.grid(row = 0, column = 1, padx = 25)
label_pos2_car2 = Label(screen_car2, text=piloto2['position'], font = 'verdana 11')
label_pos2_car2.grid(row = 1, column = 1, padx = 25)

label_time_car2 = Label(screen_car2, text='Tempo:', font = 'verdana 11 bold')
label_time_car2.grid(row = 0, column = 2, padx = 25)
label_time2_car2 = Label(screen_car2, text=piloto2['time'], font = 'verdana 11')
label_time2_car2.grid(row = 1, column = 2, padx = 25)

label_record_car2 = Label(screen_car2, text='Record:', font = 'verdana 11 bold')
label_record_car2.grid(row = 0, column = 3, padx = 25)
label_record2_car2 = Label(screen_car2, text=piloto2['record'], font = 'verdana 11')
label_record2_car2.grid(row = 1, column = 3, padx = 25)

label_volta_car2 = Label(screen_car2, text='Volta:', font = 'verdana 11 bold')
label_volta_car2.grid(row = 0, column = 4, padx = 25)
label_volta2_car2 = Label(screen_car2, text=piloto2['volta'], font = 'verdana 11')
label_volta2_car2.grid(row = 1, column = 4, padx = 25)


label_nome_car3 = Label(screen_car3, text='Nome:', font = 'verdana 11 bold')
label_nome_car3.grid(row = 0, column = 0, padx = 25)
label_nome2_car3 = Label(screen_car3, text=piloto3['nome'], font = 'verdana 11')
label_nome2_car3.grid(row = 1, column = 0, padx = 25)

label_pos_car3 = Label(screen_car3, text='Pos:', font = 'verdana 11 bold')
label_pos_car3.grid(row = 0, column = 1, padx = 25)
label_pos2_car3 = Label(screen_car3, text=piloto3['position'], font = 'verdana 11')
label_pos2_car3.grid(row = 1, column = 1, padx = 25)

label_time_car3 = Label(screen_car3, text='Tempo:', font = 'verdana 11 bold')
label_time_car3.grid(row = 0, column = 2, padx = 25)
label_time2_car3 = Label(screen_car3, text=piloto3['time'], font = 'verdana 11')
label_time2_car3.grid(row = 1, column = 2, padx = 25)

label_record_car3 = Label(screen_car3, text='Record:', font = 'verdana 11 bold')
label_record_car3.grid(row = 0, column = 3, padx = 25)
label_record2_car3 = Label(screen_car3, text=piloto3['record'], font = 'verdana 11')
label_record2_car3.grid(row = 1, column = 3, padx = 25)

label_volta_car3 = Label(screen_car3, text='Volta:', font = 'verdana 11 bold')
label_volta_car3.grid(row = 0, column = 4, padx = 25)
label_volta2_car3 = Label(screen_car3, text=piloto3['volta'], font = 'verdana 11')
label_volta2_car3.grid(row = 1, column = 4, padx = 25)


label_nome_car4 = Label(screen_car4, text='Nome:', font = 'verdana 11 bold')
label_nome_car4.grid(row = 0, column = 0, padx = 25)
label_nome2_car4 = Label(screen_car4, text=piloto4['nome'], font = 'verdana 11')
label_nome2_car4.grid(row = 1, column = 0, padx = 25)

label_pos_car4 = Label(screen_car4, text='Pos:', font = 'verdana 11 bold')
label_pos_car4.grid(row = 0, column = 1, padx = 25)
label_pos2_car4 = Label(screen_car4, text=piloto4['position'], font = 'verdana 11')
label_pos2_car4.grid(row = 1, column = 1, padx = 25)

label_time_car4 = Label(screen_car4, text='Tempo:', font = 'verdana 11 bold')
label_time_car4.grid(row = 0, column = 2, padx = 25)
label_time2_car4 = Label(screen_car4, text=piloto4['time'], font = 'verdana 11')
label_time2_car4.grid(row = 1, column = 2, padx = 25)

label_record_car4 = Label(screen_car4, text='Record:', font = 'verdana 11 bold')
label_record_car4.grid(row = 0, column = 3, padx = 25)
label_record2_car4 = Label(screen_car4, text=piloto4['record'], font = 'verdana 11')
label_record2_car4.grid(row = 1, column = 3, padx = 25)

label_volta_car4 = Label(screen_car4, text='Volta:', font = 'verdana 11 bold')
label_volta_car4.grid(row = 0, column = 4, padx = 25)
label_volta2_car4 = Label(screen_car4, text=piloto4['volta'], font = 'verdana 11')
label_volta2_car4.grid(row = 1, column = 4, padx = 25)

button = Button(start_screen, text='Start', width = 12, font = 'verdana 10 bold', command=quali)
button.pack()

button2 = Button(start_screen, text='Settings', width = 12, font = 'verdana 10 bold', command=get_set)
button2.pack()

label_settings = Label(start_screen, text='', font = 'verdana 11')
label_settings.pack(side=BOTTOM)

start_screen.pack(expand=True)

s.mainloop()