'''=======================Repation of each word in file======================================================'''
'''
result = open('/home/ubantu/Documents/PROJECT/MyProjectDetails/ProjectDocs/LambdaImage.txt')
d={}
lcount =wcount =charcount = 0
for line in result:
    l1 = (line.split())
    lcount+=1

    if l1 ==[]:
        del l1
    else:
        print(l1)
        wcount+=len(l1)
        for word in l1 :
            charcount+=len(word)
            if word not in d.keys():

                d[word]=1

            else:
                d[word]+=1


print(d)
print(lcount)
print(wcount)
print(charcount)

'''

'''==============================WordCount ,LineCount and Charcount in File  WIth with open() function ===================================================='''


with open('/home/ubantu/Documents/PROJECT/MyProjectDetails/ProjectDocs/LambdaImage.txt') as file:
    res = file.readlines()
    # print(res)
    lcount =wcount =charcount = 0
    for line in res :
        # print(line)
        lcount+=1
        words = line.split()  #['use', 'cases.'] One of line content
        wcount+=len(words)
        print(words)
        for char in words :
            charcount+=len(char)


    print(lcount)   #6
    print(wcount)   #70
    print(charcount) #336


'''===============================Outputs of read methods========================================'''

'''
with open('/home/ubantu/Documents/PROJECT/MyProjectDetails/ProjectDocs/LambdaImage.txt') as f:
    lines=f.readlines()  # read entire content of file at once
    print(lines)     #list of lines ['Welcome to www.pythonexamples.org. Here, you will find python programs for all general \n', 'use cases.\n']
    line=f.read() # read entire content of file at once
    print(line)   #"this first line\nthis second line\n"
    print(type(line))   #Str

    line=f.readline(5)    #----------------Read only single line
    print(line)  #--------------Return the single line

    line=f.readline(5)   #----------------Read only single line
    print(line)   #Read first 5 characters from file  ex :Welco

'''