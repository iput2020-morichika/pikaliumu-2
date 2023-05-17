import time
from gpiozero import Button
import board
import neopixel
# import subprocess

button = Button(21)

# LED strip configuration:
LED_COUNT   = 144      # Number of LED pixels.
LED_PIN     = board.D18      # GPIO pin
LED_BRIGHTNESS = 0.5  # LED brightness
LED_ORDER = neopixel.GRB # order of LED colours. May also be GRB, GRBW, or RGBW

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = LED_BRIGHTNESS, auto_write=False, pixel_order = LED_ORDER)
# Setting variables for a specific sequence
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
flip = 0

#flag追加
flag = 0

#---------------
#コマンド実行関数
#---------------
# def runcmd():
#   try:
#     cmd = "sudo"
#     runcmd = subprocess.run("sudo /bin/python3 /home/pi/solution_development/led.py")
#     return runcmd
#   except:
#     return None  
# runcmd()
# Function to make an alternating series of lights
def merrychristmas():
    global flip
    for i in range(LED_COUNT):
        if flip == 0:
          strip[i] = red
          flip = 1
        else:
          strip[i] = green
          flip = 0
    strip.show()


# merrychristmas()

while True:
    button.wait_for_press()
    button.wait_for_release()
    #　ここから変更（音声認識なし）
    value = flag
    
    if value == 0:
      strip.fill((0,0,0))
      strip.show()
      flag = 1

    if value == 1:
      merrychristmas()
      flag = 0