prices_stock={
0:{
    'shirt':10, 
    'trouser':60, 
    'skirt':70, 
    'gown': 80, 
    'suit':90, 
 },
1:{
    'shirt':5, 
    'trouser':6, 
    'skirt':7, 
    'gown': 8, 
    'suit':9, 
}
}
total=0
while True:
    print('Press 1 to see the list of Shirt')
    print('Press 2 to shop')
    print('Press 3 to Exit!')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print ("options of shopping are")
        print(prices_stock[0].values())
        print ("options of prices are")
        print(prices_stock[0].items())
        print ("options of stocks are" )
        print(prices_stock[1].items())
    elif choice==2 :
        dress= input('What do you want to buy: ')
        if dress =="shirt":
            if prices_stock[0]["shirt"]>=1:
                print(" item is added in bucket")
                n=prices_stock[0]["shirt"]
                n=n-1
                a=prices_stock[1]["shirt"]
                prices_stock[0]["shirt"]=n
                print(prices_stock[0])
            else:
                print("not in Stock")
        if dress =="trouser":
            if prices_stock[0]["trouser"]>=1:
                print(" item is added in bucket")
                m=prices_stock[0]["trouser"]
                m=m-1
                prices_stock[0]["trouser"]=m
                print(prices_stock[0])
            else:
                print("not in Stock")
        if dress =="skirt":
            if prices_stock[0]["skirt"]>=1:
                print(" item is added in bucket")
                o=prices_stock[0]["skirt"]
                o=o-1
                prices_stock[0]["skirt"]=o
                print(prices_stock[0])
            else:
                print("not in Stock")
        if dress =="gown":
            if prices_stock[0]["gown"]>=1:
                print(" item is added in bucket")
                p=prices_stock[0]["gown"]
                p=p-1
                prices_stock[0]["gown"]=p
                print(prices_stock[0])
            else:
                print("not in Stock")
        if dress =="suit":
            if prices_stock[0]["suit"]>=1:
                print(" item is added in bucket")
                q=prices_stock[0]["suit"]
                q=q-1
                prices_stock[0]["suit"]=q
                print(prices_stock[0])
            else:
                print("not in Stock")
    elif choice == 3:
        break