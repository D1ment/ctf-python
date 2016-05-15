# -*- coding: utf-8 -*-
import requests
import json
import socket

#######################################################
#Morze decod
def morze_dec(text_dec):
	url = 'https://gc.de/async.php'
	payload = {'decoded': '', 'key': '', 'encoded': text_dec, 'method': 'morse', 'decode': '1', 'encode': ''}
	r = requests.post(url, data=payload)
	js_new = json.loads(r.text)
	return js_new['decoded']

#######################################################
#Zamena decod
def zamen_dec(text_dec):
	x = {'a':3, 'd':5, 'g':8}
	for key in x.keys():
		text = text_dec.replace(key, str(x[key]))



sock = socket.socket()
sock.connect(('146.148.102.236', 24069))
data = sock.recv(200240)
print data
print '====================='
while 1:
	sock.send('a b c d e f g h i\n')
	data = sock.recv(200240)
	print data
	text = data[data.find('What is '):data.find('  decrypted?')]
	text = text[8:]
	text = morze_dec(text)
	sock.send(text + '\n')
	data = sock.recv(200240)
	print data