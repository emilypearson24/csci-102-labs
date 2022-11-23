#Emily Pearson
#CSCI 102 - Section F
#week 12
#resources:
#time:


def load_file(filename):
    with open(filename,'r') as filereader:
        lines = filereader.readlines()
        linestrip = []
        for line in lines:
            linestrip.append(line.strip())
    return linestrip
