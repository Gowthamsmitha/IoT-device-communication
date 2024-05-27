# Basic IoT Device Communication Simulator

Overview : This project is a basic simulator that models the communication between IoT devices in a network. The focus will be on setting up secure connections and simple message exchanges between devices.

# Working Features 

The code provides a basic framework for simulating an IoT network using MQTT, allowing communication between devices via a broker. It handles connection, subscription, and message publishing functionalities.
Currently it deals with:
1. Class defenition ie, to encapsulate the functionality of the MQTT client simulation.
2. Initialization: It initializes the MQTT client with a given client ID.
3. Connection to MQTT Broker: It establishes a secure connection to an MQTT broker and sets the username and password for authentication.
4. Subscription to Topics: It enables publishing messages to a specific MQTT topic.
5. Callbacks: This method is called when the client connects to the MQTT broker. It prints the connection result code.
6. Main Execution: It subscribes to the topic "test/topic" and displays a message "Hello from simulator!" to the topic "test/topic".

# Requirements

1. Python 3.x
2. Paho MQTT Client Library
3. MQTT Broker: The code connects to an external MQTT broker hosted at "test.mosquitto.org" on port 1883.
4. Random Module: The code uses the random module to generate random temperature readings.

# Configuration

1. Import Required Modules
2. Define IoT Device Classes:

      IoTDevice: Represents a generic IoT device.
      TemperatureSensor: Simulates a temperature sensor device.
      LightSwitch: Simulates a light switch device
3. Define MQTT Client Setup
4. Define Callback Functions
5. Define Main Functionality

# Authentication 


1. The authenticate method takes a password as input.
2. It compares the provided password with a hardcoded password ("gowtham123" in this case).
3. If the provided password matches the hardcoded password, the authenticated attribute of the device is set to True, indicating successful authentication.
4. If the passwords do not match, authentication fails, and the authenticated attribute remains False.
5. In the main function, after creating instances of TemperatureSensor and LightSwitch, the user is prompted to enter a password for authentication.
6. The entered password is then passed to the authenticate method of each device.
7. Authentication continues until both devices are successfully authenticated (authenticated attribute set to True).

# Key Points to be noted 

1. MQTT availability: Ensure that the MQTT broker is running and accessible .
2. Network Connectivity
3. Security Considerations: Ensure that the broker is configured to support TLS/SSL and has valid certificates.
4. Client ID should be unique
5. Ensure that the topics are correctly specified




