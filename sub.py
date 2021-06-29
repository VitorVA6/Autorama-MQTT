import paho.mqtt.client as mqtt
import time
from datetime import datetime
from tkinter import *
from tkinter import ttk
import _thread as thread

piloto1 = {'tag':'carro1', 'record':300, 'time':0, 'position':'_', 'anterior':0, 'atual':0, 'volta':'_'}
piloto2 = {'tag':'carro2', 'record':300, 'time':0, 'position':'_' , 'anterior':0, 'atual':0, 'volta':'_'}
piloto3 = {'tag':'carro3', 'record':300, 'time':0, 'position':'_' , 'anterior':0, 'atual':0, 'volta':'_'}
piloto4 = {'tag':'carro4', 'record':300, 'time':0, 'position':'_' , 'anterior':0, 'atual':0, 'volta':'_'}
run = True
check_sub_car1 = True
check_sub_car2 = True
check_sub_car3 = True
check_sub_car4 = True

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
            label_time2_car1.configure(text=piloto1['time'])
            label_record2_car1.configure(text=piloto1['record'])
            label_pos2_car1.configure(text=piloto1['position'])
            label_volta2_car1.configure(text=piloto1['volta'])
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
            label_time2_car2.configure(text=piloto2['time'])
            label_record2_car2.configure(text=piloto2['record'])
            label_pos2_car2.configure(text=piloto2['position'])
            label_volta2_car2.configure(text=piloto2['volta'])
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
            label_time2_car3.configure(text=piloto3['time'])
            label_record2_car3.configure(text=piloto3['record'])
            label_pos2_car3.configure(text=piloto3['position'])
            label_volta2_car3.configure(text=piloto3['volta'])
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
            label_time2_car4.configure(text=piloto4['time'])
            label_record2_car4.configure(text=piloto4['record'])
            label_pos2_car4.configure(text=piloto4['position'])
            label_volta2_car4.configure(text=piloto4['volta'])
            print(piloto4['tag'], piloto4['position'], piloto4['time'], piloto4['record'], piloto4['volta'])

def qualify():
    global run
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
s.title('Torcedor')
s.geometry('680x570')

screen = Frame(s)
start_screen = Frame(s)
screen_car1 = Frame(screen)
screen_car2 = Frame(screen)
screen_car3 = Frame(screen)
screen_car4 = Frame(screen)
screen_buttons = Frame(s)

label_qualify = Label(screen, text='Qualificatória', font = 'verdana 16 bold')
label_tag_car1 = Label(screen_car1, text='Tag:', font = 'verdana 11 bold')
label_tag_car1.grid(row = 0, column = 0, padx = 25)
label_Tag2_car1 = Label(screen_car1, text=piloto1['tag'], font = 'verdana 11')
label_Tag2_car1.grid(row = 1, column = 0, padx = 25)

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


label_tag_car2 = Label(screen_car2, text='Tag:', font = 'verdana 11 bold')
label_tag_car2.grid(row = 0, column = 0, padx = 25)
label_Tag2_car2 = Label(screen_car2, text=piloto2['tag'], font = 'verdana 11')
label_Tag2_car2.grid(row = 1, column = 0, padx = 25)

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


label_tag_car3 = Label(screen_car3, text='Tag:', font = 'verdana 11 bold')
label_tag_car3.grid(row = 0, column = 0, padx = 25)
label_Tag2_car3 = Label(screen_car3, text=piloto3['tag'], font = 'verdana 11')
label_Tag2_car3.grid(row = 1, column = 0, padx = 25)

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


label_tag_car4 = Label(screen_car4, text='Tag:', font = 'verdana 11 bold')
label_tag_car4.grid(row = 0, column = 0, padx = 25)
label_Tag2_car4 = Label(screen_car4, text=piloto4['tag'], font = 'verdana 11')
label_Tag2_car4.grid(row = 1, column = 0, padx = 25)

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

def sub_car1():
    global check_sub_car1
    if(check_sub_car1==True):
        screen_car1.forget()
        check_sub_car1 = False
    else:
        screen_car1.pack(pady=30)
        check_sub_car1 = True

def sub_car2():
    global check_sub_car2
    if(check_sub_car2==True):
        screen_car2.forget()
        check_sub_car2 = False
    else:
        screen_car2.pack(pady=30)
        check_sub_car2 = True

def sub_car3():
    global check_sub_car3
    if(check_sub_car3==True):
        screen_car3.forget()
        check_sub_car3 = False
    else:
        screen_car3.pack(pady=30)
        check_sub_car3 = True

def sub_car4():
    global check_sub_car4
    if(check_sub_car4==True):
        screen_car4.forget()
        check_sub_car4 = False
    else:
        screen_car4.pack(pady=30)
        check_sub_car4 = True

button_car1 = Button(screen_buttons, text=piloto1['tag'], width = 12, font = 'verdana 10 bold', command=sub_car1)
button_car1.grid(row = 0, column = 1)
button_car2 = Button(screen_buttons, text=piloto2['tag'], width = 12, font = 'verdana 10 bold', command=sub_car2)
button_car2.grid(row = 0, column = 2)
button_car3 = Button(screen_buttons, text=piloto3['tag'], width = 12, font = 'verdana 10 bold', command=sub_car3)
button_car3.grid(row = 0, column = 3)
button_car4 = Button(screen_buttons, text=piloto4['tag'], width = 12, font = 'verdana 10 bold', command=sub_car4)
button_car4.grid(row = 0, column = 4)

button = Button(start_screen, text='Qualify', width = 12, font = 'verdana 10 bold', command=quali)
button.pack()

start_screen.pack(expand=True)

s.mainloop()