# IB Hello World

name=input("What is your name: ").strip().capitalize()
print("Hello, " + name)

howDoYouDo=input("How are you today: ").strip().lower()

if(howDoYouDo=="bad"):
    print("I am sorry that you are feeling " + howDoYouDo+ ". I hope being at school makes your day better!")
else:
    print("You're feeling " + howDoYouDo + "?! Is that because of school?")