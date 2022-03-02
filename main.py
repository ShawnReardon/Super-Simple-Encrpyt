from mod import *
from main2 import mainLoop


















string = "Hello I am Shawn"
#print(mod(5))
#mainLoop("Hello I am Shawn")

#pause = input('Press enter to continue ')
for ch in string:
  print(ord(ch.capitalize()))


def encrypt(string, shift = 1):
  coded_message = []
  for ch in string:
    coded_message.append(ord(ch.capitalize() +shift)
  encrypted_ = ""
  for ch in coded_message:
    encrypted_ += chr(ch)
  
  print(encrypted_)


  return coded_message
    
z = encrypt("Hello I am Shawn", 5)















def dencrypt(codedString, shift = 1):
  decoded_message = ""
  for ch in codedString:
    decoded_message += chr(ch-shift)
  
  print(decoded_message)


dencrypt(z, 5)