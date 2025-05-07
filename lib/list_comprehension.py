#!/usr/bin/env python3

def return_evens(num_list):
    pass
    return[num for num in num_list if num % 2==0]

def make_exclamation(sentence_list):
    pass
    if not sentence_list:
        return[]
    return[sentense + "!" for sentense in sentence_list]
    