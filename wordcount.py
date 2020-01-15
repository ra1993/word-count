
def wordFreq(n):
    punctuations = "!,(),-,[],"",;,:,',<,>,.,/,?,@,#,$,%,^,&,*,_,~"

    opened_file = open(n, 'r')

    wordcount = {}

    for line in opened_file:
        line = line.split(" ")
        

        for i in line:
            if i in wordcount:
                 wordcount[i] += 1
            else:
                 wordcount[i] = 1
            print(i, wordcount[i])
    

    opened_file.close() 

print(wordFreq('article.txt'))
        