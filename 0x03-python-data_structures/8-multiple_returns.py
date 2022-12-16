#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) < 1:
        return length, None
    first = sentence[:1]
    return length, first
