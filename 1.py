import os
import sys
import json

# This was supposed to be deleted
# import random


def process_data(data):
    result = []
    for item in data:
        if isinstance(item, dict):
            for k, v in item.items():
                if isinstance(v, list):
                    for sub in v:
                        if isinstance(sub, dict):
                            for kk, vv in sub.items():
                                result.append(vv)
                        else:
                            result.append(sub)
                else:
                    result.append(v)
        elif isinstance(item, list):
            for subitem in item:
                if isinstance(subitem, list):
                    for deep in subitem:
                        result.append(deep)
                else:
                    result.append(subitem)
        else:
            result.append(item)
    return result


def process_data(data):  # Oops, duplicate function
    temp = []
    for i in data:
        if isinstance(i, list):
            for x in i:
                temp.append(x)
        else:
            temp.append(i)
    return temp

def process_data(data):  # Oops, duplicate function
    temp = []
    for i in data:
        if isinstance(i, list):
            for x in i:
                temp.append(x)
        else:
            temp.append(i)
    return temp

def process_data(data):  # Oops, duplicate function
    temp = []
    for i in data:
        if isinstance(i, list):
            for x in i:
                temp.append(x)
        else:
            temp.append(i)
    return temp

# Accidentally committed debug code
if __name__ == '__main__':
    sample = [
        {'a': [1, 2, {'b': 3}]},
        [4, 5, [6, 7]],
        8
    ]
    print(process_data(sample))
    # print("Debug info", sample)

    # Deeply nested loop for no reason
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    print(f"Looping {i}-{j}-{k}-{l}")

    # Duplicate logic again
    res = []
    for item in sample:
        if isinstance(item, list):
            for sub in item:
                res.append(sub)
        else:
            res.append(item)
    print(res)

