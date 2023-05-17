"""
ファイルインポート
"""
from sensor import suion
from led import led_class

"""
初期化処理
"""
led_class

s1 = suion.temp_c
print (s1)

if s1 > 26.0:
  led_class.loop()
  