#open file
file1 = open("file1.txt")
file2 = open("file2.txt")
#convert into str
line1 = file1.read().replace("\n", " ")
line2 = file2.read().replace("\n", " ")

#convert into list
liste1=list(line1.strip())
liste2=list(line2.strip())

i=0
y=0
for i in range(len(liste2)):
    if liste1[y]!=liste2[i]:
        print(liste2[i])
    else:
        y=y+1

#close file
file1.close()
file2.close()

