from machine import Pin, PWM, Timer
from utime import sleep, ticks_us, ticks_diff

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
    


# SETUP

led = PWM(Pin(15), freq = 1000)
      
            
print("Program Started")
# LOOP
while True:
    try:
        TimedUpRamp(2, 65535)
        TimedDownRamp(1, 65535)
    except KeyboardInterrupt:
        print("Program Stopped")
        led.duty_u16(0)
        break
    
       
#Functions

