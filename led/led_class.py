import time
from gpiozero import Button
import board
import neopixel

button = Button(21)
# button = Button(18)

# LED strip configuration:
LED_COUNT   = 144     # Number of LED pixels.
LED_PIN     = board.D18      # GPIO pin
LED_BRIGHTNESS = 0.9  # LED brightness
LED_ORDER = neopixel.GRB # order of LED colours. May also be GRB, GRBW, or RGBW

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)
# Setting variables for a specific sequence

class Flip:
   def __init__(self,flip):
      self.flip = flip

red = (255,0,0)
green = (0,255,0)
flip = Flip(0)

class Simple_led:
   def __init__(self,flip):
      self.flip = flip
   def red(self):
      strip.fill((255,0,0))
      strip.show()
   def green(self):
      strip.fill((0,255,0))
      strip.show()

class Gra_led:
   def __init__(self,flip):
      self.flip = flip
#
#rgb関数：赤青緑をloopして光らせる
#
   def rgb(self):
      while True:
         if value == 0:
            break
         for color in [(255,0,0),(0,255,0),(0,0,255)]:
            for i in range(256):
               r,g,b = color
               strip.fill((int(r*i/255),int(g*i/255),int(b*i/255)))
               strip.show()
               time.sleep(0.01)

#
#グラデーション
#
   def harf(self):
      red_harf = (255,0,0)
      white_harf = (255,255,255)
      while True:
         if value == 0:
            break
         for i in range(LED_COUNT):
            color = (
               int(red_harf[0] * i / (LED_COUNT - 1)),
               int(red_harf[1] * i / (LED_COUNT - 1)),
               int(red_harf[2] * i / (LED_COUNT - 1))
            )
            strip.fill(color)
            strip.show()
            time.sleep(0.01)
         for i in range(LED_COUNT):
            downcolor = (
               int(red_harf[0] * (1 - i / (LED_COUNT - 1))),
               int(red_harf[1] * (1 - i / (LED_COUNT - 1))),
               int(red_harf[2] * (1 - i / (LED_COUNT - 1)))
            )
            strip.fill(downcolor)
            strip.show()
            time.sleep(0.01)
      # for i in range(LED_COUNT):
      #   color = (
      #       int(red_harf[0] * i / (LED_COUNT - 1)),
      #       int(red_harf[1] * i / (LED_COUNT - 1)),
      #       int(red_harf[2] * i / (LED_COUNT - 1))
      #   )
      #   strip.fill(color)
      #   strip.show()
      #   time.sleep(0.01)
      # for i in range(LED_COUNT):
      #   downcolor = (
      #       int(red_harf[0] * (1 - i / (LED_COUNT - 1))),
      #       int(red_harf[1] * (1 - i / (LED_COUNT - 1))),
      #       int(red_harf[2] * (1 - i / (LED_COUNT - 1)))
      #   )
      #   strip.fill(downcolor)
      #   strip.show()
      #   time.sleep(0.01)
               
   def laser(self):
      count = 0
      for i in range(LED_COUNT):
         strip[i] = ((255,0,0))
         strip.show()
         strip[i] = ((0,0,0))
         strip.show()
         count -= 1
         time.sleep(0.05)
         strip[i] = ((255,0,0))
         strip.show()
         strip[i] = ((0,0,0))
         strip.show()

            
# Function to make an alternating series of lights
def merrychristmas():
    for i in range(LED_COUNT):
        if flip == 0:
          strip[i] = red
          flip = 1
        else:
          strip[i] = green
          Flip.flip = 0
    strip.show()


# def loop():
#    strip.fill((0,0,0)) #LEDオフ
#    while True:
#       Gra_led.rgb(flip)
#       if KeyboardInterrupt:
#          strip.fill((0,0,0))

# loop()

flag = 0
strip.fill((0,0,0))  #消灯

while True:
    button.wait_for_press()
    button.wait_for_release()
    value = flag
    
    if value == 0:
      # strip.fill((255,255,255))
      # strip.show()
      strip.fill((0,0,0))
      strip.show()
      # time.sleep(0.1)
      flag = 1

    if value == 1:
      # strip.fill((255,0,144)) ピンク
      Gra_led.harf(flip)
      # while True:
      #    strip.fill((255,255,255))
      #    strip.show()
      #    time.sleep(0.01)
      #    strip.fill((0,0,0))
      #    strip.show()
      #    time.sleep(0.01)
      
      
      # strip.show()
      flag = 0