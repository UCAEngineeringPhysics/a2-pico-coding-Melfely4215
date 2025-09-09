from machine import Pin, PWM, Timer
from utime import sleep, ticks_us, ticks_diff

# Functions
def TimedUpRamp(seconds, peak):
    StartTimer()
    for i in range(0, 1000):
        led.duty_u16( int( i * (peak / 1000)))
        sleep(0.001 * seconds)
    print(f"Ramp Up: {EndTimer()}")
         
def TimedDownRamp(seconds, peak):
    StartTimer()
    for i in range(1000, 0, -1):
        led.duty_u16( int( i * (peak / 1000)))
        sleep(0.001 * seconds)
    print(f"Ramp Down: {EndTimer()}")

def StartTimer():
    global _timer
    _timer = ticks_us()
def EndTimer():
    Time = ticks_diff(ticks_us(), _timer)
    return Time / 1000000


Mode = "Fade"
def SwapMode(dummy):
    print("Button Pressed")
    global Mode
    if (Mode == "On"):
        Mode = "Fade"
    elif (Mode == "Fade"):
        Mode = "On"
            
# SETUP

led = PWM(Pin(15), freq = 1000)
button = Pin(13, Pin.IN, Pin.PULL_DOWN)

button.irq(trigger=Pin.IRQ_FALLING, handler=SwapMode)

print("Program Started")


# LOOP
while True:
    try:
        if (Mode == "On"):
            print("Hold On")
            led.freq(1000)
            led.duty_u16(65535)
            sleep(1) #Reduce log spam            
        elif (Mode == "Fade"):
            print("Fade Mode")
            led.freq(1000)
            TimedDownRamp(2, 65535)
            TimedUpRamp(2, 65535)
            
        sleep(.001)
    except KeyboardInterrupt:
        print("Program Stopped")
        led.duty_u16(0)
        break