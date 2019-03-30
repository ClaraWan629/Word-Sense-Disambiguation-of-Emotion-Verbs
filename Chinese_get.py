# this program is used to get the FC list in the 200 Wuliao sentences
# Clara WAN
# 2018-04-06


# read the files under one directory
file = open('E:\\Buffer_data\\Wuliao500_tagged.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mylist = []
for line in mytext:
    temp_line=[]
    for ch in line:
        if 0x4e00 <ord(ch)< 0x9fff:
            temp_line.append(ch)
    mylist.append(temp_line)

#write to a file
outfile = open('E:\\WSD_output\\Wuliao\\Wuliao500-raw.txt', 'w', encoding='utf-8')
for line in mylist:
    for x in line:
        outfile.write(x)
    outfile.write('\n')
outfile.close()

print('Done!')