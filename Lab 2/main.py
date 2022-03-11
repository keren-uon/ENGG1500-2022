from time import sleep
from machine import Pin
from motor import Motor

print("Hello world")

line_sensor = Pin(26, Pin.IN)

while True:
	print(line_sensor.value())