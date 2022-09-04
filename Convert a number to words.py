# Global Array storing word for each digit
import webbrowser


words = ['zero','one','two','three','four','five','six','seven','eight','nine']
 
def number_to_word(n):
 
    # If all the digits are encountered return blank string
    if(n==0):
        return ""
     
    else:
        # compute spelling for the last digit
        small_ans = words[n%10]
 
        # keep computing for the previous digits and add the spelling for the last digit
        ans = number_to_word(int(n/10)) + small_ans + " "
     
    # Return the final answer
    return ans
 
n = int(input("enter the number:"))
print("Number Entered was : ", n)
print("Converted to word it becomes: ",end="")
print(number_to_word(n))
