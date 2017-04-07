from ev3dev.ev3 import ColorSensor, LargeMotor, TouchSensor
from utils.color import Color

STEERING_POWER = 700
NON_STEERING_POWER = 150
TURNING_POWER = 600
DEFAULT_POWER = 250

TURNING_MILLISECONDS = 350

class Robot(object):
    def __init__(self):
        self.left_color_sensor = ColorSensor('in4')
        self.right_color_sensor = ColorSensor('in1')
        self.left_large_motor = LargeMotor('outD')
        self.right_large_motor = LargeMotor('outA')
        self.touch_sensor = TouchSensor('in3')
        self.listeners = []
        self.prev_is_pressed = False

    def move_forward(self):
        self.left_large_motor.run_forever(speed_sp=DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=DEFAULT_POWER)

    def move_backward(self):
        self.left_large_motor.run_forever(speed_sp=-DEFAULT_POWER)
        self.right_large_motor.run_forever(speed_sp=-DEFAULT_POWER)

    def steer_left(self):
        self.left_large_motor.run_forever(speed_sp=NON_STEERING_POWER)
        self.right_large_motor.run_forever(speed_sp=STEERING_POWER)

    def steer_right(self):
        self.left_large_motor.run_forever(speed_sp=STEERING_POWER)
        self.right_large_motor.run_forever(speed_sp=NON_STEERING_POWER)

    def turn_left(self):
        self.stop()
        self.left_large_motor.run_timed(speed_sp=-TURNING_POWER, time_sp=TURNING_MILLISECONDS)
        self.right_large_motor.run_timed(speed_sp=TURNING_POWER, time_sp=TURNING_MILLISECONDS)

        # Block any calls to the motor while the robot is turning
        self.left_large_motor.wait_while('running')
        self.right_large_motor.wait_while('running')

    def turn_right(self):
        self.stop()
        self.left_large_motor.run_timed(speed_sp=TURNING_POWER, time_sp=TURNING_MILLISECONDS)
        self.right_large_motor.run_timed(speed_sp=-TURNING_POWER, time_sp=TURNING_MILLISECONDS)

        # Block any calls to the motor while the robot is turning
        self.left_large_motor.wait_while('running')
        self.right_large_motor.wait_while('running')

    def stop(self):
        self.left_large_motor.stop()
        self.right_large_motor.stop()

    def step(self):
        left_color = self.left_color_sensor.color
        right_color = self.right_color_sensor.color

        if left_color == Color.INVALID or right_color == Color.INVALID:
            for listener in self.listeners:
                listener.on_invalid(self, left_color == Color.INVALID, right_color == Color.INVALID)

        if left_color == Color.BLACK or right_color == Color.BLACK:
            for listener in self.listeners:
                listener.on_black(self, left_color == Color.BLACK, right_color == Color.BLACK)

        if left_color == Color.BLUE or right_color == Color.BLUE:
            for listener in self.listeners:
                listener.on_blue(self, left_color == Color.BLUE, right_color == Color.BLUE)

        if left_color == Color.GREEN or right_color == Color.GREEN:
            for listener in self.listeners:
                listener.on_green(self, left_color == Color.GREEN, right_color == Color.GREEN)

        if left_color == Color.YELLOW or right_color == Color.YELLOW:
            for listener in self.listeners:
                listener.on_yellow(self, left_color == Color.YELLOW, right_color == Color.YELLOW)

        if left_color == Color.RED or right_color == Color.RED:
            for listener in self.listeners:
                listener.on_red(self, left_color == Color.RED, right_color == Color.RED)

        if left_color == Color.WHITE or right_color == Color.WHITE:
            for listener in self.listeners:
                listener.on_white(self, left_color == Color.WHITE, right_color == Color.WHITE)

        if left_color == Color.BROWN or right_color == Color.BROWN:
            for listener in self.listeners:
                listener.on_brown(self, left_color == Color.BROWN, right_color == Color.BROWN)

        if self.prev_is_pressed and not self.touch_sensor.is_pressed:
            for listener in self.listeners:
                listener.on_click(self)

        self.prev_is_pressed = self.touch_sensor.is_pressed

    def add_listener(self, listener: 'RobotListener'):
        self.listeners.append(listener)

class RobotListener(object):
    def on_invalid(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_black(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_blue(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_green(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_yellow(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_red(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_white(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_brown(self, robot: 'Robot', left: bool, right: bool):
        pass

    def on_click(self, robot: 'Robot'):
        pass
