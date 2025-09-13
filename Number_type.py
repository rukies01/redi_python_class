#x = 22.1
#x
#print(type(x))--

x = (3+2) * (4 - 3)
y = 2 * x
z = 27 + x + y
print ("the value of x is", x, "the value of y is", y, "and the value of z is", 
      z,".")

x = 5. + 2.
print(type(x))

x = 3+ 2.
y = 2.5  * 3
z = (1.5 + .5) // 2
print("the value of x is", x, "the value of y is", y, "and the value of z iss", z)

first_string = "pine"
second_string = "apple"
single_space = " "

print(len(first_string))
print(first_string.replace("p","P"))
print(first_string.find("i"))
print(first_string + second_string)


lyric = "while my guiter gently weeps"

print(len(lyric))
print(lyric[5])
print(lyric[10])
print(lyric[15])
#print(lyric[35])

a = "Rukayyat"
b= "Rukies"
c = "yellow"

message = f"My name is {a}, And my Nicname is {b}, My favorite colour is {c}"
message_2 = f"{a}--{b}--{c}"

print(message_2)


lore_ipsum_text = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book. It has survived 
not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and 
more recently with desktop publishing software like Aldus PageMaker 
including versions of lorem Ipsum."""

# EXERCISE 2: Take the following text belo and write a program that prints 
#             the following information:
# 1) How many times the words "Lorem" and "Ipsum" appear in the text
# 2) The indexes of the first occurrence of the two words
# 3) (BONUS): The index of the last occurrence of the two words.
# 4) (BONUS): The strings "Lorem" and "lorem" both appear in the text, but 
# are considered different strings because of the capital/non-capital 
# letters. Find how many times the word appears *disregarding capitalization*.
# HINT: Search online for additional functions for strings to solve the 
# bonus exercises!

print(lore_ipsum_text.count("Lorem"))
#assignment 1

print(lore_ipsum_text.count("Ipsum"))

print(lore_ipsum_text.rindex("Lorem Ipsum"))
#assignment 3


lore_ipsum_text = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley 
of type and scrambled it to make a type specimen book. It has survived 
not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with 
the release of Letraset sheets containing Lorem Ipsum passages, and 
more recently with desktop publishing software like Aldus PageMaker 
including versions of lorem Ipsum."""

word = "lorem"
lore_ipsum_text_lower = lore_ipsum_text.lower()
word_lower= word.lower()
words = lore_ipsum_text_lower.split()
count_word = words.count(word_lower)
result = f"the word {word_lower} appeared {count_word} times"

print(result)










