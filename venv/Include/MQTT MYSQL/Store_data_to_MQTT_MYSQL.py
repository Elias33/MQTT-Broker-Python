import time
import paho.mqtt.client as mqtt
import pymysql

#connecting to mysql
my_sql_connection = pymysql.connect(host="localhost", user="root", passwd="", db="lol")
myCursor = my_sql_connection.cursor()
dev_time= input("Enter device time:\n")
dev_lat= input("Enter lattitude:\n")
dev_long=input("Enter longtitude:\n")
dev_speed= input("Enter speed:\n")
sql = """INSERT INTO test(time,lat,lng,speed) VALUES('%s','%s','%s','%s')""" % (dev_time, dev_lat, dev_long, dev_speed)
myCursor.execute(sql)
print("insert successfully")

my_sql_connection.commit()
my_sql_connection.close()


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

    client.publish("Cell id", "This data is not defined")
    client.publish("Time_date", dev_time)
    client.publish("Lat", dev_lat)
    client.publish("Long", dev_long)
    client.publish("Speed", dev_speed)
    print ("Message Sent")
    time.sleep(15)
   # client.loop_read()

client.loop_stop()
client.disconnect()


