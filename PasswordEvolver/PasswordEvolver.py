import random
import math

class Password:
    def __init__(self, string, score):
        self.string = string
        self.score = score


def comparePassword(password, key):
    """Returns a value between 0 and 1, as a score for how well the password matches the given key"""
    # characters correct / total characters
    correct = 0
    for index, char in enumerate(password):
        if index < len(key):
            if char is key[index]:
                correct = correct + 1
        else:
            correct = correct - (len(password) - len(key))
            if correct < 0:
                correct = 0;
    return correct / len(key)


def generatePassword(length):
    string = ""
    for i in range(length):
        char = math.floor(random.random() * 94) + 32;
        string = string + chr(char)
    return string


def mutatePassword(oldPass):
    removeChar = .1
    addChar = .2
    addCharToEnd = .3
    changeChar = 1
    mutation = random.random()
    charToChange = math.floor(random.random() * len(oldPass))
    if mutation < removeChar:
        password = oldPass[:charToChange] + oldPass[charToChange + 1:]
    elif mutation < addChar:
        password = oldPass[:charToChange] + chr(math.floor(random.random() * 94) + 32) + oldPass[charToChange:]
    elif mutation < addCharToEnd:
        password = oldPass + chr(math.floor(random.random() * 94) + 32)
    elif mutation < changeChar:
        password = oldPass[:charToChange] + chr(math.floor(random.random() * 94) + 32) + oldPass[charToChange + 1:]
    return password;

def sortPasswords(passwords):
    swapped = True
    sorted = 0;
    while swapped is True:
        swapped = False
        sorted = sorted + 1
        for i, password in enumerate(passwords[:len(passwords) - sorted]):
            if password.score < passwords[i + 1].score:
                tmp = password
                passwords[i] = passwords[i+1]
                passwords[i+1] = tmp
                swapped = True

## I need to make this method more random
def doSelectionAndCreation(passwords, key):
    half = math.floor(len(passwords)/2)
    for i, password in enumerate(passwords[half:len(passwords)]):
        string = mutatePassword(passwords[i].string)
        score = comparePassword(string, key)
        passwords[half + i] = Password(string, score)

def printUpdate(passwords):
    print(passwords[0].string + " " + str(passwords[0].score))
    print(passwords[50].string + "  " + str(passwords[50].score))
    print(passwords[len(passwords) - 1].string + "  " + str(passwords[len(passwords) - 1].score))

def main():
    passwords = list()
    key = "I do sure enjoy bananas, apples, and peaches!"
    for i in range(100):
            string = generatePassword(math.floor(random.random() * 10))
            passwords.append(Password(string, comparePassword(string, key)))
    gen = 0
    while passwords[0].score != 1:        
        sortPasswords(passwords)
        doSelectionAndCreation(passwords, key)
        print("Generation: " + str(gen))
        printUpdate(passwords)
        gen = gen + 1
        if gen % 10 == 0:
            input("Press any key to proceed...")
        print()

    print("The winning password was evolved!")



if __name__ == "__main__":
    main()
