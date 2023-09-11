#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        n = len(sentence)
        return n, sentence[0]
    else:
        return 0, None
