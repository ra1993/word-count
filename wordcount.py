import string

def remove_punctuation(text):
    result = ""
    for p in text:
        p = p.strip('“,”') 
        if p not in string.punctuation:
            result += p
    return result   

def wordFreq(n, num_values= 10):

    opened_file = open(n, 'r')

    wordcount = {}
    
    counter = 0
    for line in opened_file:
        line = line.lower()

        line = remove_punctuation(line) #removes punctuations.....
        line = line.split(" ")
        
        for i in line:
            if i in wordcount:
                 wordcount[i] += 1
            else:
                 wordcount[i] = 1
 
    for k, v in sorted(wordcount.items(), reverse=True, key = lambda x: x[1]):
    
        if counter <=  num_values: 
            counter += 1
            print(k, v) 
          
    opened_file.close() 

print(wordFreq('article.txt', 20))


        