from turtle import width
def pattern(width):
    for i in range(width): #used to row
        for j in range(width):#used to coll
            if(i==0 or i==width-1 or j==0 or j==width-1):
                print(' * ',end='')
            else:
                print('   ',end='')
        print("")
width=int(input("enter the width of the square "))
pattern(width)