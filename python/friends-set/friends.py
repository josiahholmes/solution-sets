#!/usr/bin/env python3

def friends(names: list) -> list:
    friends = []
    for name in names:
        if len(name) == 4:
            friends.append(name)
    return friends
    # Alternative return [name for name in names if len(names) == 4]