#make it so we can uncompress stuff
def uncompress(item, fp): #a simple algorithm that just rexpands it 
    #make item into a string
    str(item)
    #check if fp is none and if so make it into a empty string
    if fp is None:
        fp = ""
    else:
        fp = str(fp)

    #get the data
    if fp == "":
        data = item
    else:
        with open(fp, 'r') as f:
            data = f.read()

    #split the data
    split_data = data.replace("+", "|+").split("|")

    #return the final data this is where we add the new lines
    return str("\n".join(split_data))

#make the new file
if __name__ == "__main__":
    write_data = uncompress(None, input('what is your file path ') + '.numc')
    with open(input('what is your file name ') + '.numbers', 'w') as f:
        f.write(write_data)