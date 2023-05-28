"""
ファイルインポート
"""
# from sensor import suion
from sensor import jinkan, fish_dist, suion, water_dist, ph
from led import led_class
import RPi.GPIO as GPIO

"""
初期化処理
"""
class Flip:
   def __init__(self,flip):
      self.flip = flip
flip = Flip(0)

jinkan.jinkan()         #人感
fish_dist.fish()        #水中距離
suion.read_temp()       #水温
water_dist.water_dist() #水位
ph.pH_concent()         #pH

while True:
  if jinkan.jinkan() == 1:  #人感センサ反応でLED点灯
    print("点灯")
    led_class.Gra_led.laser(flip)
  else:
    led_class.trun_off()    #消灯
    print("消灯")


# s1 = suion.temp_c
# print (s1)

# if s1 > 26.0:

GPIO.cleanup()