#print the first character and last character
input_string = input("Enter the letters: ") #enther the string
word = " " 
last_index = (len(input_string) - 1)
for index in range(0, len(input_string)):
    if(index < last_index):
        word =word+input_string[index] + input_string[last_index] 
        last_index =last_index- 1
print("Answer: ",word)