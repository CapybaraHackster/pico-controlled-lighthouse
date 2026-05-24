# Wiring

| Part | Pico pin | Other  |
| --- | --- | --- |
| NeoPixel data | GP1 | VSYS for power, ground as pin 38 |
| Button input | GP3 |  ground as pin 3  |
| Button other side | GND |    |

The button uses `Pin.PULL_UP` in the code. Connect one side of the button to GP3 and the other side to GND.

Make sure the LED power wiring matches the LED strip or ring you use. For larger LED counts or high brightness, use an appropriate external power supply and common ground.
