import leds
import time

for i in range(0,1000000):
  for j in range(0,25):
    if (i % 25 == j):
      leds.rgb(2,1,0)
    elif ((i + 1) % 25 == j):
      leds.rgb(5,3,0)
    elif ((i + 2) % 25 == j):
      leds.rgb(10,5,0)
    elif ((i + 3) % 25 == j):
      leds.rgb(20,10,0)
    elif ((i + 5) % 25 == j):
      leds.rgb(0,2,0)
    elif ((i + 6) % 25 == j):
      leds.rgb(0,5,0)
    elif ((i + 7) % 25 == j):
      leds.rgb(0,10,0)
    elif ((i + 8) % 25 == j):
      leds.rgb(0,20,0)
    elif ((i + 10) % 25 == j):
      leds.rgb(2,0,2)
    elif ((i + 11) % 25 == j):
      leds.rgb(5,0,5)
    elif ((i + 12) % 25 == j):
      leds.rgb(10,0,10)
    elif ((i + 13) % 25 == j):
      leds.rgb(20,0,20)
    else:
      leds.rgb(0,0,0)
  time.sleep(0.08)
