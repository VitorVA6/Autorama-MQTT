import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print('Mensagem recebida: ', str(message.payload.decode('utf-8')))

mqttBroker = 'broker.emqx.io'
port = 1883
client = mqtt.Client()
client.connect(mqttBroker, port)

client.loop_start()
client.subscribe('Corrida/#')
client.on_message = on_message
time.sleep(32)
client.loop_stop()