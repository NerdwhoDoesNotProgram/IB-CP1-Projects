# IB, 2nd period - Strings Methods Notes

sentence =  "The quick brown fox jumped over the lazy dog"

fixed = sentence.replace("fox", 'wolf')

word = input("What word do you want: ").strip().lower()
new_word = input("What word should be in the sentence: ").strip().lower()

location = sentence.find(word)
new_sentence = sentence.replace(word, new_word)
print(new_sentence)

first_name = input("What is your first name: ").strip().title()
last_name = input("What is your last name: ").strip().title()
first_separated = first_name.split()
fixed = "".join(first_separated)
last_separated = last_name.split()
last_fixed = "".join(last_separated)
full_name = fixed.title() + " " + last_fixed.title()
print("Hello "+ full_name.title())

print(full_name.isalpha()) # Checks to see if whole thing is letters
print(full_name.isnumeric()) # Numbers
print(full_name.isupper()) # Uppercase


#print("Hello " + name)

print(sentence.find("over"))

print(sentence.split("the"))

print(f"Lower: {sentence.lower()}")
print(f"Upper: {sentence.upper()}")
print(f"Capitalize: {sentence.capitalize()}")
print(f"Title: {sentence.title()}")
print(fixed)