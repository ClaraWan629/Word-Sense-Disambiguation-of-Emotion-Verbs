import nltk
from nltk.util import ngrams
from nltk import FreqDist

# read the files under one directory
file = open('E:\\WSD_output\\Taoyan\\Taoyan500-raw.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mybigrams = []

for line in mytext:
    mybigrams += list(ngrams(line.strip('\n'), 2)) #tuples

fd = nltk.FreqDist(bigram for bigram in mybigrams)
fq = fd.most_common()


#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\bi-list.txt', 'w', encoding='utf-8')
for (i,j),y in fq:
    outfile.write(i + j +'\t')
outfile.close()

print('Done!')