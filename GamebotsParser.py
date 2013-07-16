import sys
import socket
import threading
import select

class GamebotsParser(threading.Thread):
	def __init__(self,socket,name):
		threading.Thread.__init__(self)
		self.socket = socket
		self.name = name
	def run(self):
		while 1:
			rlist, wlist, elist = select.select( [self.socket], [], [] )
			self.messageBuffer = self.socket.recv(2048)
			
			messages = self.messageBuffer.split('\n')
		
			print "\033[34m" + "[" + self.name + "] " + "\033[0m"	
			for message in messages:
				print message 
			
			
