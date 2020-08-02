# MagicBand Mickey Ears
# ---------------------
#
# For Gemma M0 : https://www.adafruit.com/product/3501?gclid=Cj0KCQjwpZT5BRCdARIsAGEX0zl4OEKc4IAJXweQIeZnpAiHyY5jYQUWC_LiUFC0w9iMBu3qW6IjqlUaAp9-EALw_wcB
# YouTube Build Video:
#
# Code is loosely based on our previous MagicBand reader code

# Contact us with any questions:
# foolishmortalbuilders@gmail.com 
#
#
from digitalio import *
from board import *
import neopixel
import time
import random
 
pixpin = D1
led = DigitalInOut(D13)
led.direction = Direction.OUTPUT

right_ring=24
right_center=12
left_ring=24
left_center=12
numpix= right_ring + right_center + left_ring + left_center

right_start=0
left_start = right_ring + right_center  
strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.3, auto_write=False)

COLORS = {
    "green" : (0,255,0),
    "canaryyellow" : (255,237,0),
    "red": (255,0,0),
    "blue" : (0,0,255),
    "lightblue" : (153,204,255),
    "white" : (255,255,255),
    "stitch" : (0,39,144)
} 


def cycle(color,wait):
    cursor=3
    for i in range(right_ring):
        if (i >= cursor):
            right = i - 3
            left  = left_start + i - 3
            strip[left] = (0,0,0)
            strip[right] = (0,0,0)
        left = i + left_start
        strip[i] = color 
        strip[left] = color 
        strip.show()
        time.sleep(wait)
    strip[i-2] = (0,0,0)
    strip[i-1] = (0,0,0)
    strip[i] = (0,0,0)
    strip[left_start + (i-2)] = (0,0,0)
    strip[left_start + (i-1)] = (0,0,0)
    strip[left_start+ i] = (0,0,0)
    strip.show()

def figure_eight(color, wait):
    x = int(right_ring * .75)
    x = x + 1
    y = int(right_ring * .25)
    z =  y + 1
    w =  x + 1
 
    # draw to X on right
    for i in range(x):
        if (i>=1) :
            strip[i - 1] = (0,0,0)
        strip[i] = color
        strip.show()
        time.sleep(wait) 
    strip[x-1] = (0,0,0)
    strip[x] = (0,0,0) 
    strip.show()
    # draw from y to y backwards on left
    for i in range(y):
        p = (left_start + y) -i 
        strip[p] = color
        if (i >= 1):
            strip[p + 1] = (0,0,0)
        strip.show()
        time.sleep(wait)
    strip[left_start + 1] = (0,0,0)
    strip.show()
    # draw all the way to y backwards on left
    for i in reversed(range(right_ring)):
        if (i < y):
            break
        strip[left_start + i] = color
        strip[left_start + i + 1] = (0,0,0)
        strip.show()
        time.sleep(wait)
    strip[left_start + y] = (0,0,0)
    strip.show()

    # draw from x to size on right
    for i in range (x, right_ring):
        strip[i - 1] = (0,0,0)
        strip[i] = color
        strip.show()
        time.sleep(wait) 
    strip[23] = (0,0,0)
    strip.show()
    time.sleep(wait) 

def all_on(color):
   strip.fill(color)
   strip.show()
   time.sleep(1)
   
def sparkle_random(times,color,start,size):
   for i in range(times):
       r = random.randint(start,size)
       strip[r] = (255,255,255)
       strip.show()
       time.sleep(.001)
       strip[r] = color 
       strip.show()
       time.sleep(.001)

def seq(color1, color2):
    cycle(color1,0.001)
    cycle(color1,0.0001)
    cycle(color1,0.00001)
    all_on(color1)
    sparkle_random(900,color2, 0, numpix -1 )
    all_on((0,0,0))

while True:
    seq(COLORS['green'], COLORS['green']);
    figure_eight(COLORS['canaryyellow'], 0.001)
    figure_eight(COLORS['stitch'], 0.001)
    figure_eight(COLORS['blue'], 0.001)
    seq(COLORS['green'], COLORS['green']);
    seq(COLORS['green'], COLORS['stitch']);
    seq(COLORS['blue'], COLORS['red']);
    seq(COLORS['red'], COLORS['canaryyellow']);


