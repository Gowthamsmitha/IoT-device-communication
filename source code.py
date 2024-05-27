import random
import paho.mqtt.client as mqtt

class IoTDevice:
    def __init__(self, device_id, device_type, mqtt_client, topic, token):
        self.device_id = device_id
        self.device_type = device_type
        self.mqtt_client = mqtt_client
        self.topic = topic
        self.token = token
        self.authenticated = False

    def authenticate(self, password):
        if password == "gowtham123":
            self.authenticated = True
            print(f"Device {self.device_id}: Authenticated successfully.")
        else:
            print(f"Device {self.device_id}: Authentication failed.")

    def send_message(self, message, token):
        if self.authenticated:
            self.mqtt_client.publish(self.topic, message)
        else:
            print(f"Device {self.device_id}: Not authenticated. Message not sent.")

class TemperatureSensor(IoTDevice):
    def __init__(self, device_id, mqtt_client, topic, token):
        super().__init__(device_id, 'TemperatureSensor', mqtt_client, topic, token)

    def read_temperature(self):
        return round(random.uniform(20.0, 30.0), 2)

class LightSwitch(IoTDevice):
    def __init__(self, device_id, mqtt_client, topic, token):
        super().__init__(device_id, 'LightSwitch', mqtt_client, topic, token)

    def toggle(self, state):
        return "ON" if state else "OFF"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("test.mosquitto.org", 1883, 60)
mqtt_client.loop_start()

def main():
    token = "securetoken"
    temp_sensor = TemperatureSensor("sensor1", mqtt_client, "home/temperature", token)
    light_switch = LightSwitch("switch1", mqtt_client, "home/light", token)

    authenticated = False
    while not authenticated:
        password = input("Enter password: ")
        temp_sensor.authenticate(password)
        light_switch.authenticate(password)
        authenticated = temp_sensor.authenticated and light_switch.authenticated

    while True:
        print("\n1. Read Temperature\n2. Toggle Light\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            temperature = temp_sensor.read_temperature()
            temp_sensor.send_message(f"Temperature: {temperature}°C", token)
        elif choice == '2':
            state = input("Enter state (on/off): ").strip().lower() == 'on'
            status = light_switch.toggle(state)
            light_switch.send_message(f"Light is {status}", token)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
