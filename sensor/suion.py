import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
SENSOR_ID = '28-031097942be5'   #センサー
device_folder = glob.glob(base_dir + SENSOR_ID)[0]
device_file = device_folder + '/w1_slave'

#温度データの入ったデータを取得する関数
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')    #温度データのみ取得
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


if __name__=="__main__":
    while True:
        print(read_temp())
        time.sleep(1)