word = str(input("Enter the Word: "))

reversed_word = word[::-1]
print('Reversed Word',reversed_word)

# Using for Loop
wordtwo = str(input("Enter the 2nd Word: "))
reversed_using_loop = ""
for char in wordtwo:
    reversed_using_loop = char + reversed_using_loop 


print("Reversed word using for",reversed_using_loop)