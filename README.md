# Pico Controlled Lighthouse

A Raspberry Pi Pico controlled LED lighthouse project for a 3D printed lighthouse model. The Pico drives a 6 LED NeoPixel (WS2812) strip and uses one button to cycle through different light modes.

Build video: coming soon.

## Features

- 6 NeoPixel LEDs controlled from a Raspberry Pi Pico
- One-button mode switching
- Steady light modes in bright white, warm yellow, and night red
- Dim lighthouse glow modes
- Fade and blink modes
- Marine blue and deep green pulse modes
- Final OFF mode

## Hardware

- Raspberry Pi Pico or compatible MicroPython board
- 6 LED NeoPixel / WS2812 strip or ring
- Momentary push button
- 3D printed lighthouse body
- Wires and suitable power connection for the LEDs

## Wiring

| Part | Pico pin | Other  |
| --- | --- | --- |
| NeoPixel data | GP1 | VSYS for power, ground as pin 38 |
| Button input | GP3 | ground as pin 3  |
| Button other side | GND |    |

The code uses the Pico internal pull-up resistor for the button, so the button should connect GP3 to GND when pressed.

<img width="3395" height="1915" alt="Lighthouse" src="https://github.com/user-attachments/assets/06170874-aa3e-4602-ab89-2e27793f7dfc" />

## Modes

1. Bright light, steady
2. Warm yellow, steady, bright
3. Night red, steady, bright
4. Warm yellow, dim steady
5. Warm yellow, very dim steady
6. Warm yellow, fade in / on / fade out / off
7. Warm yellow, hard on / off blink
8. Night red, fade pulse
9. Marine blue, fade pulse
10. Deep green, fade pulse
11. OFF

## Installing On The Pico

1. Install MicroPython on the Raspberry Pi Pico.
2. Open `main.py` in Thonny or another Pico-compatible editor.
3. Save the file to the Pico as `main.py`.
4. Restart the Pico.
5. Press the button to cycle through the modes.

## Project Files

- `main.py` - Pico MicroPython controller code
- `docs/` - extra build and wiring notes
- `3d-files/` - place STL/3MF files here
- `images/` - place build photos and assembly images here

## License

Code is released under the MIT License. 3D model files and images may use a separate license if noted in their folders.
