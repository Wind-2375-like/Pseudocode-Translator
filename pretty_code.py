import sys

def index_code(code):
    lines = code.split("\n")
    index_num = 0
    text = []
    for l in lines:
        index_num -= list(l).count("}")
        buf = "\t"*index_num + l
        index_num += list(l).count("{")
        text.append(buf+"\n")
    text = "".join(text)
    return text
