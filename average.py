number=int(input("Enter the number = ")) # get the input to the user
count=0   #set the count value is 0
sum=0    #set the sum value is 0
average=0  #set the avarage value is 0
while(number>0):
    count+=1   #count the user input values
    sum+=number #sum  the values
    number=int(input("Enter the number = ")) #get the input to the user
average=sum/count  #calculte the avarage value
print(average)    #print the average value
