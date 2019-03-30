# this program is used to get the FC tags list in the CP patterns
# Clara WAN
# 2018-07-23


# read the files under one directory
file = open('E:\\WSD_output\\Taoyan\\Taoyan500_CP.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mylist = []

for line in mytext:
    if line.find('-') >= 0:
        temp_list = line.strip('\n').split('-')
        mylist += temp_list
    else:
        mylist.append(line.strip('\n'))

myFC = set(mylist)
myFC.remove('[V]')

#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\Taoyan500_tags-list.txt', 'w', encoding='utf-8')
for i in myFC:
    outfile.write(i.strip('[]') + '\t')
outfile.close()

print('Done!')