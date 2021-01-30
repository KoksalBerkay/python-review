# [17:47, 1/30/2021] Baba: In the game of Scrabble™️, each letter has points associated with it. The total score
# of a word is the sum of the scores of its letters. 
# Less common letters have more points whereas More common letters have fewer points.
# The points schema is shown below:
# [17:47, 1/30/2021] Baba:

#  One point 	A, E, I, L, N, O, R, S, T and U
# Two points 	D and G
# Three points 	B, C, M and P
# Four points 	F, H, V, W and Y
# Five points 	K
# Eight points 	J and X
# Ten points 	Q and Z

# [17:48, 1/30/2021] Baba: Write a program that computes and displays the Scrabble score for a word.
# Create a dictionary that maps from letters to point values. Then use the dictionary to
# compute the score


dict_scrabble = {"A" : 1, "E" : 1, "I" : 1, "L" : 1, "N" : 1, "O" : 1, "R" : 1, "S" : 1, "T" : 1, "U" : 1, 
"D" : 2, "G" : 2, "B" : 3, "C" : 3, "M" : 3, "P" : 3, "F" : 4, "H" : 4, "V" : 4, "W" : 4, "Y" : 4, "K" : 5, 
"J" : 8, "X" : 8, "Q" : 10, "Z" : 10}

the_word = input("Please write the sentence or word")
the_word = the_word.upper()
total_point = 0
list_boi = []

for letter in the_word:
    for item in dict_scrabble:
        if letter == item:
            list_boi.append(dict_scrabble[item])

number_boi = 0

for value in list_boi:
    number_boi = value + number_boi

print("Your Score :", number_boi)

