import random

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

words = open("words.txt", "r")
lines = words.readlines()    
words = len(lines)
used = []

quessed = random.choice(lines)
quessed_word, question = quessed.replace("\n","").replace(" ", "").split(";")
quessed_word2 = "_" * len(quessed_word)
quessed_word3 = quessed_word

wheel = ["0", "100", "1000", "200", "500"]

work = True

score = 0
attempts = 0

print("-- Wheel of Fortune --\n")

while work:      
    print("\nTopic: " + question)
    print(quessed_word2)
    print("\nLetters used: " + ", ".join(used))
    print("\nSpin the wheel!")
    input()
    wheel_choice = int(random.choice(wheel))
    print(wheel_choice)
    choice = int(input("Letter(1) or word(2) or exit(3): "))
    if choice == 2:
        word = input("Your word: ")
        if word == quessed_word3:
            print("You win!")
            score += wheel_choice
            print("Score: " + str(score))
            work = False
        else:
            print("No! Incorrect word!")
            attempts += 1
    elif choice == 1:
        letter = input("Your letter: ")
        if quessed_word.find(letter) != -1 and letter != "":
            print("Yes!")
            score += wheel_choice
            while quessed_word.find(letter) != -1:
                quessed_word2 = separate(quessed_word2)
                quessed_word2[quessed_word.find(letter)] = letter
                quessed_word = quessed_word.replace(letter, "^", 1)
                quessed_word2 = unite(quessed_word2)
            if quessed_word.count("^") == len(quessed_word):
                print("You win!")
                print("Score: " + str(score))                
                work = False     
        else:
            print("No! Incorrect letter!") 
            used.append(letter)
            attempts += 1   
    elif choice == 3:
        work = False
    if attempts >= 3:
        print("\nYou lose!")
        work = False             