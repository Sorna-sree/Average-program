food_items = [ "idly" , "poori" , "vadai" , "pongal", "dosai" ] # food items for cafe
price_of_items = [ 5 , 10 , 5 , 40 , 30 ]  #price of those items
supply_of_items = [5 , 5 , 5 , 5 , 5]  #supply of those items
total_price_of_items = 0
maximum_transaction = 10
total_sale_of_the_day=0
for quantity in range (0,len(food_items)):
    print(food_items[quantity] +  " price: " + str(price_of_items[quantity]) + " supply of items: " + str(supply_of_items[quantity])) #display the manu card
for customer in range (0,maximum_transaction): #10 transaction
    for order in range(0,len(food_items)):
     if(supply_of_items[order]>0):
        customer_order = int(input(" How Many " + str(food_items[order]) +  " do you want:  "))
        total_price_of_items =total_price_of_items + (price_of_items[order]) * (customer_order)   #calculate total price of item
        supply_of_items[order]-=customer_order
     else:
         print("nil")
         
    print(supply_of_items)                                                            
    print("customer  buys "  "Rs"+str(total_price_of_items))
total_sale_of_the_day =total_sale_of_the_day+ total_price_of_items   #calculate the total sale of the day           
print("Total sales of the day: ",total_sale_of_the_day) 
