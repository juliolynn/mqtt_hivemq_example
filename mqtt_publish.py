from time import sleep
from dotenv import dotenv_values
import paho.mqtt.client as paho
from paho import mqtt

config = dotenv_values(".env")  

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set(config["USERNAME"], config["PASSWORD"])
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect(config["HOST"], int(config["PORT"]), 60)

client.loop_start()

temp = 0

while True:
    temp += 1
    sleep(5)
    client.publish("paho/temperature", temp)
