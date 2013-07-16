import sys
import os
import threading
import signal
from AIRRobot import *

def signal_handler(signal, frame):
        print 'Exiting...'
        os._exit(0)

def main():

	if len(sys.argv) < 2:
    		sys.stderr.write('Usage: ugc.py <host_ip_address>\n')
    		sys.exit(1)
	
	host = sys.argv[1]
	port = '3000'
	
	
	quad = AIRRobot(host,port,"UAV1")
	
	quad.start()
	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
	quad.join()

if __name__ == '__main__':
	main()
