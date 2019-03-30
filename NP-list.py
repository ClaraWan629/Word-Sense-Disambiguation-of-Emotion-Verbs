import nltk
from nltk import FreqDist


# read the files under one directory
file = open('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\NP\\NP200.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

#create the NP list
NPlist = []
for line in mytext:
    if line.find('-')>=0:
        NPlist += line.strip('\n').split('-')
    else:
        NPlist.append(line.strip('\n'))


fd = nltk.FreqDist(ch for ch in NPlist)
fq = fd.most_common()

#write to a file
outfile = open('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\NP\\NP-list.txt', 'w', encoding='utf-8')
for x,y in fq:
    outfile.write(x +'\t')
outfile.close()

print('Done!')




