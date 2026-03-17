import time
import json
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "facu/greenhouse/data"

DEVICE = "greenhouse_1"

client = mqtt.Client()
client.connect(BROKER, PORT)

while True:
    data = {
        "device": DEVICE,
        "temperature": round(random.uniform(20, 38), 2),
        "air_humidity": round(random.uniform(35, 80), 2),
        "soil_moisture": round(random.uniform(15, 60), 2),
        "timestamp": datetime.now().isoformat()
    }

    payload = json.dumps(data)
    client.publish(TOPIC, payload)

    print("Publicado:", payload)

    time.sleep(5)