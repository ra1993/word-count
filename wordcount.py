import string

def remove_punctuation(value):
    result = ""
    for p in value:
        p = p.strip('“,”')
        if p not in string.punctuation:
            result += p
    return result   


def wordFreq(n):

    opened_file = open(n, 'r')

    wordcount = {}
    top10 = []

    for line in opened_file:
        line = line.lower()

        line = remove_punctuation(line) #removes punctuations.....
        line = line.split(" ")
        
    
        for i in line:
            if i in wordcount:
                 wordcount[i] += 1
            else:
                 wordcount[i] = 1

    counter = 0
    for k, v in sorted(wordcount.items(), reverse=False, key = lambda x: x[1]):
    
        if counter <  10:
            counter += 1
        print(k, v)   


    opened_file.close() 

print(wordFreq('article.txt'))
        