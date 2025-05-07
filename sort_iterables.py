#sort() method = used with lists
# sort() function = used with  iterables

# students=("nishan","harimaya","harikala","anish","zaman")
# # students.sort(reverse=True)
# sorted_students=sorted(students,reverse=True)



# for i in sorted_students :
#     print(i)





students=[("Nishan","F",60),
          ("anish","A",60),
          ("hero","T",100),
          ("hari","F",60),
          ("shyam","B",70)
          ]
grade= lambda grades:grades[1]
students.sort(key=grade)
for i in students:
    print(i)