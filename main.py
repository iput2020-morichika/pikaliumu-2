"""
ファイルインポート
"""
# from sensor import suion
from sensor import jinkan
from led import led_class

"""
初期化処理
"""
class Flip:
   def __init__(self,flip):
      self.flip = flip
flip = Flip(0)

jinkan.jinkan()    

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

  