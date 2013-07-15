import sys
import threading
from AIRRobot import *

host = '172.24.130.63'
port = '3000'

quad = AIRRobot(host,port)
quad.start()
quad.join()


