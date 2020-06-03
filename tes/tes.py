

#with open("tes.txt", "a") as f:
    #print("hello " + dunia, file = f)

f = open("tes1.txt", "r")
lines1 = f.read().split('\n')
f.close()

f = open("tes2.txt", "r")
lines2 = f.read().split('\n')
f.close()

lines = []


counter = 0

for i in lines1:
    newElement = lines1[counter] + lines2[counter]
    lines.append(newElement)
    counter = counter + 1
    





newcounter = 0
for i in lines:
    print(lines[newcounter])
    newcounter = newcounter + 1



with open("tes.txt", "w") as f:
    newcounter = 0
    for i in lines:
        print(lines[newcounter], file = f)
        newcounter = newcounter + 1



#linesID[1] = newIndex

#print(linesID)



#with open('tes.txt', 'w') as file:
    #for lines in linesID:
        #file.writelines(linesID[lines-1])

      