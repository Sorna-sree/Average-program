##Grade function
def grade(mark):        
    if(mark>90):
        print("A")        
    elif(mark>80):
        print("B")
    elif(mark>70):
        print("C")
    elif(mark>60):
        print("D")
    else:
        print("Fail")

##Input
mark=[]
n=int(input("enter the subject count"))
for i in range(0,n):
    mark.append(int(input("enter the mark")))

##Total
total=0
for i in range(0,len(mark)):
    total+=mark[i]
print(total)

##Grade for each subject
for i in range(0,len(mark)):
    grade(mark[i])

##Grade for Average
average=total/n
print("Average is")
grade(average)