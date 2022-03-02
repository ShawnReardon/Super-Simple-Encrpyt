from mod import mod
from random import randint
class pairs:
  def __init__(self, ch, shift):
    self.ch = ch
    self.shift = shift


def mainLoop(string):

  string = string
  print(mod(5))

  for ch in string:
    print(ord(ch.capitalize()))


  def encrypt(string, shift = 1):
    coded_message = []
    for ch in string:
      shift = mod(ord(ch), randint(1,26))
      temp = pairs(ord(ch.capitalize())+shift, shift)
      coded_message.append(temp)
    encrypted_ = ""
    for ch in coded_message:
      encrypted_ += chr(ch.ch)
  
    print(encrypted_)
    print("Shifted:", coded_message[1].shift)


    return coded_message
      
  z = encrypt(string, 5)


  def dencrypt(codedString, shift = 1):
    decoded_message = ""
    for ch in codedString:
      decoded_message += chr(ch.ch-ch.shift)
    
    print(decoded_message)


  dencrypt(z, 5)