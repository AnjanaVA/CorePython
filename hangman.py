import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                    

'''
print(logo)

stages = [ '''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']

animal_name=["chiken","dog","goat","monkey","gorilla","camel"]
animal=(random.choice(animal_name))

animal_list=[]
for i in animal:
    animal_list.append("_")
print(animal_list)
      
life=6
while life>0:
    user_guess=input("Enter the letter:").lower()
    if user_guess in animal:
        for i in range(len(animal)):
            if animal[i]==user_guess:
                animal_list[i]= user_guess
        if "_" not in animal_list:
            print("\n You won!",animal)
            
            break
    else:
        life -=1
        print("Lives left:",life)
        print(stages[6 - life])
        if life == 0:
            print("you failed,",animal)
            print(stages[0])
            break
        #print(stages[6 - life])
          
    print(animal_list)