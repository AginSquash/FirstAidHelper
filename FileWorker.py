
def readFile():
    sympotms_dict = {}
    #f = open('FIRSTAIDHELPER.txt')
    with open("FIRSTAIDHELPER.txt", encoding='utf-8') as file:
        for line in file:
            data = line.split("-", maxsplit=1)
            sympotms_dict[data[0]] = data[1]
    return sympotms_dict
