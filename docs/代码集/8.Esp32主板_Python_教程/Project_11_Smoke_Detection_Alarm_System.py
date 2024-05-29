# 导入 Pin 和 time 库. 
from machine import Pin
import time

# 定义模拟气体(MQ-2)传感器，led和有源蜂鸣器的引脚. 
sensor_smoke = Pin(15, Pin.IN)
led = Pin(2, Pin.OUT)
buzzer = Pin(0, Pin.OUT)
 
while True: 
      value = sensor_smoke.value()
      if value == 0:
          print("ALARM! smoke or flammable gas detected!")
          buzzer.value(1)
          led.value(1)
          time.sleep(0.5)
          buzzer.value(0)
          led.value(0)
          time.sleep(0.5)         
      else:
          buzzer.value(0)
          led.value(0)