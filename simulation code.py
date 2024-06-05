import os
import random
import hashlib
import time
import paho.mqtt.client as mqtt

from dotenv import load_dotenv

load_dotenv("/content/secure.env")

class IoTDevice:
    def __init__(self, device_id, device_type, mqtt_client, topic, token):
        self.device_id = device_id
        self.device_type = device_type
        self.mqtt_client = mqtt_client
        self.topic = topic
        self.token = token
        self.authenticated = False

    def authenticate(self, username, password):
        hashed_username = hashlib.sha256(username.encode()).hexdigest()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_username == os.getenv("DEVICE_USERNAME_HASH") and hashed_password == os.getenv("DEVICE_PASSWORD_HASH"):
            self.authenticated = True
            print(f"Device {self.device_id}: Authenticated successfully.")
        else:
            print(f"Device {self.device_id}: Authentication failed.")

    def send_message(self, message):
        self.mqtt_client.publish(self.topic, message)

class TemperatureSensor(IoTDevice):
    def read_temperature(self):
        return random.uniform(20.0, 25.0)  # Simulate reading temperature

class LightSwitch(IoTDevice):
    def toggle(self, state):
        return "on" if state else "off"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def connect_mqtt(client, broker, port, retries=5, delay=5):
    attempts = 0
    while attempts < retries:
        try:
            client.connect(broker, port)
            client.loop_start()
            return True
        except Exception as e:
            attempts += 1
            print(f"Connection attempt {attempts} failed: {e}")
            time.sleep(delay)
    return False

def main():
    broker = os.getenv("MQTT_BROKER")
    port = int(os.getenv("MQTT_PORT"))
    topic = os.getenv("MQTT_TOPIC")
    token = os.getenv("MQTT_PASSWORD")

    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.username_pw_set(username=os.getenv("MQTT_USERNAME"), password=token)

    if not connect_mqtt(mqtt_client, broker, port):
        print("Failed to connect to MQTT broker after several attempts.")
        return

    temp_sensor = TemperatureSensor("sensor1", "temperature", mqtt_client, topic, token)
    light_switch = LightSwitch("switch1", "light", mqtt_client, topic, token)

    authenticated = False
    while not authenticated:
        username = input("Enter username: ")
        password = input("Enter password: ")
        temp_sensor.authenticate(username, password)
        light_switch.authenticate(username, password)
        authenticated = temp_sensor.authenticated and light_switch.authenticated

    while True:
        print("\n1. Read Temperature\n2. Toggle Light\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            temperature = temp_sensor.read_temperature()
            temp_sensor.send_message(f"Temperature: {temperature}°C")
        elif choice == '2':
            state = input("Enter state (on/off): ").strip().lower() == 'on'
            status = light_switch.toggle(state)
            light_switch.send_message(f"Light is {status}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
