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
    

def start_broker():
    client.loop_start()
    client.on_message = on_message
    time.sleep(45)
    client.loop_stop()
    

def unsub_car1():
    global sub_car1
    if (sub_car1==False):
        client.subscribe('Qualify/Pil1')
        sub_car1=True
    else:
        client.unsubscribe('Qualify/Pil1')
        sub_car1=False

def unsub_car2():
    global sub_car2
    if (sub_car2==False):
        client.subscribe('Qualify/Pil2')
        sub_car2=True
    else:
        client.unsubscribe('Qualify/Pil2')
        sub_car2=False

def unsub_car3():
    global sub_car3
    if (sub_car3==False):
        client.subscribe('Qualify/Pil3')
        sub_car3=True
    else:
        client.unsubscribe('Qualify/Pil3')
        sub_car3=False

def unsub_car4():
    global sub_car4
    if (sub_car4==False):
        client.subscribe('Qualify/Pil4')
        sub_car4=True
    else:
        client.unsubscribe('Qualify/Pil4')
        sub_car4=True

thread.start_new_thread(start_broker, ())
s = Tk()
s.title('Torcedor')
s.geometry('680x570')

button_unsub_car1 = Button(s, text='Piloto1', width = 12, font = 'verdana 10 bold', command=unsub_car1)
button_unsub_car1.pack()
button_unsub_car2 = Button(s, text='Piloto2', width = 12, font = 'verdana 10 bold', command=unsub_car2)
button_unsub_car2.pack()
button_unsub_car3 = Button(s, text='Piloto3', width = 12, font = 'verdana 10 bold', command=unsub_car3)
button_unsub_car3.pack()
button_unsub_car4 = Button(s, text='Piloto4', width = 12, font = 'verdana 10 bold', command=unsub_car4)
button_unsub_car4.pack()

s.mainloop()


