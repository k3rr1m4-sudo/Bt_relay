# Bluetooth SPP Client Documentation

## Introduction
The Bluetooth SPP Client project is designed to provide a reliable and robust Bluetooth Serial Port Profile (SPP) client implementation. This project facilitates the communication between Bluetooth devices over a serial interface using the SPP protocol.

## Features
- **Easy-to-Use Interface**: Provides a simple API for connecting to Bluetooth devices.
- **Reliable Data Transmission**: Ensures stable and reliable data transmission over Bluetooth.
- **Support for Multiple Devices**: Able to connect and communicate with multiple Bluetooth SPP devices.
- **Event Handling**: Implements event handling for connection, disconnection, and data receipt events.

## Installation
To install the Bluetooth SPP Client project, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/k3rr1m4-sudo/Bt_relay.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Bt_relay
   ```
3. Install the necessary dependencies:
   ```bash
   npm install
   ```

## Usage
To use the Bluetooth SPP Client:
1. Import the client module in your project:
   ```javascript
   const BluetoothSPPClient = require('./path/to/BluetoothSPPClient');
   ```
2. Create an instance of the client:
   ```javascript
   const sppClient = new BluetoothSPPClient();
   ```
3. Connect to a Bluetooth device:
   ```javascript
   sppClient.connect(deviceAddress);
   ```
4. Send data to the connected device:
   ```javascript
   sppClient.send(data);
   ```

## Configuration
The Bluetooth SPP Client can be configured through the following options:
- **deviceAddress**: The Bluetooth address of the device to connect to.
- **timeout**: Connection timeout in milliseconds (default is 5000ms).
- **reconnect**: Boolean flag to enable/disable automatic reconnection attempts (default is true).

## System Requirements
- **Node.js**: Version 14 or higher
- **Bluetooth Adapter**: A compatible Bluetooth adapter must be installed and enabled on your system.
- **Operating System**: The project is compatible with Windows, macOS, and Linux.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.