import paho.mqtt.client as mqtt

client_id = ""
username = ""
password = ""

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/phone")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect("shimla-broker.infiswift.tech", 8883)

client.loop_forever()