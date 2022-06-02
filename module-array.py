from array import array
scores = array('d')  # our backet will store doubles
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# common operation
names = ['Susan', 'Christopher']
print(len(names))

names.insert(0, 'Bill') #insert before index
print(names)
names.sort() # sort in ascending order
print(names)

#retrieving ranges
students = ["Susan", "Christopher", "Bill", "Justin"]
presentes = students[1:3]
#start and end index

print(students)

