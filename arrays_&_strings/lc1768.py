#merge strings alternatively

def merge(word1:str, word2:str)->str:

    if len(word1)<=len(word2):
        smaller= word1
        larger=word2
    else:
        smaller=word2
        larger=word1
    
    lenDiff= abs(len(word1)-len(word2))

    if lenDiff!=0:
        additionalLetters= larger[-lenDiff : ]
    else:
        additionalLetters=""

    res=[]
    for i in range(len(smaller)):
        res.append(word1[i])
        res.append(word2[i])

    res.append(additionalLetters)

    return "".join(res)


print(merge("abc","pqr"))