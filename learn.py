print("welcome to bill calculator")
bill = float(input("enter bill : "))
split = int(input("bill splitting :"))
tip = int(input("10 or 20 :"))
total_bill = bill / split
print("total bill without tip")
print(total_bill)
total_billl = (bill / split) + tip
print("total bill with tip")
print(total_billl)
