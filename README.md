Pull and run HiveMQ Community Edition MQTT broker Container
```
docker pull hivemq/hivemq-ce
docker run --name hivemq-ce -d -p 1883:1883 hivemq/hivemq-ce
```

Install Eclipse Paho MQTT Python client library and other dependencies
```
pip install paho-mqtt
pip install python-dotenv
```

(Optiona) Run ngrok to be able to connect from outside of the local network
```
ngrok tcp 1883
```

Run subscriber
```
python mqtt_subscribe.py
```

Or

Run publisher
```
python mqtt_publish
```
