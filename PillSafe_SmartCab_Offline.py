#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:49:08 2021

@author: pi
"""

import RPi.GPIO as GPIO
import time
from hx711 import HX711

# Determine if it's time to take medication
medication_taken = False

# Pin definitons
power_indicator_pin = 4
door_pin = 5
reminder_pin = 6

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_indicator_pin,GPIO.OUT)
GPIO.setup(door_pin,GPIO.IN)
GPIO.setup(reminder_pin,GPIO.OUT)

# Setup for the HX711



# Program
print("PillSafe Cab Program Running")
try:
    while 1:
        
        # Indicator light for power
        GPIO.output(power_indicator_pin,GPIO.HIGH)
        
        # Reminder light for medication
        if medication_taken == False:
            GPIO.output(reminder_pin,GPIO.HIGH)
        if medication_taken == True:
            GPIO.output(reminder_pin,GPIO.LOW)
        
        # Checks to see if door is open
        if GPIO.input(door_pin) == True:
            print("Door is opened")
            medication_taken = True
            time.sleep(1)

# Exit code
except KeyboardInterrupt:
    GPIO.cleanup()
