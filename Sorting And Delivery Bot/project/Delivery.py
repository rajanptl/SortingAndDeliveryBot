from utils.brick import BP,Motor,EV3ColorSensor,configure_ports,TouchSensor, Brick 
import time

def turn_motor_3(motor):
    motor.set_position_relative(122)
    motor.wait_is_moving()
    time.sleep(0.30)
    motor.set_position_relative(-120)
    motor.wait_is_moving()
    
def turn_motor_2(motor):
    motor.set_position_relative(62)
    motor.wait_is_moving()
    time.sleep(0.30)
    motor.set_position_relative(-60)
    motor.wait_is_moving()
    
def turn_motor_1(motor):
    motor.set_position_relative(102)
    motor.wait_is_moving()
    time.sleep(0.30)
    motor.set_position_relative(-100)
    motor.wait_is_moving()


POWER_LIMIT = 80
SPEED = 600


MOTOR_RED = Motor('D')
MOTOR_BLUE = Motor('B')
MOTOR_GREEN = Motor('C')

MOTOR_RED.reset_encoder()
MOTOR_BLUE.reset_encoder()
MOTOR_GREEN.reset_encoder()

MOTOR_RED.set_limits(POWER_LIMIT,SPEED)
MOTOR_BLUE.set_limits(POWER_LIMIT,SPEED)
MOTOR_GREEN.set_limits(POWER_LIMIT,SPEED)

MOTOR_RED.set_dps(SPEED)
MOTOR_BLUE.set_dps(SPEED)
MOTOR_GREEN.set_dps(SPEED)

MOTOR_RED.set_position(0)
MOTOR_BLUE.set_position(0)
MOTOR_GREEN.set_position(0)

COLOR_SENSOR=configure_ports(PORT_1=EV3ColorSensor)


try:
    while True:
            colors = COLOR_SENSOR.get_color_name()
            print(colors)
            if (colors == "Red"):
                
                turn_motor_3(MOTOR_RED)
                time.sleep(2)
            elif (colors == "Blue"):
                
                turn_motor_2(MOTOR_BLUE)
                time.sleep(2)
            elif (colors == "Green"):
              
                turn_motor_1(MOTOR_GREEN)
                time.sleep(2)
except Exception as e:
    print(e)
    BP.reset_all()

