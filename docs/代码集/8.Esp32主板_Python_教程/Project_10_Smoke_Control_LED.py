# 导入 Pin 和 time 库.
from machine import Pin
import time

# 定义模拟气体(MQ-2)传感器和led的引脚. 
sensor_smoke = Pin(15, Pin.IN)
led = Pin(2, Pin.OUT)
  
while True: 
      value = sensor_smoke.value()
      if value == 0:
          print("ALARM! smoke or flammable gas detected!") 
          led.value(1)
          time.sleep(0.5)
          led.value(0)
          time.sleep(0.5)         
      else:
          led.value(0)