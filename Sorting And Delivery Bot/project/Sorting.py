from utils.brick import BP, Motor, EV3ColorSensor, configure_ports
import time

def turn_motor_out(motor):
    motor.set_position_relative(-80)
    motor.wait_is_moving()
    
def turn_motor_in(motor):
    motor.set_position_relative(80)
    motor.wait_is_moving()

def conv_motor(delay):
    motor.set_position_relative(delay)
    motor.wait_is_moving()


DELAY_KICK = 350
DELAY_KICK2 = 400
DELAY_KICK3 = 450
MAX_DELAY=1000

POWER_LIMIT = 80
SPEED = 300



KICK_MOTOR = Motor('A')
KICK_MOTOR2 = Motor('B')
KICK_MOTOR3 = Motor('C')
CONV_MOTOR = Motor('D')

KICK_MOTOR.reset_encoder()
KICK_MOTOR2.reset_encoder()
KICK_MOTOR3.reset_encoder()
CONV_MOTOR.reset_encoder()

KICK_MOTOR.set_limits(POWER_LIMIT,SPEED)
KICK_MOTOR2.set_limits(POWER_LIMIT,SPEED)
KICK_MOTOR3.set_limits(POWER_LIMIT,SPEED)
CONV_MOTOR.set_limits(POWER_LIMIT,SPEED)

KICK_MOTOR.set_dps(SPEED)
KICK_MOTOR2.set_dps(SPEED)
KICK_MOTOR3.set_dps(SPEED)
CONV_MOTOR.set_dps(400)

KICK_MOTOR.set_position(0)
KICK_MOTOR2.set_position(0)
KICK_MOTOR3.set_position(0)
CONV_MOTOR.set_position(0)

COLOR_SENSOR = configure_ports(PORT_3=EV3ColorSensor)

try:
    while True:
        colors = COLOR_SENSOR.get_color_name()
        print(colors)
        if(str(colors) == "Red"):
            time.sleep(2)
            CONV_MOTOR.set_position_relative(70)
            time.sleep(1)
            turn_motor_out(KICK_MOTOR2)
            time.sleep(0.5)
            turn_motor_in(KICK_MOTOR2)
            time.sleep(0.5)
        elif (str(colors) == "Blue"):
            time.sleep(2)
            CONV_MOTOR.set_position_relative(320)
            time.sleep(1.5)
            turn_motor_out(KICK_MOTOR3)
            time.sleep(0.5)
            turn_motor_in(KICK_MOTOR3)
            time.sleep(0.5)
        elif (str(colors) == "Green"):
            time.sleep(2)
            CONV_MOTOR.set_position_relative(560)
            time.sleep(2)
            turn_motor_out(KICK_MOTOR)
            time.sleep(0.5)
            turn_motor_in(KICK_MOTOR)
            time.sleep(0.5)

except:
    BP.reset_all()




