from time import sleep
from machine import Pin
from motor import Motor

print("Hello world") # on startup

line_sensor = Pin(26, Pin.IN)

while True:
	motor_left.set_forwards()  # Set the left motor to run forwards
	motor_right.set_forwards()  # Set the right motor to run forwards
	sensor_value = line_sensor.value()  # Reads 1 if no obstacle is present
	# ...otherwise 0
	# Let’s say our desired duty cycles are 100% and 70%
	# Multiply the previous ‘1’ or ‘0’ by the desired duty (* is multiply)
	motor_left.duty(sensor_value * 100)  # circle
	motor_right.duty(sensor_value * 70)  # circle

