import random
import math

class Password(object):
    """A Password"""

    def __init__(self, length=4):
        string = generatePassword(length)








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
        char = math.floor(random.random() * 94)
        string = string + chr(char)
    print (string)
    return string


def mutatePassword(oldPass):
    banana = 2