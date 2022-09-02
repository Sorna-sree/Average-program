#print the letters in btwn first a and last a 
input_string = input("enter the string: ") #input string
first_a=0 
last_a=0
for index in range(0,len(input_string)): #find the index of first a
    if(input_string[index] == 'a'):
        first_a=index
        break
for index in range((len(input_string) - 1),-1,-1): # find the index of last a 
    if(input_string[index] == 'a'):
        last_a=index
        break  
for index in range((first_a+1),last_a): #print the  letter btwn first and last a
    print(input_string[index])
    