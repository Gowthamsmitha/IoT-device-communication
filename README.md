# IoT Device Simulator with MQTT Communication

This project simulates IoT devices, specifically a temperature sensor and a light switch, that communicate via the MQTT protocol. It includes user authentication and error handling for MQTT connection failures.

## Features

- **User Authentication**: Secure authentication using hashed credentials.
- Simulated IoT Devices: Temperature sensor and light switch.
- MQTT Communication: Devices publish messages to an MQTT broker.
- Error Handling: Retry logic for MQTT connection failures.

## prerequisites

- Python 3.x
- `paho-mqtt` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/iot-device-simulation.git
    cd iot-device-simulator
    ```

2. Install the required libraries:
    ```sh
    pip install paho-mqtt python-dotenv
    ```

3. Create a `.env` file in the project directory with the following variables:
    ```sh
    MQTT_BROKER=your_mqtt_broker_address
    MQTT_PORT=your_mqtt_broker_port
    MQTT_TOPIC=your_mqtt_topic
    MQTT_USERNAME=your_mqtt_username
    MQTT_PASSWORD=your_mqtt_password
    DEVICE_USERNAME_HASH=hashed_username
    DEVICE_PASSWORD_HASH=hashed_password
    ```

## Usage

Run the script:
`sh
python iot_device_simulation.py`

## Code Structure

- IoTDevice: Base class for IoT devices, handling authentication and message sending.
- TemperatureSensor: Inherits from IoTDevice, simulates reading temperature.
- LightSwitch: Inherits from IoTDevice, simulates toggling a light switch.
- connect_mqtt: Function to connect to the MQTT broker with retry logic.
- main: Main function to run the application, handle user inputs, and perform actions.


## Working Features 

The code provides a basic framework for simulating an IoT network using MQTT, allowing communication between devices via a broker. It handles connection, subscription, and message publishing functionalities.
Currently it deals with:
1. Class defenition ie, to encapsulate the functionality of the MQTT client simulation.
2. Initialization: It initializes the MQTT client with a given client ID.
3. Connection to MQTT Broker: It establishes a secure connection to an MQTT broker and sets the username and password for authentication.
4. Subscription to Topics: It enables publishing messages to a specific MQTT topic.
5. Callbacks: This method is called when the client connects to the MQTT broker. It prints the connection result code.
6. Main Execution: It subscribes to the topic "test/topic" and displays a message "Hello from simulator!" to the topic "test/topic".

## Requirements

1. Python 3.x
2. Paho MQTT Client Library
3. MQTT Broker: The code connects to an external MQTT broker hosted at "test.mosquitto.org" on port 1883.
4. Random Module: The code uses the random module to generate random temperature readings.

## Configuration

1. Import Required Modules
2. Define IoT Device Classes:

      IoTDevice: Represents a generic IoT device.
      TemperatureSensor: Simulates a temperature sensor device.
      LightSwitch: Simulates a light switch device
3. Define MQTT Client Setup
4. Define Callback Functions
5. Define Main Functionality

## Authentication 


1. The authenticate method takes a username and a password as input.
2. It compares the provided username and password with a hardcoded username and password.
3. If the provided credentials matches the hardcoded credentials, the authenticated attribute of the device is set to True, indicating successful authentication.
4. If the credentials do not match, authentication fails, and the authenticated attribute remains False.
5. In the main function, after creating instances of TemperatureSensor and LightSwitch, the user is prompted to enter a password and username for authentication.
6. The entered credentials are then passed to the authenticate method of each device.
7. Authentication continues until both devices are successfully authenticated (authenticated attribute set to True).

## Error Handling


- The application attempts to connect to the MQTT broker multiple times with a delay between attempts.
- If the connection fails after all attempts, the application exits gracefully.

## Key Points to be noted 

1. MQTT availability: Ensure that the MQTT broker is running and accessible .
2. Network Connectivity
3. Security Considerations: Ensure that the broker is configured to support TLS/SSL and has valid certificates.
4. Client ID should be unique
5. Ensure that the topics are correctly specified




