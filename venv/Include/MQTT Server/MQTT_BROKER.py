import time
import paho.mqtt.client as mqtt


# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("Test/#")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    print ( str(msg.payload) )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("soldier.cloudmqtt.com", 18540, 60)
client.username_pw_set("zpdgaazi", "qO-AaU_shyP7")


# client.loop_forever()
client.loop_start()
time.sleep(1)

while True:

    client.publish("Cell id", "set data here")
    client.publish("Time_date", "set data here")
    client.publish("Lat", "set data here")
    client.publish("Long", "set data here")
    client.publish("Speed", "set data here")
    print ("Message Sent")
    time.sleep(15)
   # client.loop_read()

client.loop_stop()
client.disconnect()


