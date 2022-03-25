import time
import rtc
import supervisor
import board
import adafruit_dotstar as dotstar
dots = dotstar.DotStar(board.GP18, board.GP19, 72, brightness=0.1)
dotnum = len(dots)
dots.fill((0, 0, 0))
trail_len = 16
has_completed = False
def init_clock():
    clock.datetime = time.struct_time((2022, 3, 25, 0, 0, 0, 0, -1, -1))
    if not supervisor.runtime.serial_connected:
        return 0, 0, 0
    print("Enter hour: ", end='')
    h, m, s = (0, 0, 0)
    while True:
        if not supervisor.runtime.serial_bytes_available:
            time.sleep(.01)
            if clock.datetime[5] > 5:
                break       
    if supervisor.runtime.serial_bytes_available:
        h = int(input())
    print("\nEnter minute: ", end='')
    st = clock.datetime[5]
    while True:
        if not supervisor.runtime.serial_bytes_available:
            time.sleep(.01)
            if clock.datetime[5] > 5+st:
                break
    if supervisor.runtime.serial_bytes_available:
        m = int(input())
    print("\nEnter second: ", end='')
    st = clock.datetime[5]
    while True:
        if not supervisor.runtime.serial_bytes_available:
            time.sleep(.01)
            if clock.datetime[5] > 5+st:
                break
    if supervisor.runtime.serial_bytes_available:
        s = int(input())
    return h, m, s

hourdotstart = 0
minutedotstart = 8
seconddotstart = 16
clock = rtc.RTC()
h, m, s = init_clock()
clock.datetime = time.struct_time((2022, 3, 25, h, m, s, 0, -1, -1))
dots[7] = (255, 0, 0)
dots[15] = (255, 0, 0)

while True:
    time.sleep(.1)
    h = '{:07b}'.format(clock.datetime[3]).replace("0b", "")
    m = '{:07b}'.format(clock.datetime[4]).replace("0b", "")
    s = '{:07b}'.format(clock.datetime[5]).replace("0b", "")
    for d in range(len(h)):
        if h[d] == '1':
            dots[hourdotstart+d] = (255, 255, 255)
        else:
            dots[hourdotstart+d] = (0, 0, 0)
    for d in range(len(m)):
        if m[d] == '1':
            dots[minutedotstart+d] = (255, 255, 255)
        else:
            dots[minutedotstart+d] = (0, 0, 0)
    for d in range(len(s)):
        if s[d] == '1':
            dots[seconddotstart+d] = (255, 255, 255)
        else:
            dots[seconddotstart+d] = (0, 0, 0)
