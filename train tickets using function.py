one_way_ticket=1000
retrun_ticket=1750
total=0
def train_ticket():
    person_input=int(input("Enter the no_of person: "))
    senier_person=int(input("enter the senior person count"))
    count1=0 #for using return ticket
    count2=0 # for using one way ticket
    for i in range(person_input):
        ticket_want=input(("do you want return ticket ans yes or no")) 
    if(ticket_want=="yes"):
        count1+=1  #count the return ticket
    else:
        count2+=1 # count the one way ticket
        total+=one_way_ticket*count2+retrun_ticket*count1
    if(person_input>=4):
        total+=total-total*20/100
    if(senier_person>0 and count1>0):
        total+=retrun_ticket*senier_person-total*50/100
    elif(senier_person>0 and count2>0):
        total+=one_way_ticket*senier_person-total*50/100

    print(total)
train_ticket()

    