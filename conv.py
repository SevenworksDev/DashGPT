import json

def conv(objs):
    lvl = []
    for jsonlvl in objs:
        leveldata = "1,{},{},{},21,1;".format(jsonlvl["object"], jsonlvl["x"], jsonlvl["y"])
        lvl.append(leveldata)
    return "".join(lvl)

level = [
    {"object": 1, "x": 0, "y": 0},
    {"object": 1, "x": 10, "y": 0}
}

result = conv(level)
print(result)