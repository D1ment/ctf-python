#========perebor sha1============================
#===alphabet number==============================
import hashlib

b = "a58dc2cfc5a93134666c607fbc5d6e961254214a"
i = 10000000
while True:
	print i
	a = hashlib.sha1(str(i)).hexdigest()
	i = i + 1
	if a == b:
		print i
		break
