import re


def to_digits(s):
    temp = [i for i in re.split(r'([0-9]+)', s) if i != '']
    result = []
    for e in temp:
        try:
            result.append(int(e))
        except ValueError:
            result.append(e)
    return result

def build_key(s):
    key = []
    d = to_digits(s)
    for i in d:
        if isinstance(i, str):
            key.append(i)
    key = [''.join(key)]
    for i in d:
        if not isinstance(i, str):
            key.append(i)
    return key

def sort(s):
    return sorted(s, key=build_key)
