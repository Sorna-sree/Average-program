coffee_rate=100
Vadai_rate=100
Sandwich_rate=200
Coke_rate=60
offer_coffee_rate=50
total=0
discount=0
coffee=int(input("enter the no of coffee:"))
Vadai=int(input("enter the no of Vadai:"))
Sandwich=int(input("enter the no of sandwich:"))
Coke=int(input("enter the no of Coke:"))
if(Sandwich>1 or Vadai>2):
 total+=(offer_coffee_rate*coffee+Vadai_rate*Vadai+Sandwich_rate*Sandwich+Coke_rate*Coke)
elif(coffee==1 and Vadai==1 and Sandwich==1 and Coke==1):
    total+=(coffee*coffee_rate+Vadai*Vadai_rate+Sandwich*Sandwich_rate+Coke*Coke_rate)
discount=(total-(total/10)2)
print("total",total)
if(total>1000):
    total=(total-(total/10)2)
    print("total",total)
else:
   print("total",discount)    
    
    
    

    

 