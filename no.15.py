import csv
seatlistsearch=[]
namelist=[]
gradelist=[]
with open("studentsgrades.csv","r") as thisfile:
    allRowsList =csv.reader(thisfile)
    for currentRow in allRowsList :
            namelist.append(currentRow[0])
            seatlistsearch.append(currentRow[1])
            gradelist.append(currentRow[2])
start=1
found=False
end=len(seatlistsearch)
wanted_number=int(input("enter the seating number to search: "))
while end-start != 1:
    current_location=int((end+start)/2)
    current_number=int(seatlistsearch[current_location])
    if current_number>wanted_number:
        end=current_location
    elif current_number<wanted_number:
        start = int((end-start)/2)+start
    else:
        found =True
        break
if found ==True:
    print("the students' name is: "+namelist[current_location])
    print("the students' grade is: "+gradelist[current_location])
else:
    print("the student isn't in the list")
