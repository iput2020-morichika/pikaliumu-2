import RPi.GPIO as GPIO
import time 

class CallBack:

    def __init__(self):

        # 4番pinを入力、プルアップに設定
        pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP) 

        # 割り込みイベント設定
        GPIO.add_event_detect(pin, GPIO.RISING, bouncetime=1000)
        # コールバック関数登録
        GPIO.add_event_callback(pin, self.my_callback_one) 
        GPIO.add_event_callback(pin, self.my_callback_two)
                    
    def my_callback_one(self, channel):
        print('Callback one')
    
    def my_callback_two(self, channel):
        print('Callback two')

    def callback_test(self):
        while True:
            time.sleep(1)

cb = CallBack()
cb.callback_test() # 割り込みイベント待ち