#!/usr/bin/env python3


def split_strings(lst):
    if len(lst) % 2 == 1:
        lst += '_'
    return [lst[i:i+2] for i in range(0, len(lst), 2)]