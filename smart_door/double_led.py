# # import RPi.GPIO as GPIO
# import time
# class Double_LED_Class:
#     def __init__(self):  # double_led 初始化工作
#         makerobo_pins = (11, 12)  # PIN管脚字典
#         GPIO.setmode(GPIO.BOARD)  # 采用实际的物理管脚给GPIO口
#         GPIO.setwarnings(False)  # 去除GPIO口警告
#         GPIO.setup(makerobo_pins, GPIO.OUT)  # 设置Pin模式为输出模式
#         GPIO.output(makerobo_pins, GPIO.LOW)  # 设置Pin管脚为低电平(0V)关闭LED
#         self.p_R = GPIO.PWM(makerobo_pins[0], 2000)  # 设置频率为2KHz
#         self.p_G = GPIO.PWM(makerobo_pins[1], 2000)  # 设置频率为2KHz
#         # 初始化占空比为0(led关闭)
#         self.p_R.start(0)
#         self.p_G.start(0)
#     def makerobo_pwm_map(self,x, in_min, in_max, out_min, out_max):
#         return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
#     def makerobo_set_red_Color(self,col):  # 例如:col = 0x1122
#         # 把0-255的范围同比例缩小到0-100之间
#         R_val = self.makerobo_pwm_map(col, 0, 255, 0, 100)
#         self.p_R.ChangeDutyCycle(R_val)  # 改变占空比
#     def makerobo_set_green_Color(self,col):  # 例如:col = 0x1122
#         # 把0-255的范围同比例缩小到0-100之间
#         G_val = self.makerobo_pwm_map(col, 0, 255, 0, 100)
#         self.p_G.ChangeDutyCycle(G_val)  # 改变占空比
#     # 释放资源
#     def makerobo_destroy(self):
#         self.p_G.stop()
#         self.p_R.stop()
#         GPIO.output(self.makerobo_pins, GPIO.LOW)  # 关闭所有LED
#         GPIO.cleanup()  # 释放资源
# '''
# # 测试用例
# if __name__ == "__main__":
#     Hardware_double_led=Double_LED_Class()
#     Hardware_double_led.makerobo_set_red_Color(200)
#     time.sleep(3)#显示红灯3s后显示绿灯
#     Hardware_double_led.makerobo_set_red_Color(0)
#     Hardware_double_led.makerobo_set_green_Color(200)
# '''