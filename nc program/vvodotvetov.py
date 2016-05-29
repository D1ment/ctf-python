# -*- coding: utf-8 -*-
import socket

sock = socket.socket()
sock.connect(('p.tjctf.org', 8006))
data = sock.recv(200240)

direction1 = ['north', 'west', 'examine journal2', 'east', 'east', 'east', 'examine paintedeye', 'down', 'examine book', 'up', 'west', 'west', 'south', 'south', 'examine paper' ]

for elem in direction:
	sock.send(elem + '\n')
	data = sock.recv(200240)
	print data
	print '====================='
	
