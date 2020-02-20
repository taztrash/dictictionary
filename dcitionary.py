#collection which is unordered,changeable and indexed.
student = {
    'name' : 'James',
    'email' : 'james@gamil.com',
    'phone no' : 744352345,
    'ADM' : 989898,
}
print (student)

#Accesing items 
x = student['email']
print(x)

#using get() to access items
y = student.get('email')
print(y)

f = student.get('ADM')
print(f)

#changing values in the dictionary
student['name'] = 'john' 
print (student)

#loop through a dictionary
for s in student : 
    print(s)
# values 
for value in student. values():
    print(value)

# items () in accessing both values and keys
for k, v in student.items():
    print(k,v)


# Check if item exists
if "name" in student:
    print('hakuna matata')
if "wakiritho" in student:
    print('hakuna matata')
else:
     print('shida nyingi')

#adding an item
student ['reg-no']="BSCIT-05_0091/2018"
print(student)

student['marital status']="married"
print(student)

student['age']="78"
print(student)

#removing an item 
student.pop('age')
print (student)

#to determine how many items(key-value pairs) a dictionary has
print (len(student))

#removing the last item from the dictionary
student.popitem()
print(student)

#updating the dictionary with the specified key-value pairs\
student.update({"gender" : "male"})
print(student)

#make a copy of a dictionary with the copy() method
student = student.copy()
print(student)

#returning athe value of the specified key
student=student.setdefault('name:' , 'kamau:')
print(student)