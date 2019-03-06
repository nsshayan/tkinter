

""" file = open('./CMSP_dup.txt','r')
line = file.readline()
 """

def writetoendofline(lines, line_no, append_txt):
    lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'

with open('./CMSP_dup.txt', 'r') as txtfile:
    lines = txtfile.readlines()
    
writetoendofline(lines, 4, ' 2020-03-11 21:30')


# write the edited content back to the file
with open('./text', 'w') as txtfile:
    txtfile.writelines(lines)

# close the file
txtfile.close()
