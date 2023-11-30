import hashlib
import time
import base64
import pyotp
from pyotp.utils import build_uri

secret_key = 'HENNGECHALLENGE003'
msg = 'codetest57@gmail.com'
key = msg+secret_key
passw = pyotp.TOTP(base64.b32encode(bytearray(key, 'ascii')), digits=10, digest=hashlib.sha512)
passwz = passw.now()
print(passwz) 
time.sleep(5)
print(passw.verify(passwz))
