while True:

  try:
    number = int(input("Which number do you want to check?"))
    if number % 2 == 0:
      print("This is an even number.")
    else:
      print("This is an odd number.")
  except ValueError:
      print("That's not an int!")
      continue
  ask_user:str = input("Type 'y' to continue  and 'n' to exit: " )
  if ask_user == 'y':
    continue
  elif ask_user == 'n':
    print("Thank you for playing!!")
    break


