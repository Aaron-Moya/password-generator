import sys
import random

class PasswordGenerator:
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

    def __init__(self):
        pass
    
    def getRandomCharacter(self):
      character = random.choice(self.characters)
      self.characters = self.characters.replace(character, '')
      return character
    
    def askForLength(self):
      return int(input("Enter the length of your password: "))
    
    def generatePassword(self):
      password = ''

      if len(sys.argv) == 2:
         password_length = int(sys.argv[1])
      else: 
         password_length = self.askForLength()

      for i in range(password_length):
         password += self.getRandomCharacter()

      return password

try:
    password_generator = PasswordGenerator()
    print(f'Generated password: {password_generator.generatePassword()}')
except Exception as e:
    print('The length of your password must be an integer.')

