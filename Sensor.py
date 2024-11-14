import csv
import time
import adafruit_dht
import board
import RPi.GPIO as GPIO
import threading

dht_device = adafruit_dht.DHT11(board.D14)

LDR_PIN = 17
SOIL_MOISTURE_PIN = 4
GPIO.setmode(GPIO.BCM)

fieldnames = ["seconds", "temperature", "humidity", "ldr_value", "soil_moisture"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

seconds = 0
running = True

def read_ldr_value():
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.2)

    GPIO.setup(LDR_PIN, GPIO.IN)

    start_time = time.time()
    while (GPIO.input(LDR_PIN) == GPIO.LOW):
        pass
    discharge_time = time.time() - start_time

    return discharge_time

def read_soil_moisture():
    GPIO.setup(SOIL_MOISTURE_PIN, GPIO.OUT)
    GPIO.output(SOIL_MOISTURE_PIN, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(SOIL_MOISTURE_PIN, GPIO.IN)

    start_time = time.time()
    while GPIO.input(SOIL_MOISTURE_PIN) == GPIO.LOW:
        pass
    discharge_time = time.time() - start_time

    return discharge_time

def read_dht_sensor():
    retries = 5
    for _ in range(retries):
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            if temperature_c is not None and humidity is not None:
                return temperature_c, humidity
        except RuntimeError as error:
            print("Retrying...")
            time.sleep(1)
    return None, None

def read_sensors():
    global seconds, running
    try:
        while running:
            temperature_c, humidity = read_dht_sensor()

            if temperature_c is not None and humidity is not None:
                temperature_f = temperature_c * (9 / 5) + 32

                ldr_value = read_ldr_value()
                soil_moisture_value = read_soil_moisture()

                info = {
                    "seconds": seconds,
                    "temperature": temperature_c,
                    "humidity": humidity,
                    "ldr_value": ldr_value * 100000,
                    "soil_moisture": soil_moisture_value * 100000
                }

                with open('data.csv', 'a') as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writerow(info)

                print("Seconds: {}, Temp: {:.1f} C / {:.1f} F, Humidity: {}%, LDR response: {:.2f} s, Soil Moisture response: {:.2f} s".format(
                    seconds, temperature_c, temperature_f, humidity, ldr_value * 100000, soil_moisture_value * 100000
                ))

                seconds += 2

            time.sleep(2)

    except RuntimeError as err:
        print("Error: ", err.args[0])
    finally:
        GPIO.cleanup()

def listen_for_exit():
    global running
    input("Press 'Enter' to stop...\n")
    running = False

sensor_thread = threading.Thread(target=read_sensors)
sensor_thread.start()

listen_for_exit()

sensor_thread.join()
print("Program ended. GPIO cleaned up.")
