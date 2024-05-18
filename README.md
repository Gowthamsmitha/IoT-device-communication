# Basic IoT Device Communication Simulator

Overview : This project is a basic simulator that models the communication between IoT devices in a network. The focus will be on setting up secure connections and simple message exchanges between devices.

Working Features :The code provides a basic framework for simulating an IoT network using MQTT, allowing communication between devices via a broker. It handles connection, subscription, and message publishing functionalities.
Currently it deals with:
1. Class defenition ie, to encapsulate the functionality of the MQTT client simulation.
2. Initialization: It initializes the MQTT client with a given client ID.
3. Connection to MQTT Broker: It establishes a secure connection to an MQTT broker and sets the username and password for authentication.
4. Subscription to Topics: It enables publishing messages to a specific MQTT topic.
5. Callbacks: This method is called when the client connects to the MQTT broker. It prints the connection result code.
6. Main Execution: It subscribes to the topic "test/topic" and displays a message "Hello from simulator!" to the topic "test/topic".

Key Points to be noted :
1. MQTT availability: Ensure that the MQTT broker is running and accessible .
2. Network Connectivity
3. Security Considerations: Ensure that the broker is configured to support TLS/SSL and has valid certificates.
4. Client ID should be unique
5. Ensure that the topics are correctly specified




