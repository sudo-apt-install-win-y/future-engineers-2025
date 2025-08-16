#!/usr/bin/env python3
"""
Robot Button Watcher with LED feedback
- Button on GPIO 9
- LED on GPIO 10: flashes for short-press routines, solid for long-press routines
"""
import time
import subprocess
from gpiozero import Button, LED

# --- Configuration ---------------------------------------------------------
BUTTON_PIN   = 9       # BCM pin for push-button
LED_PIN      = 10      # BCM pin for LED
SHORT_PRESS  = 1.0     # seconds threshold for short vs long press

# Map press type to your scripts
SCRIPTS = {
    'short': '~/WRO2025-FE-sudoaptinstallwin-y/software/round1/round1.py',
    'long':  '~/WRO2025-FE-sudoaptinstallwin-y/software/round2/round2.py'
}

# --- Setup -----------------------------------------------------------------
button = Button(BUTTON_PIN, pull_up=True, bounce_time=0.05)
led    = LED(LED_PIN)

# --- Helper ----------------------------------------------------------------
def run_script(path):
    """Launch a separate Python process so main loop isn’t blocked."""
    subprocess.Popen(['python3', path])
    print(f"→ Launched {path}")

# --- Main loop -------------------------------------------------------------
print("Waiting for button press...")

while True:
    button.wait_for_press()
    t0 = time.time()
    button.wait_for_release()
    held = time.time() - t0

    if held < SHORT_PRESS:
        # Flash LED 3 times for short-press feedback
        for x in range(3):
            led.on()
            time.sleep(0.2)
            led.off()
        run_script(SCRIPTS['short'])

    else:
        # Solid LED for long-press feedback
        led.on()
        run_script(SCRIPTS['long'])

    # Return LED to off after a brief pause (customize as needed)
    time.sleep(0.5)
    led.off()