import sys
from Adafruit_IO import MQTTClient
import time
import random
from esp32cam import ESP32Cam 
from detect import process_image

esp32cam = ESP32Cam('http://192.168.213.104/cam-lo.jpg')  

# AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "minhpham51"
AIO_KEY = ""

# def connected(client):
#     print("Ket noi thanh cong ...")
#     for topic in AIO_FEED_IDs:
#         client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

# def message(client , feed_id , payload):
#     print("Nhan du lieu: " + payload + ", feed id:" + feed_id)
#     if feed_id == "nutnhan1":
#         if payload == "0":
#             writeData("1")
#         else:
#             writeData("2")
#     if feed_id == "nutnhan2":
#         if payload == "0":
#             writeData("3")
#         else:
#             writeData("4")

client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
client.on_disconnect = disconnected
# client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
sensor_type = 0
ai_result = ""
previous_result = ""

while True:
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        image = esp32cam.get_frame()
        previous_result = ai_result
        ai_result = process_image(image)
        print("AI Output: ", ai_result)
        if previous_result != ai_result:
            client.publish("ai", ai_result)
    
    time.sleep(1)
