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
    print (string)
    return string


def mutatePassword(oldPass):
    removeChar = .1
    addChar = .2
    changeChar = 1
    mutation = random.random()
    charToChange = math.floor(random.random() * len(oldPass))
    if mutation < removeChar:
        password = oldPass[:charToChange] + oldPass[charToChange + 1:]
    elif mutation < addChar:
        password = oldPass[:charToChange] + chr(math.floor(random.random() * 94) + 32) + oldPass[charToChange:]
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




def main():
    passwords = list()
    key = "banana"
    for i in range(100):
            string = generatePassword(math.floor(random.random() * 10))
            passwords.append(Password(string, comparePassword(string, key)))
    sortPasswords(passwords)
    for password in passwords:
        print(password.string + "      " + str(password.score))
        





if __name__ == "__main__":
    main()
