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

# NP list generation
myNPs = []
for x,y in fq:
    myNPs.append(x)

# attribute table creation
# read the files under one directory
file = open('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\NP\\NP200.txt', 'r', encoding='utf-8')
mylines = file.readlines()
file.close()

mytable = []

for line in mylines:
    temp_row = []
    for item in myNPs:
        if line.find(item)>=0:
            temp_row.append(str(1))
        else:
            temp_row.append(str(0))
    mytable.append(temp_row)


#write to a file
outfile = open('C:\\Users\\Clara\\Desktop\\WSD-new\\Fan\\NP\\NP-table.txt', 'w', encoding='utf-8')
for line in mytable:
    for x in line:
        outfile.write(x+'\t')
    outfile.write('\n')
outfile.close()

print('Done the writing of the attribute table!')




