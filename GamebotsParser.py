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
		
			print "\n" + "\033[34m" + "[" + self.name + "] " + "\033[0m"	
			for message in messages:
				pair = message.split(' ',1)
				
				if len(pair) > 1:
					print "\033[33m" + pair[0] + "\033[0m"
					payload = ''.join(pair[1])
					tokens = payload.split('{')
					tokens = ''.join(tokens)
					tokens = tokens.split('}')
					# Here I need to return sensors (SEN) information to the IRobot class splitted in dictionary
					for token in tokens:
						print token
					
					
			
	def parser(self):
		pass	
