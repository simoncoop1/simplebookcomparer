import argparse

#parse arguments
parser = argparse.ArgumentParser(description='comparing books for unique words')
#parser.add_argument('main book',nargs=1,
#               help='the filename of the main book everything will be compared to')
parser.add_argument('--count', dest='count', action='store_true',
               help='show the word counts')

args = parser.parse_args()

#def read book return dict
def read(path):
    words = {}
    with open(path,'r') as f:
        for line in f:
            for word in line.split():
               word = word.strip('.,[]_()')
               word = word.lower()
            
               if(word in  words):
                   words[word]= words[word]+1
               else:
                   words[word]=1  

    return words

# count the words by sum(word*frequency)
def wordcou(adic):
    wcount=0
    for aWord in adic.keys():
        wcount+=adic[aWord]
    return wcount

#def negat one dict to another normalised dict, to get rid of words usual words
def negate(dicmain,diccom_norm):
    newDic = {}

    for k in dicmain.keys():
        if k in diccom_norm.keys():
            newDic[k] = dicmain[k]-(diccom_norm[k]*wordcou(dicmain))
        else:
            newDic[k] = dicmain[k]

    return newDic

def main():
    words = {}
    words = read('book.txt')
    wordso = sorted(words,key=lambda word:words[word])

    #for item in wordso:
    #    print(item,words[item])

    #wcount=0
    #for aWord in wordso:
    #    wcount+=words[aWord]
    print("word count:",wordcou(words))


    words2= read('book2.txt')
    print("word count2:",wordcou(words2))
    wordso2 = sorted(words2,key=lambda word:words2[word])
    #print("max:",words2[wordso2[-1]])
    #normailized= 1/max
    for k in wordso2:
        words2[k]=words2[k]*(1/words2[wordso2[-1]])
    #for item in wordso2:
    #    print(item,words2[item])


    negatee = negate(words,words2)
    negateso = sorted(negatee,key=lambda word:negatee[word])
    for item in negateso:
        print(item,negatee[item])



if args.count:
    words = {}
    words = read('book.txt')
    words2 = read('book2.txt')
    print("word count main book:",wordcou(words))
    print("word count compared book:",wordcou(words2))
else:
    main()




#do a word count

##train it and get normalised count.
#then unnormalise trained data, deduct trained data from data of interest. you get a
# rankedcount of most common words and how much more than the trained data. Also what
# the data of interest in lacking in comparison to the trained.
# add comand line for not doing any negating
# add code for having more than single second book