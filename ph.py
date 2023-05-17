import spidev
Vref = 3.3
ch0 = [0x06,0x00,0x00]

spi = spidev.SpiDev()
spi.open(0,0) #bus 0,cs 0
spi.max_speed_hz = #100kHz 最近のRaspberry Piではこれが必要になった

adc = spi.xfer2(ch0)
data = ((adc[1] & 0x0f) << 8) | adc[2] #0x00_00(=0)から0x0fff(=4095)の値

data_v = (data * Vref) / float(4096)
print("data_v: %f V (max=%f)" % (data_v, Vref))
      
spi.close()