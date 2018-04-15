from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
import time

if __name__ == '__main__':
    bw = back_wheels.Back_Wheels()
    fw = front_wheels.Front_Wheels()
    bw.speed = 60
    bw.backward()
    pan_servo = Servo.Servo(1)
    pan_servo.write(0)
    try:
        while True:
            fw.turn(80)
            #pan_servo.write(1)
            time.sleep(1)
            fw.turn(90)
            #pan_servo.write(0)
            #bw.speed = motor_speed
            #bw.forward()
            time.sleep(1)
            fw.turn(100)
            time.sleep(1)
            fw.turn(90)
            time.sleep(1)
    except KeyboardInterrupt:
        fw.turn_straight()
        bw.stop()
        pan_servo.write(90)
