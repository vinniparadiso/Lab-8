#Vinni, Benthany, Krista
#Number 8
import random
def random_int(x):
    random_number=random.randint(1,10)
    if x==random_number:
        print("Congratulations you guessed the number!")
    else:
        print("Sorry, try again!")

random_int(3)
random_int(8)
random_int(1)
random_int(2)
random_int(7)
