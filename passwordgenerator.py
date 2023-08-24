import random
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*","(",")"]
all=alphabet+numbers+symbols
#print(all)
user_alphabet=int(input("Enter how many no of letters u need:"))
user_numbers=int(input("Enter how many no of Numbers u need:"))
user_symbols=int(input("Enter how many symbols u need:"))
alpha_1=alphabet[0:user_alphabet]
num_1=numbers[0:user_numbers]
sym_1=symbols[0:user_symbols]
a=(alpha_1+num_1+sym_1)
print(a)
password_generator=random.shuffle(a)





