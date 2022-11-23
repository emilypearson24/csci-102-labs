#Emily Pearson
#CSCI 102 - Section F
#week 12
#resources: https://www.w3schools.com/python/ref_list_count.asp , 
#time:


def load_file(filename):
    with open(filename,'r') as filereader:
        lines = filereader.readlines()
        linestrip = []
        for line in lines:
            linestrip.append(line.strip())
    return linestrip

def update_string(string1, string2, indexnum):
    #indexnum = int(indexnum)
    newstring = string1[0:indexnum] + string2 + string1[(indexnum+1):]
    return newstring

def find_word_count(linestrip, word):
    print(linestrip)
    word = word.strip()
    wordcount = 0
    for i in linestrip:
        wordcount += i.count(word)
    return wordcount


