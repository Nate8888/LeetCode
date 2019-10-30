def defangIPaddr2(address):
    newStr = ""
    for x in address:
        if x == ".":
            newStr += "[.]"
        else:
            newStr += x
    return newStr