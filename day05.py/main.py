import random
import string  
password:list[str] = []
final_password:str = ""

print("how many letters would you like in your password?")
letters:int = int(input(""))
for i in range(0,letters,+1):
    a:str = random.choice(string.ascii_letters) 
    password.append(a)


print("How many symbols would you like?")
symbol: int = int(input())
for ind in range(0,symbol,+1):
    c:str = random.choice(string.punctuation)
    password.append(c)

print("How many numbers would you like?")
number:int = int(input())
for inde in range(0,number+1):
    b:str = random.choice(string.digits)
    password.append(b)

for index in range(0,len(password),+1):
    final_password = final_password + password[index]
print(f"Here is your password: {final_password }")
print("Your password is strong.")