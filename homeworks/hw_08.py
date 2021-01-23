# Exercise 131: Morse Code
# (15 Lines)
# Morse code is an encoding scheme that uses dashes and dots to represent numbers
# and letters. In this exercise, you will write a program that uses a dictionary to store
# the mapping from letters and numbers to Morse code. Use a period to represent a dot,
# and a hyphen to represent a dash. The mapping from letters and numbers to dashes
# and dots is shown in Table 6.1.
# Your program should read a message from the user. Then it should translate each
# letter and number in the message to Morse code, leaving a space between each
# sequence of dashes and dots. Your program should ignore any characters that are not
# letters or numbers. The Morse code for Hello, World! is shown below:

# .... . .-.. .-.. --- .-- --- .-. .-.. -..

# Table 6.1 Morse Code Letters and Numbers
# Letter Code Letter Code Letter Code Number Code
# A .- J .- - - S ... 1 .----
# B -... K -.- T - 2 ..---
# C -.-. L .-.. U ..- 3 ...--
# D -.. M -- V ...- 4 ....-
# E . N -.   W .- - 5 .....
# F ..-. O --- X - ..- 6 -....
# G --. P .--. Y - .- - 7 --...
# H .... Q --.-  Z --.. 8 ---..
# I .. R .-. 0 ----- 9 ----.


Morse_code = {"A" : ".-",        "J" : ".---",        "S" : "...",     "1" : ".----",
"B" : "-...",      "K" : "-.-",         "T" : "-",       "2" : "..---",
"C" : "-.-.",      "L" : ".-..",        "U" : "..-",     "3" : "...--",
"D" : "-..",       "M" : "--",          "V" : "...-",    "4" : "....-",
"E" : ".",         "N" : "-.",          "W" : ".--",     "5" : ".....",
"F" : "..-.",      "O" : "---",         "X" : "-..-",    "6" : "-....",
"G" : "--.",       "P" : ".--.",        "Y" : "-.--",    "7" : "--...",
"H" : "....",      "Q" : "--.-",        "Z" : "--..",    "8" : "---..",
"I" : "..",        "R" : ".-.",         "0" : "-----",   "9" : "----."}

value = []
The_word = input("Please write the sentence or word in capitals.")

for letter in The_word:
    if letter == " ":
        value.append(" ")
        continue

    if letter not in Morse_code:
        print('Data not formatted properly')
        break

    else:
        value.append(Morse_code[letter])
        # print(Morse_code[letter], end = ' ')

string_value = " ".join(value)
print(string_value)
    
