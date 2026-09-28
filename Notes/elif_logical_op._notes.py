# IB - Elif and Logical Operators Notes

age = 14    #int(input("What is your age: "))
license = True

if age >= 18: 
    print("Ypu are an adult and can vote!")
elif age >= 15 and license:
    print('You can drive! But you are still a minor, so go to school!')
elif age >= 15 and not license:
    print("You could drive, but you havent done the paperwork. (Also, go to school)")
else:
    print("You are too young to drive. Go to school")


win = True
hp = 25

if  win or hp <= 0:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("You lost :(")
else:
    print('The game is still going')