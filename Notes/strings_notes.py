# IB - Strings Notes

# Strings are a collectoin of characters held together by quotatoin marks

name = "Ms. LaRose"

age = "15"

print(age + '2')

print(name + " " + age)

first_name = 'Vienna'
last_name = 'LaRose'
full_name = first_name + " " + last_name
print(full_name)
# escape char \
sentence_two = '\tThen he said \n"that isn\'t fair"'
print(sentence_two)

print("%" * 30)
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
print(sentence.find("w"))
# Indexes start at zero, hence the 'w' being at 13, rather than 14
# If letter appears more than once, it does the first instance of the letter
print(sentence[10:15])
#It does not include the end point, but does include the start point.
word = input("What word do you want: ")
start_word = sentence.find(word) #.find finds the position of the word
length_word = len(word) #len gets you the length of the word
print(sentence[start_word:start_word+length_word])