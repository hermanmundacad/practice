# First prompt

sentence = input("Please enter a sentence: \n")

print(sentence.upper()+"\n")

paragraph = input("Please enter a paragraph: \n")
count_words = len(paragraph.split(" "))
print(f"This paragraph has {count_words} words\n")

string1 = input("Please enter a stringg with only digits: \n")

try:
    for letter in string1:
        int(letter)
except ValueError:
    print("False\n")
else:
    print("True\n")

string2 = input("Please enter a stringg: \n")

print(string2.replace("a", "o"))

full_name = input("Please enter your full name: ")
initials = ""
for name in full_name.split(" "):
    initials = initials+name.capitalize()[0]+"."

print(f"Your initials are: {initials}")

string3 = input("Please enter the last string: ")

print(f"the length of your string is: {len(string3)}")
