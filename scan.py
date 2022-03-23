import time
import board
import adafruit_dotstar as dotstar
dots = dotstar.DotStar(board.SCK, board.MOSI, 72, brightness=0.01)
dotnum = len(dots)
dots.fill((0, 0, 0))
trail_len = 10
has_completed = False
try:
    while True:
        for d in range(0, dotnum, 1):
            print(f"d: {d}")
            r = d
            if d >= trail_len:
                r = d - trail_len
            if d >= dotnum:
                print("d >= dotnum", d, dotnum)
                has_completed = True
                break
            if r >= dotnum:
                print("r >= dotnum", r, dotnum)
                r %= dotnum
            dots[d] = (255,   0,   0)
            if r < d or has_completed:
                for r in range(d-trail_len, d):
                    brightness = 255-int(255*((d-r)/trail_len))
                    print(f'brightness: {brightness}, r: {r}, d: {d}, (d-r)/trail_len: {(d-r)/trail_len}')
                    dots[r] = (brightness,   0,   0)
            time.sleep(.01)
        for e in range(dotnum-1, 0, -1):
            print(f"e: {e}")
            r = e
            if e >= trail_len:
                r += trail_len
            if e < 0:
                print("e < 0", e, dotnum)
                has_completed = False
                break
            dots[e] = (255,   0,   0)
            if r > e and r < dotnum:
                # this needs work
                for r in range(e, e-trail_len):
                    brightness = 255-int(255*((e-r)/trail_len))
                    print(f'brightness: {brightness}, r: {r}, d: {e}, (e-r)/trail_len: {(e-r)/trail_len}')
                    dots[r] = (brightness,   0,   0)
            time.sleep(.01)
except KeyboardInterrupt:
    for d in range(dotnum):
        dots[d] = (0, 0, 0)
