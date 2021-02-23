def caseCount(word):

    ucase = 0
    lcase = 0

    for x in word:
        if(x.islower()):
            lcase += 1
        elif(x.isupper()):
            ucase +=1
    print("Word : "+word+" | Upper Case Count : "+str(ucase)+" Lower Case Count : "+str(lcase))

caseCount("Striker")
