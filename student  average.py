students = int (input("total students: ")) # store the total student
list_of_students = [] #store the student name
mark = []  # store the student mark
total_mark = 0 # intialize the mark is zero
for total_student in range(0,students ):
    list_of_students.append(input("Enter the student name: ")) # enter the student name
    mark.append(int(input("Enter your mark: "))) #enter the student  mark 
    total_mark =total_mark+ mark[total_student] # calculate the tatal mark
for index in range(len(list_of_students,1)):
    print(str (list_of_students[index])  +  "scored" + str (mark[index]) )
print("total mark = ",total_mark) 
average = total_mark/students # calculate average mark
print("average mark of the class: ",average) 
