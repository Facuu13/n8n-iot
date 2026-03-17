import time
import json
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "facu/sensores/temperatura"

SENSORS = [
    "sensor_1",
    "sensor_2",
    "sensor_3",
]

client = mqtt.Client()
client.connect(BROKER, PORT)

while True:
    for sensor in SENSORS:
        temp = round(random.uniform(20, 45), 2)

        data = {
            "device": sensor,
            "temp": temp,
            "timestamp": datetime.now().isoformat()
        }

        payload = json.dumps(data)
        client.publish(TOPIC, payload)

        print("Publicado:", payload)

        time.sleep(0.5)

    time.sleep(5)