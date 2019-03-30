# this program is used to get the FC list in the 200 Taoyan sentences
# Clara WAN
# 2018-04-06

import nltk
from nltk import FreqDist


# read the files under one directory
file = open('E:\\Buffer_data\\Taoyan500-raw.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mylist = []

for line in mytext:
    for ch in line:
        mylist.append(ch)

fd = nltk.FreqDist(ch for ch in mylist)
fq = fd.most_common()

#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\Taoyan-unigram-list.txt', 'w', encoding='utf-8')
for x,y in fq:
    outfile.write(x +'\t')
outfile.close()

print('Done!')