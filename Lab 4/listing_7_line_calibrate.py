# Distances from the centroid of the robot to the centre of each sensor in mm
x0 = -15
x1 = 0
x2 = 15

# Initialise pins for analog line sensors
adc_A0 = ADC(Pin(26))
adc_A1 = ADC(Pin(27))
adc_A2 = ADC(Pin(28))

while True:
  #   TODO: Take sensor measurements using "w0 = adc_A0.read()"
  #         storing sensor data in w0, w1, w2,
  #   TODO: Calculate numerator of weighted average
  numerator = ???
  #   TODO: Calculate denominator of weighted average
  denominator = ???

  line_dist = numerator/denominator

  print("Distance from line = {:3.2f}".format(line_dist))
  sleep(0.1)  #   50ms delay