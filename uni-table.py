# this program is used to get the FC list in the 200 Fan sentences
# Clara WAN
# 2018-04-06

# read the word list file under one directory
file = open('E:\\WSD_output\\Fan\\Fan-unigram-list.txt', 'r', encoding='utf-8')
myline = file.readline()
file.close()

# creat the word list
myword = []
for char in myline:
    if char != '\t':
        myword.append(char)

# read the raw 200 file under one directory
file = open('E:\\Buffer_data\\Wuliao500-raw.txt', 'r', encoding='utf-8')
mylines = file.readlines()
file.close()

mytable = []

for line in mylines:
    temp_row = []
    for item in myword:
        if line.find(item)>=0:
            temp_row.append(str(1))
        else:
            temp_row.append(str(0))
    mytable.append(temp_row)


#write to a file
outfile = open('E:\\WSD_output\\Fan\\Fan-Uni-attr-table.txt', 'w', encoding='utf-8')
for line in mytable:
    for x in line:
        outfile.write(x+'\t')
    outfile.write('\n')
outfile.close()

print('Done the writing of the attribute table!')
