import wiringpi

data_pin = 8
clock_pin = 9

wiringpi.wiringPiSetup()
wiringpi.pinMode(data_pin, 1)
wiringpi.pinMode(clock_pin,1)

def rgb(red, green, blue):
  wiringpi.shiftOut(data_pin, clock_pin, 1, red)
  wiringpi.shiftOut(data_pin, clock_pin, 1, green)
  wiringpi.shiftOut(data_pin, clock_pin, 1, blue)

def set(leds):
  for led in leds:
    rgb(led[0], led[1], led[2])


def off(num):
  for i in range(0, num):
    rgb(0,0,0)


