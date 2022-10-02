one_way_ticket = 1000
retrun_ticket = 1750
total=0
print("60 above is senier age")
person_input = int(input("Enter the no_of person: "))
senier_person = int(input("enter the senior person count: "))
discount_count = person_input - senier_person 
count1=0 #for using return ticket
count2=0 # for using one way ticket
def train_ticket(discount_count):
    for i in range(discount_count):
        ticket_want=input(("do you want return ticket ans yes or no: ")) 
        if(ticket_want== "yes"):
            count1+=1  #count the return ticket
        else:
            count2+=1 # count the one way ticke 4
    total+=one_way_ticket*count2+retrun_ticket*count1
    if(discount_count>=4):
     total+=total-total*20/100 #calculate the 20% discount
     return total

def senior_ticket_calculation():
    if(senier_person>0 and count1>0):
        total+=retrun_ticket*senier_person-total*50/100 #calculate the senior person return ticket amount
    elif(senier_person>0 and count2>0):
      total+=one_way_ticket*senier_person-total*50/100 #calculate the senior person one way ticket amount
    return total
print(total)
train_ticket(discount_count)
senior_ticket_calculation()   
    