#odd  index characters
input_string= input("enter the characters:  ")
print("odd characters: ")
for index in range(0,len(input_string)):
    if(index % 2 != 0):
        print(input_string[index])

#even index characters
print("even characters: ")
for index in range(len(input_string)-1,-1,-1):
    if(index % 2 ==0):
        print(input_string[index])
   