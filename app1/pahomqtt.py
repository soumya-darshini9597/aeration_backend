import paho.mqtt.client as mqtt
from app1.models import Areation
from datetime import datetime
import json

# MQTT Configuration
MQTT_BROKER = 'mqttbroker.bc-pl.com'
MQTT_PORT = 1883
MQTT_TOPICS = ['pump/compressor/status', 'pump/stepper/status']  # List of topics you want to subscribe to
MQTT_USER = 'mqttuser'
MQTT_PASSWORD = 'Bfl@2025'


topic_aliases = {
    "pump/compressor/status": "compressor",
    "pump/stepper/status": "stepper",
}


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        topic = msg.topic

        # Use alias from dictionary or fallback to original topic
        alias = topic_aliases.get(topic, topic)

        formatted_state = f"{alias}: {payload}"
        print(f"Received and formatted: {formatted_state}")

        # Save to the database
        Areation.objects.create(state=formatted_state)

    except Exception as e:
        print(f"Error processing message: {e}")




# Callback function when a message is received
# def on_message(client, userdata, msg):
#     try:
#         payload = msg.payload.decode('utf-8')
#         topic = msg.topic
#         print(f"Received from topic: {topic} : {payload}")
        
#         # Assuming your payload is a simple value, you can change this if it's JSON
#         if topic == 'pump/compressor/status':
#             # Save data for topic1 (pump/compressor/status)
#             Areation.objects.create(state=f"pump/compressor/status: {payload}")
#         elif topic == 'pump/stepper/status':
#             # Save data for topic2 (pump/stepper/status)
#             Areation.objects.create(state=f"pump/stepper/status: {payload}")
#         else:
#             print(f"Unknown topic: {topic}")

#     except Exception as e:
#         print(f"Error processing message: {e}")



# Callback function when MQTT client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker.")
        for topic in MQTT_TOPICS:
            client.subscribe(topic)
            print(f"Subscribed to topic: {topic}")
    else:
        print(f"Failed to connect with code: {rc}")

# Set up the MQTT client
client = mqtt.Client()
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    print(f"Connected to {MQTT_BROKER}")
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")

# Start the MQTT client loop to handle incoming messages
client.loop_start()

# Keep the script running
try:
    while True:
        pass  # Infinite loop to keep the subscriber running
except KeyboardInterrupt:
    print("Disconnected")
    client.disconnect()
