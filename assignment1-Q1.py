#Lists
names = ['Alice', 'Bob', 'Charlie', 'Daisy']
mid = [38, 43, 27, 39]
fin = [90, 60, 55, 87]

#Prints the title
print('STUDENT MARKS'.center(30, '*'))

#Prints the column names
print("{:<10}{:^5}{:^7}{:>8}".format('NAME', 'MID', 'FINAL', 'GRADE'))

#Loops through the list of names
for i in range(len(names)):
    #Calculates final grades
    finalGrade = mid[i] * 0.15 + fin[i] * 0.85
    #Prints student's results
    print("{:<10}{:^5}{:^7}{:>8.1f}".format(names[i], mid[i], fin[i], finalGrade))