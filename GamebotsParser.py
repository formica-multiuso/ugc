import sys
import socket
import threading
import select

class GamebotsParser(threading.Thread):
	def __init__(self,socket):
		threading.Thread.__init__(self)
		self.socket = socket
	def run(self):
		while 1:
			rlist, wlist, elist = select.select( [self.socket], [], [] )
			print self.socket.recv(1024)
