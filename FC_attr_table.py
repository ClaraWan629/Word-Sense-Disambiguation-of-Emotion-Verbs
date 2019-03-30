# this program is used to produce the attribute table of the FC context
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
myFC_list = [x.strip('[]') for x in myFC]
#myFC_list.remove('')
myFC_list.remove('V') # generate the attribute list

# read the tagged file under one directory
file = open('E:\\WSD_output\\Taoyan\\Taoyan500_tagged.txt', 'r', encoding='utf-8')
tagged = file.readlines()
file.close()
mytable = []

for line in tagged:
    temp_row = []
    for item in myFC_list:
        if line.find(item)>=0:
            temp_row.append(str(1))
        else:
            temp_row.append(str(0))
    mytable.append(temp_row)


#write to a file
outfile = open('E:\\WSD_output\\Taoyan\\Taoyan500_attr-table.txt', 'w', encoding='utf-8')
for line in mytable:
    for x in line:
        outfile.write(x+'\t')
    outfile.write('\n')
outfile.close()

print('Done the writing of the attribute table!')





