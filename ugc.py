










import sys
import threading
from AIRRobot import *

def main():

	if len(sys.argv) < 2:
    		sys.stderr.write('Usage: ugc.py <host_ip_address>\n')
    		sys.exit(1)
	
	host = sys.argv[1]
	port = '3000'
	
	
	quad = AIRRobot(host,port)
	quad.start()
	quad.join()

if __name__ == '__main__':
	main()
