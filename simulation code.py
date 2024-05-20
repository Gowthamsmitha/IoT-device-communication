import paho.mqtt.client as mqtt
import ssl
import warnings

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

class IoTNetworkSimulator:
    def __init__(self, client_id):
        self.client = None
        self.client_id = client_id

    def connect_to_broker(self, broker_address, port, username=None, password=None):
        try:
            self.client = mqtt.Client(client_id=self.client_id)
            # Enable TLS/SSL
            self.client.tls_set_context(ssl.create_default_context())
            # Set username and password 
            if username and password:
                self.client.username_pw_set(username=username, password=password)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(broker_address, port)
            print("Connected to MQTT broker securely.")
            self.client.loop_start()
        except ConnectionRefusedError:
            print("Connection refused: Check if the MQTT broker is running.")
        except OSError as e:
            print(f"Error connecting to MQTT broker: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def subscribe_to_topics(self, topics):
        if self.client:
            for topic in topics:
                self.client.subscribe(topic)
            print("Subscribed to topics:", topics)
        else:
            print("Error: Not connected to MQTT broker.")

    def publish_message(self, topic, message):
        if self.client:
            self.client.publish(topic, message)
            print(f"Published message on topic {topic}: {message}")
        else:
            print("Error: Not connected to MQTT broker.")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code " + str(rc))

    def on_message(self, client, userdata, msg):
        print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

    def disconnect(self):
        if self.client:
            self.client.disconnect()
            print("Disconnected from MQTT broker.")
        else:
            print("Error: Not connected to MQTT broker.")

if __name__ == "__main__":
    # Initialize the simulator with a unique client ID
    simulator = IoTNetworkSimulator("client001")

    # Connect to MQTT broker securely
    broker_address = "192.168.43.188"
    port = 1883
    username = "your_username"
    password = "your_password"
    simulator.connect_to_broker(broker_address, port, username, password)

    # Subscribe to topics
    simulator.subscribe_to_topics(["test/topic"])

    # Publish a message
    simulator.publish_message("test/topic", "Hello from simulator!")

    # Disconnect from MQTT broker
    simulator.disconnect()

