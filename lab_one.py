import random

# declare and initialize a list of words
words = ["orange", "animal", "river", "option", "sloth", "rainbow"]
# shuffling the words and putting them in a random order
random.shuffle(words)


print("A jumble takes the letters in a word and changes the order randomly")
print("it is the player's job to put the letters back into their right order. \n")
# go through words in list
for word in words:
    # use list cosntructor with string argument to get list of characters
    jumble=list(word)
    # put the characrers in random order
    random.shuffle(jumble)
    # use join method to put characters together to form a string
    display = "".join(jumble)
    # show user jumbled words
    print(display)
    # take in user's guess
    guess=input("Enter your guess for the jumbled word: ")
    #check the guess
    if guess == word:
        print("You got it!\n")
    else:
        print("No the word was {0}\n".format(word))