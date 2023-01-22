import random
import string

def generatePassword():
  specials = "!@#$&%^*|()_-+"

  selLen = input('Provide password length:')
  selLen = int(selLen)
  selDig = input('Use digits? (y/n):')
  selDig = string.digits if selDig == 'y' else ""
  selUpp = input('Use upper case letters? (y/n):')
  selUpp = string.ascii_uppercase if selUpp == 'y' else ""
  print("selUpp " + selUpp)
  selSpec = input('Use special characters? (y/n):')
  selSpec = specials if selSpec == 'y' else ""
  print("selSpec " + selSpec)
  password = "".join(random.choice(string.ascii_lowercase + selUpp + selDig + selSpec) for i in range(selLen))
  print("Generated password: " + password)
  return


def main():
  while True:
    message = '''\n-- Password Genrator --\n
    Choose option:
    1: generate password
    2: exit program \n
    '''

    print(message)
    selection = input("Your Choice: ")
    print (selection)

    if selection == '2':
      print('Bye!')
      break
    elif (selection == '1'):
      generatePassword()
    else:
      print('Please enter a correct value')


if __name__ == '__main__':
  main()

