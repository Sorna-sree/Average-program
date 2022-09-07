fruits = ['apples','oranges','bananas']
required = False
order = " "
quantity = " "
supply = ['one','two','three','four','five','six','seven','eight','nine']
for menu in range(0,len(fruits)):
    print('Nine ',fruits[menu]," Available")
answer = input("what do you want to buy:")
answer = answer.split() #i want apples it is used for split the answer
for buy in range(0,len(answer)): 
    if(answer[buy] in fruits): #find the what fruit buy
        order += answer[buy] + ' '
    if(answer[buy] in supply): #find how may fruit buy
        quantity += answer[buy] + ' '
        required = True
if(required == False):
    quantity += input("how many you want: ") 
    if(quantity not in supply):
        quantity = ""
        print("Not Available Please Enter Below: ")
        quantity += input("how many do you want : ")
order = order.split()
quantity = quantity.split()
print("customer ordered")
for i in range (0,len(quantity)):
    print(quantity[i],' ',order[i])