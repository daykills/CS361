def printInput():
  val = input("Enter your value: ")
  print(val)
  confirmed = False
  userConfirm = input("Is this what you want to print?")
  if confirmed == '1':
    confirmed = True
  elif userConfirm == 'yes':
    confirmed = True
  elif userConfirm == 'Yup':
    confirmed = True
  if confirmed == True:
    print('your input is: ', val)
  else:
    print('You did not confirm your input')
  return 


  def printInput():
  val = input("Enter your value: ")
  confirmed = False
  userConfirm = input("Is this what you want to print?", val)
  if userConfirm == '1' or userConfirm == "yes" or userConfirm == "Yup":
    confirmed = True
    print('your input is: ', val)
  else:
    print('You did not confirm your input')
  return 