# coding: utf8
import random

global words, lines, words, used, quessed, quessed_word, quessed_word2, quessed_word3

words = open("words.txt", encoding='utf8')
lines = words.readlines()    
words = len(lines)
used = []

quessed = random.choice(lines)
quessed_word, question = quessed.replace("\n","").split(";")
quessed_word2 = "*" * len(quessed_word)
quessed_word3 = quessed_word

wheel = ["0", "100", "200", "300", "400","500", "600", "700", "800", "900", "1000"]

work = True

def separate(string):
    array = []
    for i in string:
        array.append(i)
    return array

def unite(array):
    string = ""
    for i in array:
        string += str(i)
    return string

def turn(player):
    global words, lines, words, used, quessed, quessed_word, quessed_word2, quessed_word3
    print("\nTopic: " + question)
    print(quessed_word2)
    print("\nLetters used: " + ", ".join(used))
    print("\nSpin the wheel, " + player.name + "!")
    input()
    wheel_choice = int(random.choice(wheel))
    print(wheel_choice)
    choice = int(input("Letter(1) or word(2) or exit(3): "))
    if choice == 2:
        word = input("Your word: ")
        if word == quessed_word3:
            print("You win!")
            player.score += wheel_choice
            return 0
        else:
            print("No! Incorrect word!")
    elif choice == 1:
        letter = input("Your letter: ")
        if quessed_word.find(letter) != -1 and letter != "":
            print("Yes!")
            player.score += wheel_choice
            while quessed_word.find(letter) != -1:
                quessed_word2 = separate(quessed_word2) 
                quessed_word2[quessed_word.find(letter)] = letter
                quessed_word = quessed_word.replace(letter, "^", 1)
                quessed_word2 = unite(quessed_word2)
            if quessed_word.count("^") == len(quessed_word):               
                return 0
        else:
            print("No! Incorrect letter!") 
            used.append(letter)
    elif choice == 3:
        return 3        
    
class Player():
    name = ""
    score = 0
    def __init__(self, name):
        self.name = name
        self.score = 0
    

print("-- Wheel of Fortune --\n")

players = int(input("Input player count: "))

players = [Player("player " + str(i)) for i in range(players)]

while work:      
    for i in players:
        returnment = turn(i)
        if returnment == 0:
            print(i.name + " win!")
            print("His score: " + str(i.score))
            work = False
            break
        elif returnment == 3:
            work = False
            break