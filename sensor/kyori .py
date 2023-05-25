#
# R1：10k（負荷抵抗）
# R2：5k（検出距離約10cmのはず）
#
import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def main():
  try:
    while True:
        sensor_state = GPIO.input(pin)
        # print(sensor_state)
        # time.sleep(0.5)
        if sensor_state == GPIO.HIGH:
          print("検出")
        else:
          print("---")
        time.sleep(1)


  except KeyboardInterrupt:
      pass

if __name__=="__main__":
  main()

