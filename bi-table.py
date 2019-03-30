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

#bi-gram list generation
bigram_list = []
for (i,j),y in fq:
    bigram_list.append(i + j)

# generate the attribute table
# read the files under one directory
file = open('E:\\WSD_output\\Taoyan\\Taoyan500-raw.txt', 'r', encoding='utf-8')
mylines = file.readlines()
file.close()

mytable = []

for line in mylines:
    temp_row = []
    for item in bigram_list:
        if line.find(item)>=0:
            temp_row.append(str(1))
        else:
            temp_row.append(str(0))
    mytable.append(temp_row)


#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\Bi-attr-table.txt', 'w', encoding='utf-8')
for line in mytable:
    for x in line:
        outfile.write(x+'\t')
    outfile.write('\n')
outfile.close()

print('Done the writing of the attribute table!')
