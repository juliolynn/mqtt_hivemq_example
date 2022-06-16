from time import sleep
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()

temp = 0

while True:
    temp += 1
    sleep(5)
    client.publish("paho/temperature", temp)
