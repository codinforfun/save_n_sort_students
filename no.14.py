nameslist=[]
seatinglist=[]
gradeslist=[]
conti="y"
while conti !="n":
    nameslist.append(input("enter the student name: "))
    seatinglist.append(int(input("enter the seating number: ")))
    gradeslist.append(input("enter the student grade: "))
    conti=input("do you want to continue?(y/n): ")
for x in range(len(seatinglist)):
    for i in range(len(seatinglist)-1):
        if seatinglist[i]>seatinglist[i+1]:
            Zseating=seatinglist[i]
            Znames=nameslist[i]
            Zgrades=gradeslist[i]
            seatinglist[i]=seatinglist[i+1]
            nameslist[i]=nameslist[i+1]
            gradeslist[i]=gradeslist[i+1]
            seatinglist[i+1]=Zseating
            nameslist[i+1]=Znames
            gradeslist[i+1]=Zgrades
print(seatinglist)
print(nameslist)
print(gradeslist)
fileName="studentsgrades.csv"
accessMode="w"
myFile=open(fileName,accessMode)
myFile.write("Names,")
myFile.write("Seating Number,")
myFile.write("Grades \n")
for i in range(len(seatinglist)):
    myFile.write(nameslist[i]+", ")
    myFile.write(str(seatinglist[i])+",  ")
    myFile.write(str(gradeslist[i]) +"\n")
myFile.close()
