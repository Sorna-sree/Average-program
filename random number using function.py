import random
input_number=(int(input("enter the number: ")))
random_number=0
def random_num():
    for i in range(1,100):
        random_number=random.randint(1,100)
        if(random_number%input_number==0): #check the random number is divisible by input number
            print(random_number)
            
random_num()

