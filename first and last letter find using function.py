#find the first and last lattter and print the between two letter
input_string=(input("Enter the string:")) 
start=0
end=0
output=""
def characters(start,end,output): #function defenition
    character=(input("enter the character:"))
    for index in range(0,len(input_string)): #find the first character index
        if(input_string[index]==character):
            start=index
            break
        
    for index in range(len(input_string)-1,start,-1): #find the second character index
        if(input_string[index]==character):
            end=index
            break
        
    for letter in range(start+1,end): 
        output+=(input_string[letter])    
    return output   
print(characters(start,end,output)) #function call and print the character

        