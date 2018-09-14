#! /usr/bin/env python

# Version: 2.0

import RPi.GPIO as GPIO
import threading
import time

GPIO_LED_PINS = [2, 3]

LED_OFF = 0
LED_ON = 1

def set_led_at_pin(led_pin, value):
    GPIO.output(led_pin, value)

def set_led_at_index(led_index, value):
    set_led_at_pin(GPIO_LED_PINS[led_index], value)

def setup():
    # setup the GPIO for the LED
    GPIO.setmode(GPIO.BCM)
    for led_pin in GPIO_LED_PINS:
        GPIO.setup(led_pin, GPIO.OUT)
        # Initially turn off the LED
        set_led_at_pin(led_pin, LED_OFF)

def blink_lights():
    while True:
        set_led_at_index(0, LED_ON)
        set_led_at_index(1, LED_ON)
        time.sleep(1)
        set_led_at_index(0, LED_OFF)
        set_led_at_index(1, LED_OFF)
        time.sleep(1)

def run():
    setup()
    t = threading.Thread(target=blink_lights)
    t.daemon = True
    t.start()

    # wait until the user enters something
    user_input = raw_input("Press enter to exit program")
    # release any GPIO resources
    GPIO.cleanup()

if __name__ == '__main__':
    run()
