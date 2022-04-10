with open("C:/Users/Bekir Emanet/Desktop/grades.txt","r",encoding="utf-8") as file:
    passers = list()
    leftovers = list()
    
    for column in file:
        column = column[:-1]
        column_elements = column.split(" ")
        if (column_elements[3] == "FF"):
            leftovers.append(column + "\n")
        else:
            passers.append(column + "\n")

    with open("C:/Users/Bekir Emanet/Desktop/leftovers.txt","a",encoding="utf-8") as leftoversList:
        for i in leftovers:
            leftoversList.write(i)
            
    with open("C:/Users/Bekir Emanet/Desktop/passers.txt","w",encoding="utf-8") as passersList:
        for i in passers:
            passersList.write(i)
    