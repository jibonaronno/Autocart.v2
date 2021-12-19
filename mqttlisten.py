# https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/
# https://pimylifeup.com/raspberry-pi-mosquitto-mqtt-server/
# Linux Command
# mosquitto_pub -h 192.168.88.62 -t "/recvData" -m "Hello world"
import paho.mqtt.client as mqtt

class MqttListen(object):
    def __init__(self):
        self.broker = "portaldevex.com"
        self.port = 1883
        self.recvMsg = ""

    # Callback function which Executes when message received on MQTT
    def on_message(self, client, userdata, message):
        global recvMsg, licPlate
        recvMsg = str(message.payload.decode("utf-8"))
        print("message received:" ,recvMsg.lstrip())
        print("message topic=",message.topic)

    def Subscribe(self):
        #Create MQTT Publisher and subscriber
        client = mqtt.Client("mqtt_listener") #create new instance
        client.connect(host=self.broker, port=self.port, keepalive=60) #connect to broker
        client.loop_start()
        client.subscribe("/recvData") ## Subscribe to topic
        client.on_message = self.on_message # Declare the callback funcion

