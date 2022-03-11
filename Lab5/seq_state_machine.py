from machine import Pin
from time    import sleep
from motor   import Motor
from ultrasonic import sonic

# TODO: Ensure these are the pin numbers used on your robot
ECHO  = 2
TRIG  = 3
LINE1 = "INTENTIONALLY_UNDEFINED_PIN_ERROR" # TODO: Insert line sensor pin
# Initialise the motors
motor_left  = Motor("left", 8, 9, 6)
motor_right = Motor("right", 10, 11, 7)
# Initialise the ultrasonic sensor
ultrasonic_sensor = sonic(ECHO, TRIG)
# Initialise a line sensor
line_sensor_1 = Pin(LINE1, Pin.IN)

# Declare variables that need to retain value in loop
pwm_left  = 0
pwm_right = 0
dir_left  = 0
dir_right = 0

# Declare states
state_list = ['DRIVING', 'FOLLOW_WALL', 'STOPPED']

state = 'DRIVING'   # Default state on init is DRIVING

while True:
    # Collect sensor data
    sonar_dist = ultrasonic_sensor.distance_mm()
    # TODO: Read value from line sensor
    #(Use analog or binary value, your decision as a team)
    line_measurement_1 = ???

    # TODO: State machine here
    if state == 'DRIVING':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values
        dir_left  = #??? either fwd or bwd
        dir_right = #???
        pwm_left  = #??? [0, 100]
        pwm_right = #???
        # Transition condition
        if ():  # TODO: Condition based on measurement here
            state = 'FOLLOW_WALL'
        else:
            state = state  # Remain in current state if condition not met

    elif state == 'FOLLOW_WALL':
        print(state)         # Update to OLED
        # Actions
        # TODO: Drive by setting direction and PWM values according to distance

        # Transition condition
        if ():  # TODO: Condition based on measurement here
            state = 'STOPPED'
        else:
            state = state  # Remain in current state if condition not met

    elif state == 'STOPPED':
        print(state)         # Update to OLED
        # Actions
        # TODO: Stop driving by setting PWM values
        dir_left  = 'back' # Trollolol
        dir_right = 'back' # Trollolol
        pwm_left  = 70     # Trollolol
        pwm_right = 70     # Trollolol
        # No transition condition, remain in a safe state.

    else:
        print('Incorrect state selected!') # Update to OLED

    # Finally, send control signals to motors
    if dir_left == 'fwd':
        motor_left.set_forwards()
    else:
        motor_left.set_backwards()
    if dir_right == 'fwd':
        motor_right.set_forwards()
    else:
        motor_right.set_backwards()

    motor_left.duty(pwm_left)
    motor_right.duty(pwm_right)

    time.sleep(0.02)