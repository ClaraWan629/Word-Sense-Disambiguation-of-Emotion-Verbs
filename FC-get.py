# this program is used to 1) strip the FC tags from the 500 tagged sentences
# 2) strip the tagged sentences
# Clara WAN
# 2018-07-23


# read the files under one directory
file = open('E:\\Buffer_data\\Tagged Data\\討厭_500.tag', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mylist = []
my_tagged_sent = []

for line in mytext:
    if line.find('%%') >= 0:
        mylist.append(line.strip("%%PATTERN: (0123456789/)\n"))

    elif line.find('##') == -1:
        my_tagged_sent.append(line)

my_tagged_sent2 = []
#remove the empty lines
for line in my_tagged_sent:
    if line != '\n':
        my_tagged_sent2.append(line)

#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\Taoyan500_CP.txt', 'w', encoding='utf-8') # only constructional patterns
for i in mylist:
    outfile.write(i+'\n')
outfile.close()

#write to a file
outfile2 = open('E:\\WSD_output\\Taoyan\\Taoyan500_tagged.txt', 'w', encoding='utf-8') # only tagged sentences
for j in my_tagged_sent2:
    outfile2.write(j)
outfile2.close()

print('Done!')