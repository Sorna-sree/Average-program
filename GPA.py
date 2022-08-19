students=3 #number of student
subjects=3 #number of subjects
gpa=0  
total_gpa=0
total=0
average_gpa=0
score=0
for student in range(1,students+1): 
    print("student",student)
    for subject in range(1,subjects+1):
        score=int(input("enter the score = ")) #enter 3 subject score
        total+=score #total the 3 subject score
    gpa=total/subjects  #calculate the gpa  
    total_gpa+=gpa
     
total=0
average_gpa=total_gpa/students
print(average_gpa)
