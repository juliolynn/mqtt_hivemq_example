Pull and run HiveMQ Community Edition MQTT broker Container
`
docker pull hivemq/hivemq-ce
docker run --name hivemq-ce -d -p 1883:1883 hivemq/hivemq-ce
`

Install Eclipse Paho MQTT Python client library
`
pip install paho-mqtt
`

(Optiona) Run ngrok to be able to connect from outside of the local network
`
ngrok tcp 1883
`