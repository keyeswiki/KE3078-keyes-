//**********************************************************************************
/*  
 * 名称   : Smoke_Control_LED
 * 功能   : 烟雾或可燃性气体控制LED
 * 作者   : http://www.keyes-robot.com/ 
*/
byte item = 0;

void setup() {
  Serial.begin(115200); //设置串口波特率为115200
  pinMode(16, INPUT);  //模拟气体(MQ-2)传感器连接GPIO16上，并设置为输入模式
  pinMode(18, OUTPUT);  //将LED连接到GPIO18上，并设置为输出模式
}

void loop() {
  item = digitalRead(16);  //读取模拟气体(MQ-2)传感器输出的数字信号
  Serial.println(item);  //串口打印模拟气体(MQ-2)传感器输出的数字信号
  if (item == 0) {  //检测到烟雾或可燃性气体
    digitalWrite(18, HIGH);  //打开LED
    delay(500);  //延迟 500ms
    digitalWrite(18, LOW);  //关闭LED
    delay(500);  //延迟 500ms
  } else {  //未检测到烟雾或可燃性气体
    digitalWrite(18, LOW);  //关闭LED
  }
}
//**********************************************************************************