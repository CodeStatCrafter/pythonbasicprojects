print("welcome to the bill splitter")
bill = float(input("enter the bill: "))
tip = int(input("how much would you like to give as tip 10 or 15: "))
contr = int(input("bill splitting with: "))
if tip == 10 or tip == 15 :
    print("bill with tip ")
    print((bill+(bill*(tip/100))))
else:
    print("bill without tip")
    print(bill/contr)
