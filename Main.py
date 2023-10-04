from random import choice
from collections import Counter

someWords = """apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon"""

someWords = someWords.split(" ")
word = choice(someWords)

for i in word:
    print("_", end=" ")

letterGuessed = ""
chances = len(word) + 2
flag = 0
print("Guess the word! HINT: word is a name of a fruit")
while chances != 0:
    print()
    chances -= 1
    try:
        guess = input("Write a letter to guess:")
    except:
        print("write only ONE letter")
        continue
    if len(guess) > 1:
        print("Write only one letter")
    if guess in letterGuessed:
        print("you already guessed that letter")
    if guess in word:
        chances += 1

        k = word.count(guess)
        for _ in range(k):
            letterGuessed += guess
    for char in word:
        if char in letterGuessed and Counter(letterGuessed) != Counter(word):
            print(char, end=" ")
        elif Counter(letterGuessed) == Counter(word):
            print(word)
            print("Congratulations, You Won")
            break
        else:
            print("_", end=" ")
    if chances == 0:
        print("You lost! Try again")
        print("The word was {}".format(word))
