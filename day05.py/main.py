import random
import string
password:list[str] = []
final_password:str = ""
a = random.choice(string.ascii_letters) 
b = random.choice(string.digits)
c = random.choice(string.punctuation)

print("how many letters would you like in your password?")
letters:int = int(input(""))
for i in range(letters):
    password.append(a)


print("How many symbols would you like?")
symbol: int = int(input())
for ind in range(symbol):
    password.append(c)

print("How many numbers would you like?")
number:int = int(input())
for inde in range(number):
    password.append(b)

for index in range(0,len(password),+1):
    final_password = final_password + password[index]
print(f"Here is your password: {final_password }")
print("Your password is strong.")