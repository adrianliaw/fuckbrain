# Original Java code:
# http://codegolf.stackexchange.com/questions/5418/brainfuck-golfer/5440#5440

import pickle
from pathlib import Path

with (Path(__file__).parent / "table.pkl").open("rb") as f:
    G = pickle.load(f)


def generate(s):
    code = ""
    lastc = 0
    for c in s:
        a = G[lastc][ord(c)]
        b = G[0][ord(c)]
        if len(a) <= len(b):
            code += a
        else:
            code += ">" + b
        code += "."
        lastc = ord(c)
    return code

def beautify(code, s):
    output = ""
    lines = code.split(".")
    for l, c in zip(lines, s):
        output += '{0}    {1}.\n'.format(repr(c), l)
    return output

def generate_beautified(text):
    return beautify(generate(text), text)

if __name__ == "__main__":
    print(generate_beautified("Hello World!"))
