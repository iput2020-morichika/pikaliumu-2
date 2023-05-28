import RPi.GPIO as GPIO
import time

pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def jinkan():
    sensor_state = GPIO.input(pin)
    time.sleep(0.5)  
    return sensor_state

if __name__=="__main__":
    while True:
        state = jinkan()
        print(state)
