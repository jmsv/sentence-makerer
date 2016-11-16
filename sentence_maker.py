#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import load_wiki


class SentenceMaker:
    def __init__(self):
        pass

    def make_sentence(self, first_word, source="wikipedia"):
        if source == "wikipedia":
            word_list = load_wiki.get_list(15)
        else:
            word_list = load_text_file(source)
        for word in word_list:
            if "(" in word or ")" in word or "\"" in word or "'" in word:
                word_list.remove(word)
        if first_word not in word_list:
            raise ValueError("This word does not exist in the file")
        sentence = ""
        next_word = first_word
        for i in range(10):
            sentence += next_word + " "
            next_word = find_next_word(word_list, next_word)
        while next_word[-1] != ".":
            sentence += next_word + " "
            next_word = find_next_word(word_list, next_word)
        sentence += next_word
        return sentence


def load_text_file(filename="oliver-twist"):
    with open("text-files/" + filename + ".txt", 'r') as f:
        output = f.read()
    return output.split()


def find_next_word(word_list, current_word):
    following_list = []
    for index, word in enumerate(word_list):
        if word == current_word:
            following_list.append(word_list[index+1])
    return random.choice(following_list)
