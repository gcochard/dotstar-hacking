import board
import adafruit_dotstar as dotstar
dots = dotstar.DotStar(board.SCK, board.MOSI, 8, brightness=0.5)
dotnum = 8
dots[0] = (  0,   0,   0)
dots[1] = (  0,   0, 255)
dots[2] = (  0, 255, 255)
dots[3] = (  0, 255,   0)
dots[4] = (255, 255,   0)
dots[5] = (255, 255, 255)
dots[6] = (255,   0, 255)
dots[7] = (255,   0,   0)
