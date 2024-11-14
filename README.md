# Greenhouse Environment Monitoring Project

This project provides a Raspberry Pi-based solution for monitoring key environmental parameters within a greenhouse, including temperature, humidity, light intensity, and soil moisture. The system uses a DHT11 sensor, LDR sensor, and a resistive soil moisture sensor to collect data, which is then recorded in a CSV file and visualized through real-time graphs.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Hardware Components](#hardware-components)
- [Project Setup](#project-setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Sensor.py](#sensorpy)
  - [Grapher.py](#grapherpy)
- [Example Readings](#example-readings)
- [License](#license)

---

## Project Overview

This monitoring system logs data about temperature, humidity, light levels, and soil moisture in a greenhouse environment. It displays the data in real-time on a Matplotlib-based dashboard with four graphs for easier tracking and analysis.

## Features

- **Continuous Data Collection**: Logs sensor data every two seconds.
- **CSV Data Logging**: Saves readings to a CSV file for easy access and analysis.
- **Real-time Visualization**: Displays temperature, humidity, light intensity, and soil moisture data in real-time.
- **User-Controlled Shutdown**: Graceful exit using an interactive prompt.

## System Requirements

- **Hardware**: Raspberry Pi 3 Model B or higher
- **Sensors**:
  - DHT11 Temperature and Humidity Sensor
  - LDR (Light Dependent Resistor)
  - Resistive Soil Moisture Sensor
- **Software**:
  - Python 3.x
  - Matplotlib
  - pandas
  - adafruit_dht library
  - RPi.GPIO library

## Hardware Components

- **Raspberry Pi 3 Model B** (or higher)
- **DHT11** sensor (connected to GPIO 14)
- **LDR sensor** (connected to GPIO 17)
- **Soil Moisture Sensor** (connected to GPIO 4)
- Breadboard, resistors, and jumper wires as needed for sensor connections

## Project Setup

1. Clone this repository to your Raspberry Pi.
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required libraries:
    ```bash
    pip install pandas matplotlib adafruit-circuitpython-dht
    sudo apt-get install libgpiod2  # Required for Adafruit DHT library
    ```

3. Connect the DHT11, LDR, and Soil Moisture sensors to the specified GPIO pins on the Raspberry Pi.

## Usage

1. **Run `Sensor.py`** to start collecting sensor data and logging it to `data.csv`.
    ```bash
    python3 Sensor.py
    ```
   - To stop data collection, press `Enter` when prompted.

2. **Run `Grapher.py`** to visualize the data from `data.csv` in real time.
    ```bash
    python3 Grapher.py
    ```

## Code Explanation

### Sensor.py

The `Sensor.py` script reads data from the DHT11, LDR, and soil moisture sensors and logs the readings to a CSV file (`data.csv`). It utilizes threading to allow continuous data collection until stopped by user input.

- **Temperature and Humidity**: Collected from the DHT11 sensor.
- **LDR (Light Intensity)**: Measured by the discharge time of an LDR circuit.
- **Soil Moisture**: Measured by the discharge time of a soil moisture circuit.
- **Logging**: Each reading includes the time elapsed, temperature, humidity, light intensity, and soil moisture level.

### Grapher.py

The `Grapher.py` script reads the recorded data from `data.csv` and creates four real-time graphs:
- **Temperature** (in Celsius)
- **Humidity** (as a percentage)
- **LDR Value** (light intensity via discharge time)
- **Soil Moisture** (soil moisture via discharge time)

The graphs update every second, displaying only the last eight data points for each parameter to maintain a focused, real-time view.

## Example Readings

Here are some example readings from the greenhouse environment monitoring project:

- **Temperature Graph**  
  ![image](https://github.com/user-attachments/assets/ad2e6d22-0779-4456-90ba-b912f3e2749b)

- **Humidity Graph**
  ![image](https://github.com/user-attachments/assets/29f2c752-57f5-4b14-8478-0d0a359e6481)

- **Light Intensity (LDR) Graph**
  ![image](https://github.com/user-attachments/assets/eab45e9d-556c-41f3-b2d4-2d5fc686ab16)


- **Soil Moisture Graph**  
  ![image](https://github.com/user-attachments/assets/0311bd45-fcce-4a1d-90ae-e51d325ad935)

## License

This project is licensed under the MIT License.

---

This README covers all essential project details and is GitHub-friendly for display and ease of navigation.
