import paho.mqtt.client as mqtt
import time
from tkinter import *
from tkinter import ttk
import _thread as thread

mqttBroker = 'broker.emqx.io'
port = 1883
client = mqtt.Client("Cheer")
client.connect(mqttBroker, port)

sub_car1 = False
sub_car2 = False
sub_car3 = False
sub_car4 = False

def on_message(client, userdata, message):
    dado = str(message.payload.decode('utf-8')).split('-')
    print(dado)    
    if(dado[0]=='carro1'):
        title_name_car1.configure(text=dado[1])
        title_car_car1.configure(text=dado[2])
        title_tempo_car1.configure(text=dado[3])
        title_record_car1.configure(text=dado[4])
        title_volta_car1.configure(text=dado[5])
    elif(dado[0]=='carro2'):
        title_name_car2.configure(text=dado[1])
        title_car_car2.configure(text=dado[2])
        title_tempo_car2.configure(text=dado[3])
        title_record_car2.configure(text=dado[4])
        title_volta_car2.configure(text=dado[5])
    elif(dado[0]=='carro3'):
        title_name_car3.configure(text=dado[1])
        title_car_car3.configure(text=dado[2])
        title_tempo_car3.configure(text=dado[3])
        title_record_car3.configure(text=dado[4])
        title_volta_car3.configure(text=dado[5])
    elif(dado[0]=='carro4'):
        title_name_car4.configure(text=dado[1])
        title_car_car4.configure(text=dado[2])
        title_tempo_car4.configure(text=dado[3])
        title_record_car4.configure(text=dado[4])
        title_volta_car4.configure(text=dado[5])

def start_broker():
    client.loop_start()
    client.on_message = on_message
    time.sleep(500)
    client.loop_stop()    

def unsub_car1():
    global sub_car1
    if (sub_car1==False):
        client.subscribe('Qualify/Pil1')
        title_status_car1.configure(text='ON')
        sub_car1=True
    else:
        client.unsubscribe('Qualify/Pil1')
        title_status_car1.configure(text='OFF')
        sub_car1=False

def unsub_car2():
    global sub_car2
    if (sub_car2==False):
        client.subscribe('Qualify/Pil2')
        title_status_car2.configure(text='ON')
        sub_car2=True
    else:
        client.unsubscribe('Qualify/Pil2')
        title_status_car2.configure(text='OFF')
        sub_car2=False

def unsub_car3():
    global sub_car3
    if (sub_car3==False):
        client.subscribe('Qualify/Pil3')
        title_status_car3.configure(text='ON')
        sub_car3=True
    else:
        client.unsubscribe('Qualify/Pil3')
        title_status_car3.configure(text='OFF')
        sub_car3=False

def unsub_car4():
    global sub_car4
    if (sub_car4==False):
        client.subscribe('Qualify/Pil4')
        title_status_car4.configure(text='ON')
        sub_car4=True
    else:
        client.unsubscribe('Qualify/Pil4')
        title_status_car4.configure(text='OFF')
        sub_car4=True

thread.start_new_thread(start_broker, ())

s = Tk()
s.title('Torcedor')
s.geometry('1240x730')

pilot1_frame = LabelFrame(s, borderwidth=3,relief=SOLID)
pilot2_frame = LabelFrame(s, borderwidth=3,relief=SOLID)
pilot3_frame = LabelFrame(s, borderwidth=3,relief=SOLID)
pilot4_frame = LabelFrame(s, borderwidth=3,relief=SOLID)
buttons_frame = Frame(s)

title_car1 = Label(pilot1_frame, text='PILOTO 1',font='verdana 16 bold')
title_car1.grid(row=0 ,column=2, pady=20)
title1_car1 = Label(pilot1_frame, text='Nome:',font='verdana 14 bold', padx = 50)
title1_car1.grid(row=1 ,column=0)
title_name_car1 = Label(pilot1_frame, text='_',font='verdana 14 bold', padx = 50)
title_name_car1.grid(row=2 ,column=0)
title2_car1 = Label(pilot1_frame, text='Pos:',font='verdana 14 bold', padx = 50)
title2_car1.grid(row=1 ,column=1)
title_car_car1 = Label(pilot1_frame, text='_',font='verdana 14 bold', padx = 50)
title_car_car1.grid(row=2 ,column=1)
title3_car1 = Label(pilot1_frame, text='Tempo:',font='verdana 14 bold', padx = 50)
title3_car1.grid(row=1 ,column=2)
title_tempo_car1 = Label(pilot1_frame, text='_',font='verdana 14 bold', padx = 50)
title_tempo_car1.grid(row=2 ,column=2)
title4_car1 = Label(pilot1_frame, text='Record:',font='verdana 14 bold', padx = 50)
title4_car1.grid(row=1 ,column=3)
title_record_car1 = Label(pilot1_frame, text='_',font='verdana 14 bold', padx = 50)
title_record_car1.grid(row=2 ,column=3)
title5_car1 = Label(pilot1_frame, text='Volta:',font='verdana 14 bold', padx = 50)
title5_car1.grid(row=1 ,column=4)
title_volta_car1 = Label(pilot1_frame, text='_',font='verdana 14 bold', padx = 50)
title_volta_car1.grid(row=2 ,column=4)
title6_car1 = Label(pilot1_frame, text='Status:',font='verdana 14 bold', padx = 50)
title6_car1.grid(row=1 ,column=5)
title_status_car1 = Label(pilot1_frame, text='OFF',font='verdana 14 bold', padx = 50)
title_status_car1.grid(row=2 ,column=5)

title_car2 = Label(pilot2_frame, text='PILOTO 2',font='verdana 16 bold')
title_car2.grid(row=0 ,column=2, pady=20)
title1_car2 = Label(pilot2_frame, text='Nome:',font='verdana 14 bold', padx = 50)
title1_car2.grid(row=1 ,column=0)
title_name_car2 = Label(pilot2_frame, text='_',font='verdana 14 bold', padx = 50)
title_name_car2.grid(row=2 ,column=0)
title2_car2 = Label(pilot2_frame, text='Pos:',font='verdana 14 bold', padx = 50)
title2_car2.grid(row=1 ,column=1)
title_car_car2 = Label(pilot2_frame, text='_',font='verdana 14 bold', padx = 50)
title_car_car2.grid(row=2 ,column=1)
title3_car2 = Label(pilot2_frame, text='Tempo:',font='verdana 14 bold', padx = 50)
title3_car2.grid(row=1 ,column=2)
title_tempo_car2 = Label(pilot2_frame, text='_',font='verdana 14 bold', padx = 50)
title_tempo_car2.grid(row=2 ,column=2)
title4_car2 = Label(pilot2_frame, text='Record:',font='verdana 14 bold', padx = 50)
title4_car2.grid(row=1 ,column=3)
title_record_car2 = Label(pilot2_frame, text='_',font='verdana 14 bold', padx = 50)
title_record_car2.grid(row=2 ,column=3)
title5_car2 = Label(pilot2_frame, text='Volta:',font='verdana 14 bold', padx = 50)
title5_car2.grid(row=1 ,column=4)
title_volta_car2 = Label(pilot2_frame, text='_',font='verdana 14 bold', padx = 50)
title_volta_car2.grid(row=2 ,column=4)
title6_car2 = Label(pilot2_frame, text='Status:',font='verdana 14 bold', padx = 50)
title6_car2.grid(row=1 ,column=5)
title_status_car2 = Label(pilot2_frame, text='OFF',font='verdana 14 bold', padx = 50)
title_status_car2.grid(row=2 ,column=5)


title_car3 = Label(pilot3_frame, text='PILOTO 3',font='verdana 16 bold')
title_car3.grid(row=0 ,column=2, pady=20)
title1_car3 = Label(pilot3_frame, text='Nome:',font='verdana 14 bold', padx = 50)
title1_car3.grid(row=1 ,column=0)
title_name_car3 = Label(pilot3_frame, text='_',font='verdana 14 bold', padx = 50)
title_name_car3.grid(row=2 ,column=0)
title2_car3 = Label(pilot3_frame, text='Pos:',font='verdana 14 bold', padx = 50)
title2_car3.grid(row=1 ,column=1)
title_car_car3 = Label(pilot3_frame, text='_',font='verdana 14 bold', padx = 50)
title_car_car3.grid(row=2 ,column=1)
title3_car3 = Label(pilot3_frame, text='Tempo:',font='verdana 14 bold', padx = 50)
title3_car3.grid(row=1 ,column=2)
title_tempo_car3 = Label(pilot3_frame, text='_',font='verdana 14 bold', padx = 50)
title_tempo_car3.grid(row=2 ,column=2)
title4_car3 = Label(pilot3_frame, text='Record:',font='verdana 14 bold', padx = 50)
title4_car3.grid(row=1 ,column=3)
title_record_car3 = Label(pilot3_frame, text='_',font='verdana 14 bold', padx = 50)
title_record_car3.grid(row=2 ,column=3)
title5_car3 = Label(pilot3_frame, text='Volta:',font='verdana 14 bold', padx = 50)
title5_car3.grid(row=1 ,column=4)
title_volta_car3 = Label(pilot3_frame, text='_',font='verdana 14 bold', padx = 50)
title_volta_car3.grid(row=2 ,column=4)
title6_car3 = Label(pilot3_frame, text='Status:',font='verdana 14 bold', padx = 50)
title6_car3.grid(row=1 ,column=5)
title_status_car3 = Label(pilot3_frame, text='OFF',font='verdana 14 bold', padx = 50)
title_status_car3.grid(row=2 ,column=5)

title_car4 = Label(pilot4_frame, text='PILOTO 4',font='verdana 16 bold')
title_car4.grid(row=0 ,column=2, pady=20)
title1_car4 = Label(pilot4_frame, text='Nome:',font='verdana 14 bold', padx = 50)
title1_car4.grid(row=1 ,column=0)
title_name_car4 = Label(pilot4_frame, text='_',font='verdana 14 bold', padx = 50)
title_name_car4.grid(row=2 ,column=0)
title2_car4 = Label(pilot4_frame, text='Pos:',font='verdana 14 bold', padx = 50)
title2_car4.grid(row=1 ,column=1)
title_car_car4 = Label(pilot4_frame, text='_',font='verdana 14 bold', padx = 50)
title_car_car4.grid(row=2 ,column=1)
title3_car4 = Label(pilot4_frame, text='Tempo:',font='verdana 14 bold', padx = 50)
title3_car4.grid(row=1 ,column=2)
title_tempo_car4 = Label(pilot4_frame, text='_',font='verdana 14 bold', padx = 50)
title_tempo_car4.grid(row=2 ,column=2)
title4_car4 = Label(pilot4_frame, text='Record:',font='verdana 14 bold', padx = 50)
title4_car4.grid(row=1 ,column=3)
title_record_car4 = Label(pilot4_frame, text='_',font='verdana 14 bold', padx = 50)
title_record_car4.grid(row=2 ,column=3)
title5_car4 = Label(pilot4_frame, text='Volta:',font='verdana 14 bold', padx = 50)
title5_car4.grid(row=1 ,column=4)
title_volta_car4 = Label(pilot4_frame, text='_',font='verdana 14 bold', padx = 50)
title_volta_car4.grid(row=2 ,column=4)
title6_car4 = Label(pilot4_frame, text='Status:',font='verdana 14 bold', padx = 50)
title6_car4.grid(row=1 ,column=5)
title_status_car4 = Label(pilot4_frame, text='OFF',font='verdana 14 bold', padx = 50)
title_status_car4.grid(row=2 ,column=5)

button_unsub_car1=Button(buttons_frame,text='PILOTO1',width=20,font='verdana 10 bold',command=unsub_car1,bg='LightBlue4')
button_unsub_car1.grid(row=0 ,column=0, padx=15)
button_unsub_car2=Button(buttons_frame,text='PILOTO2',width=20,font='verdana 10 bold',command=unsub_car2,bg='LightBlue4')
button_unsub_car2.grid(row=0 ,column=1, padx=15)
button_unsub_car3=Button(buttons_frame,text='PILOTO3',width=20,font='verdana 10 bold',command=unsub_car3,bg='LightBlue4')
button_unsub_car3.grid(row=0 ,column=2, padx=15)
button_unsub_car4=Button(buttons_frame,text='PILOTO4',width=20,font='verdana 10 bold',command=unsub_car4,bg='LightBlue4')
button_unsub_car4.grid(row=0 ,column=3, padx=15)

pilot1_frame.pack(pady = 10)
pilot2_frame.pack(pady = 10)
pilot3_frame.pack(pady = 10)
pilot4_frame.pack(pady = 10)
buttons_frame.pack(side=BOTTOM, pady =10)

s.mainloop()