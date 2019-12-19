
def readFile():
    sympotms_dict = {}
    f = open('FIRSTAIDHELPER.txt')
    for line in f:
        data = line.split("-", maxsplit=1)
        sympotms_dict[data[0]] = data[1]
    return sympotms_dict
