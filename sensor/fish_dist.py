#
# R1：10k（負荷抵抗）
# R2：5k（検出距離約10cmのはず）
#
import RPi.GPIO as GPIO
import time

pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def fish():
  try:
        sensor_state = GPIO.input(pin)
        return sensor_state
  except KeyboardInterrupt:
      pass
  

if __name__=="__main__":
  while True:
    status = fish()
    if status == GPIO.LOW:
      print("検出")
    else:
      print("---")
    time.sleep(0.5)

