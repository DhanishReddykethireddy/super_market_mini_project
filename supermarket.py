# '''
# write a python program to generate a bill for a super market purchase.the program should store the items
# and their prices in a list of tuples.it should then iterate over this list to print out each item along with its 
# price .finally calculate and print the total cost of all the items.
# '''
# name=input("Enter the name:").capitalize()
# supermarketname='DSUNIVERSE'
# place='PULIVENDULA'
# mobilenumber=int(input("Enter your mobile number:"))
# #products in supermarket
# products='''
# rice=45rs/kg
# sugar=30rs/kg
# oreobiscuits=20rs
# milk=75/litre
# coffe_powder=50rs/pack
# '''
# #declaration
# price=0
# pricelist=[]
# totalprice=0
# finalprice=0
# itemlist=[]
# quantitylist=[]
# plist=[]

# #products and their prices in dictionary
# product={'rice':45,'sugar':30,'oreobiscuit':20,'milk':75,'coffe_powder':50}
# while True:
#     option=int(input("choose the option 1 for products and 2 for exit:"))
#     if option==2:
#         print(f'thank you for coming into our supermarket {supermarketname}')
#         break
#     elif option==1:
#         print(products)
#     while True:
#         option=int(input('choose 1 for buy and 2 for exit:'))
#         if option==2:
#             print("Thanks for coming and making shopping")
#             print("please do visit again for better experience")
#             break     
#         elif option==1:
#             item=input('enter the product:').lower()
#             while True:
#                 quantity=input('enter the quantity:')
#                 if quantity.isdigit():
#                    quantity=int(quantity)
#                    break
#                 else:
#                  print('please enter valid quantity')   
#         if item in product:
#             price=quantity*product[item]
#             pricelist.append((item,quantity,product[item],price))
#             totalprice += price
#             itemlist.append(item)
#             quantitylist.append(quantity)
#             plist.append(price)
#         else:
#           print(f'the item {item} that you are searching is not available')
        
# if totalprice > 0:
#     tax=(totalprice*8)/100
#     finalamount=tax+totalprice 
#     print("="*58)
#     print(f'='*22,supermarketname,"="*22)
#     print(f' '*22,place,' '*22)
#     print("="*58)
#     print(f'name:',name," "*20,"mobilenumber:",mobilenumber)
#     print("="*58)
#     print("s.no"," "*10,"item"," "*10,"quantity"," "*10,"Price",) 
#     for i in range(len(pricelist)):
#         print(i,13*' ', itemlist[i], 13*' ',quantitylist[i], 13*' ',plist[i])
#     print("="*58)
#     print(f"total amount"," "*39,totalprice)
#     print("tax amount",35*" ",'Rs',tax)
#     print("="*58)
#     print(" "*33,"Final amount","Rs",finalamount)
#     print("="*58)
#     print(" "*20,"Thank you & Visit again")
#     print("="*58)
 
name=input("Enter the name:")
mobilenumber=int(input("enter mobile number:"))
supermarketname='BHANU PRAKASH SUPER MARKET'
place='PULIVENDULA'
#items in supermarket
product='''
dairymilk=5rs/chocolate/piece
balckcurrenticecream=50rs
watermelonseeds=90rs
wheatflour=70rs/kg
sugar=80rs/kg
magnum=15rs/piece
maaza=90/litre
lays=15rs/175grams
surfexcel=10rs/pack
honey=98/bottle
'''
price=0
totalprice=0
fianlprice=0
pricelist=[]
productslist=[]
quantitylist=[]
prlist=[]
#items and cost
products={'dairymilk':5,
         'blackcurrenticecream':50,
         'wheatflour':70,
         'watermelonseeds':90,
         'sugar':80,
         'magnum':15,
         'maaza':90,
         'lays':15,
         'surfexcel':10,
         'honey':98       
}
while True:
    choice=int(input('choose 1 for prodcuts and 2 for exit:'))
    if choice==1:
        print(product)
    elif choice==2:
        print('thanks for coming and purchasing')
        break
    while True:
        choice=int(input('choose 1 for buy and 2 for exit:'))
        if choice==1:
            product=input("choose the product:").lower()
            while True:
                quantity=input("enter the quantity:")
                if quantity.isdigit():
                   quantity=int(quantity)
                   break
                else:
                    print('please enter quantity in numbers')
        elif choice ==2:
            print('thanks for coming and purchasing')
            break
        
        if product in products:
            price=quantity*products[product] 
            pricelist.append((product,quantity,products[product],price))
            totalprice+=price
            productslist.append(product)
            quantitylist.append(quantity)
            prlist.append(price)
        else:
            print(f'the product {product} that you are searching is not available')
            print(f'sorry for inconvenience we will maintain that {product} soon')
            
if totalprice>0:
    tax=(totalprice*10)/100
    finalprice=tax+totalprice
    print("-"*58)
    print(f' '*22,supermarketname,' '*22)
    print(f' '*28,place,' '*18)
    print("-"*58)
    print(f'Name:',name,' '*15,'mobilenumber:',mobilenumber)
    print("="*58)
    print('S.no'," "*5,'itemname',' '*10,'quantity',' '*10,'price')
    print("="*58)
    for k in range(len(pricelist)):
        print(k,' '*5,productslist[k],' '*18,quantitylist[k],' '*17,prlist[k])
    print("-"*58)
    print(f' '*30, 'totalamount:',totalprice)
    print(' '*30,'taxamount',tax)
    print('-'*58)
    print(' '*30,'finalprice',finalprice)
    print('-'*58)
    print(' '*20,'Thank you and visit again')
    print('-'*58)
    
    
    
    
            
            
            
    
            
            