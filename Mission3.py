#!/usr/bin/env python
#######################################################################
# Mission Description
#
# ##Description
#
# Then, make an HTTP POST request to the URL http://hdegip.appspot.com/challenge/003/endpoint 
# which contains the JSON string as a body part.
#
# * Content-Type: of the request must be "application/json".
# * The URL is protected by HTTP Basic Authentication, which is explained on Chapter 2 of RFC2617, so you have to provide an Authorization: header field in your POST request
# * For the "userid" of HTTP Basic Authentication, use the same email address you put in the JSON string.
# * For the "password", provide an 10-digit time-based one time password conforming to RFC6238 TOTP.
# 
# ** You have to read RFC6238 (and the errata too!) and get a correct one time password by yourself.
# ** TOTP's "Time Step X" is 30 seconds. "T0" is 0.
# ** Use HMAC-SHA-512 for the hash function, instead of the default HMAC-SHA-1.
# ** Token shared secret is the userid followed by ASCII string value "HDECHALLENGE003" (not including double quotations).
# 
# *** For example, if the userid is "ninja@example.com", the token shared secret is "ninja@example.comHDECHALLENGE003".
# *** For example, if the userid is "ninjasamuraisumotorishogun@example.com", the token shared secret is "ninjasamuraisumotorishogun@example.comHDECHALLENGE003"
#
# If your POST request succeeds, the server returns HTTP status code 200.
#
#######################################################################


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
