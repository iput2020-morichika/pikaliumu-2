import RPi.GPIO as GPIO
import time

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def jinkan():
    while True:
        sensor_state = GPIO.input(pin)
        # print(sensor_state)
        time.sleep(0.5)  
        return sensor_state

if __name__=="__main__":
    jinkan()
