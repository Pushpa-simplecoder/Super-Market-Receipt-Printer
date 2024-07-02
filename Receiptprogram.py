import datetime
n=int(input("Enter no.of product"))
ammount=0
products=[]
for i in range(n+1):
    name=input("Enter product:")
    qty1=int(input("enter qty:"))
    pr=int(input("enter price:"))
    products.append((name, qty1, pr))
market="SRITHARA"
width=50
centerd_marked=market.center(width)
print(centerd_marked)
res=datetime.datetime.now()
datetime = res.strftime("%Y-%m-%d %H:%M:%S")
width=50
centerdt=datetime.center(width)
print(centerdt)
receipt="CASH RECEIPT"
width=50
center_receipt=receipt.center(width)
print(center_receipt)
print(f"{'Product Name':<20}{'Quantity':<20}{'Price':<20}")
print("-"*50)
for product in products:
    print(f"{product[0]:<20}{product[1]:<20}{product[2]:<20}")
print("-"*50)
amount = 0
for product in products:
    amount += product[1] * product[2]
total=f"TotalAmmount:{amount}"
width=40
center_total=total.center(width)
print(center_total)
visiting="THANK YOU FOR VISTING!!"
width=40
center_visiting=visiting.center(width)
print(center_visiting)
visit="VISIT AGAIN 😊 😊 "
width=40
center_visit=visit.center(width)
print(center_visit)

    





