from machine import Pin
import neopixel
import time

# =========================
# HARDWARE SETUP
# =========================
LED_PIN = 1
BUTTON_PIN = 3
NUM_LEDS = 6

button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)
strip = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)

# =========================
# USER-EDITABLE COLORS
# =========================
WARM_YELLOW = (255, 180, 50)
NIGHT_RED = (255, 0, 0)
MARINE_BLUE = (53, 148, 107)
DEEP_GREEN = (0, 255, 0)
BRIGTH_LIGTH = (255, 255, 200)

COLOR_MODE_1 = BRIGTH_LIGTH
COLOR_MODE_2 = WARM_YELLOW
COLOR_MODE_3 = NIGHT_RED
COLOR_MODE_4 = WARM_YELLOW
COLOR_MODE_5 = WARM_YELLOW
COLOR_MODE_6 = WARM_YELLOW
COLOR_MODE_7 = WARM_YELLOW
COLOR_MODE_8 = NIGHT_RED
COLOR_MODE_9 = MARINE_BLUE
COLOR_MODE_10 = DEEP_GREEN

# Brightness levels
BRIGHTNESS_MODE_1 = 1.0
BRIGHTNESS_MODE_2 = 0.35
BRIGHTNESS_MODE_3 = 0.10

# =========================
# STATE
# =========================
mode = 1

last_button_state = 1
last_button_time = 0
debounce_ms = 250

mode_timer = time.ticks_ms()
mode_phase = 0

# =========================
# HELPER FUNCTIONS
# =========================
def apply_brightness(color, brightness):
    r = int(color[0] * brightness)
    g = int(color[1] * brightness)
    b = int(color[2] * brightness)
    return (r, g, b)

def fill_all(color):
    for i in range(NUM_LEDS):
        strip[i] = color
    strip.write()

def leds_off():
    fill_all((0, 0, 0))

def reset_mode_state():
    global mode_timer, mode_phase
    mode_timer = time.ticks_ms()
    mode_phase = 0
    leds_off()

def check_button():
    global mode, last_button_state, last_button_time

    current_state = button.value()

    # Button press detected: HIGH -> LOW
    if last_button_state == 1 and current_state == 0:
        now = time.ticks_ms()

        if time.ticks_diff(now, last_button_time) > debounce_ms:
            mode += 1

            if mode > 11:
                mode = 1

            last_button_time = now
            reset_mode_state()
            print("Mode:", mode)

    last_button_state = current_state

# =========================
# MODE FUNCTIONS
# =========================
def run_mode_1():
    # Bright steady on
    fill_all(apply_brightness(COLOR_MODE_1, BRIGHTNESS_MODE_1))

def run_mode_2():
    # Bright steady on
    fill_all(apply_brightness(COLOR_MODE_2, BRIGHTNESS_MODE_1))

def run_mode_3():
    # Bright steady on
    fill_all(apply_brightness(COLOR_MODE_3, BRIGHTNESS_MODE_1))

def run_mode_4():
    # Dimmer steady on
    fill_all(apply_brightness(COLOR_MODE_4, BRIGHTNESS_MODE_2))

def run_mode_5():
    # Even more dimmer steady on
    fill_all(apply_brightness(COLOR_MODE_5, BRIGHTNESS_MODE_3))

def run_mode_6():
    """
    Fade in, stay on 3 sec,
    fade out, stay off 2 sec,
    repeat.
    """
    global mode_timer, mode_phase

    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, mode_timer)

    fade_time = 1000
    on_time = 3000
    off_time = 2000

    if mode_phase == 0:
        # Fade in
        if elapsed <= fade_time:
            brightness = elapsed / fade_time
            fill_all(apply_brightness(COLOR_MODE_6, brightness))
        else:
            fill_all(COLOR_MODE_6)
            mode_phase = 1
            mode_timer = now

    elif mode_phase == 1:
        # Stay on
        fill_all(COLOR_MODE_6)
        if elapsed >= on_time:
            mode_phase = 2
            mode_timer = now

    elif mode_phase == 2:
        # Fade out
        if elapsed <= fade_time:
            brightness = 1.0 - (elapsed / fade_time)
            fill_all(apply_brightness(COLOR_MODE_6, brightness))
        else:
            leds_off()
            mode_phase = 3
            mode_timer = now

    elif mode_phase == 3:
        # Stay off
        leds_off()
        if elapsed >= off_time:
            mode_phase = 0
            mode_timer = now

def run_mode_7():
    """
    No fade:
    on 3 sec, off 3 sec,
    repeat.
    """
    global mode_timer, mode_phase

    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, mode_timer)

    on_time = 3000
    off_time = 3000

    if mode_phase == 0:
        fill_all(COLOR_MODE_7)
        if elapsed >= on_time:
            mode_phase = 1
            mode_timer = now

    elif mode_phase == 1:
        leds_off()
        if elapsed >= off_time:
            mode_phase = 0
            mode_timer = now

def run_mode_8():
    """
    Fade in 2 sec,
    stay peak 1 sec,
    fade out 1 sec,
    stay off 1 sec,
    repeat.
    """
    global mode_timer, mode_phase

    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, mode_timer)

    fade_in_time = 2000
    peak_time = 1000
    fade_out_time = 1000
    off_time = 1000

    if mode_phase == 0:
        # Fade in over 2 seconds
        if elapsed <= fade_in_time:
            brightness = elapsed / fade_in_time
            fill_all(apply_brightness(COLOR_MODE_8, brightness))
        else:
            fill_all(COLOR_MODE_8)
            mode_phase = 1
            mode_timer = now

    elif mode_phase == 1:
        # Stay at peak brightness
        fill_all(COLOR_MODE_8)
        if elapsed >= peak_time:
            mode_phase = 2
            mode_timer = now

    elif mode_phase == 2:
        # Fade out over 1 second
        if elapsed <= fade_out_time:
            brightness = 1.0 - (elapsed / fade_out_time)
            fill_all(apply_brightness(COLOR_MODE_8, brightness))
        else:
            leds_off()
            mode_phase = 3
            mode_timer = now

    elif mode_phase == 3:
        # Stay off
        leds_off()
        if elapsed >= off_time:
            mode_phase = 0
            mode_timer = now

def run_mode_9():
    """
    Fade in 2 sec,
    stay peak 1 sec,
    fade out 1 sec,
    stay off 1 sec,
    repeat.
    """
    global mode_timer, mode_phase

    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, mode_timer)

    fade_in_time = 2000
    peak_time = 1000
    fade_out_time = 1000
    off_time = 1000

    if mode_phase == 0:
        # Fade in over 2 seconds
        if elapsed <= fade_in_time:
            brightness = elapsed / fade_in_time
            fill_all(apply_brightness(COLOR_MODE_9, brightness))
        else:
            fill_all(COLOR_MODE_9)
            mode_phase = 1
            mode_timer = now

    elif mode_phase == 1:
        # Stay at peak brightness
        fill_all(COLOR_MODE_9)
        if elapsed >= peak_time:
            mode_phase = 2
            mode_timer = now

    elif mode_phase == 2:
        # Fade out over 1 second
        if elapsed <= fade_out_time:
            brightness = 1.0 - (elapsed / fade_out_time)
            fill_all(apply_brightness(COLOR_MODE_9, brightness))
        else:
            leds_off()
            mode_phase = 3
            mode_timer = now

    elif mode_phase == 3:
        # Stay off
        leds_off()
        if elapsed >= off_time:
            mode_phase = 0
            mode_timer = now

def run_mode_10():
    """
    Fade in 2 sec,
    stay peak 1 sec,
    fade out 1 sec,
    stay off 1 sec,
    repeat.
    """
    global mode_timer, mode_phase

    now = time.ticks_ms()
    elapsed = time.ticks_diff(now, mode_timer)

    fade_in_time = 2000
    peak_time = 1000
    fade_out_time = 1000
    off_time = 1000

    if mode_phase == 0:
        # Fade in over 2 seconds
        if elapsed <= fade_in_time:
            brightness = elapsed / fade_in_time
            fill_all(apply_brightness(COLOR_MODE_10, brightness))
        else:
            fill_all(COLOR_MODE_10)
            mode_phase = 1
            mode_timer = now

    elif mode_phase == 1:
        # Stay at peak brightness
        fill_all(COLOR_MODE_10)
        if elapsed >= peak_time:
            mode_phase = 2
            mode_timer = now

    elif mode_phase == 2:
        # Fade out over 1 second
        if elapsed <= fade_out_time:
            brightness = 1.0 - (elapsed / fade_out_time)
            fill_all(apply_brightness(COLOR_MODE_10, brightness))
        else:
            leds_off()
            mode_phase = 3
            mode_timer = now

    elif mode_phase == 3:
        # Stay off
        leds_off()
        if elapsed >= off_time:
            mode_phase = 0
            mode_timer = now

def run_mode_11():
    # OFF
    leds_off()

# =========================
# STARTUP
# =========================
reset_mode_state()
print("Starting in Mode 1")

# =========================
# MAIN LOOP
# =========================
while True:
    check_button()

    if mode == 1:
        run_mode_1()
    elif mode == 2:
        run_mode_2()
    elif mode == 3:
        run_mode_3()
    elif mode == 4:
        run_mode_4()
    elif mode == 5:
        run_mode_5()
    elif mode == 6:
        run_mode_6()
    elif mode == 7:
        run_mode_7()
    elif mode == 8:
        run_mode_8()
    elif mode == 9:
        run_mode_9()
    elif mode == 10:
        run_mode_10()
    elif mode == 11:
        run_mode_11()

    time.sleep_ms(20)
