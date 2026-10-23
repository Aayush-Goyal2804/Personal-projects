import random


tries = 5


random_var = random.randrange(1,100)

print("A random number has been selected, you've got 5 tries to guess the correct number and defuse the bomb before the\n entire city is destroyed.")




while tries>=0:
    user_var = int(input("Enter your guess : "))

    if  user_var == random_var:
        print(f"You stopped the bomb from exploding. You had {tries+1} tries left")
        break
    elif tries == 0:
        print(f"Try again after some time later!! \n The random number was {random_var}")
        break

    else:
        print(f"Try again, you've got {tries} left.")
        tries-=1


#Test case
#print(random_var)