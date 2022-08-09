let Display = grove.createDisplay(DigitalPin.P1, DigitalPin.P15)
basic.forever(function () {
    Display.show(grove.measureInCentimeters(DigitalPin.P0))
    basic.pause(1000)
})
