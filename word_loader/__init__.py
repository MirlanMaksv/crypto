import json
import os
import sys


def load_words():
    try:
        filename = os.path.join(
            os.getcwd(), "word_loader/words.json")
        with open(filename, "r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)


def load():
    try:
        filename = os.path.join(os.getcwd(), "word_loader/words.txt")
        with open(filename, "r") as wordsfile:
            return wordsfile.readline().split(" ") 
    except Exception:
        return None


# words_list = load()
words_dict = load_words()