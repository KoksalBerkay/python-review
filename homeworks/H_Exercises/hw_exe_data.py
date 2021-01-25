'''Create a function that can recognize the number of unique characters in a string
entered by the user. For example Hello should be 4 characters. And your program should
push all unique characters to a list then print out the unique characters as new string.
Wow super mom --> wo super m'''

word = input("Pls give a word or sentence")
word = word.lower()
dic_boi = {}
list_boi = []
    
def unique_letter_detector():
    for letter in word:
        dic_boi[letter] = letter

    for thing in dic_boi:
        list_boi.append(thing)   

unique_letter_detector()
string_boi = "".join(list_boi)
print (string_boi)



