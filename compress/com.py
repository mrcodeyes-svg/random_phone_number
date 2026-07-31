def compress(items, fp): #a algorithm that just takes all the new lines out
    items = str(items) #make these into strings
    #check if its none and if so make it into a empty string
    if fp is None:
        fp = ""
    else:
        fp = str(fp)

    if fp == "":
        data = items
    else:
        with open(fp, 'r') as f:
            data = f.read() #get the data

    #make data into a list
    data = list(data)

    #clear it of new lines
    data = [x for x in data if x != "\n"]

    return str("".join(data)) #join them back together