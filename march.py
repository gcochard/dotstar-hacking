import time
import board
import adafruit_dotstar as dotstar
dots = dotstar.DotStar(board.SCK, board.MOSI, 72, brightness=0.01)
dotnum = len(dots)
dots.fill((0, 0, 0))
trail_len = 5
has_completed = False
while True:
    for d in range(dotnum+trail_len):
        r = d
        if d > trail_len:
            r = d - trail_len
        elif has_completed:
            d = r + 1
        if d >= dotnum:
            d %= dotnum
            has_completed = True
        if r >= dotnum:
            r %= dotnum
        dots[d] = (  0,   0, 255)
        if r < d or has_completed:
            dots[r] = (  0,   0,   0)
        time.sleep(.05)
