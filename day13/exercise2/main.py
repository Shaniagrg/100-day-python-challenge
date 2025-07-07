while True:
    try:
        year = int(input("Which year do you want to check?"))

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Leap year.")
                else:
                    print("Not leap year.")
            else:
                print("Leap year.")
        else:
            print("Not leap year.")
    except ValueError:
      print("That's not a year!")
      continue
    
    ask_user:str = input("Type 'y' to continue  and 'n' to exit: " )
    if ask_user == 'y':
        continue
    elif ask_user == 'n':
        print("Thank you for playing!!")
    break