Display = grove.create_display(DigitalPin.P1, DigitalPin.P15)

def on_forever():
    Display.show(grove.measure_in_centimeters(DigitalPin.P0))
    basic.pause(1000)
basic.forever(on_forever)
