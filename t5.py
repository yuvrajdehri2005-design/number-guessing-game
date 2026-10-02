items=[]
t=0

while True:
    n = input("Enter Item name: ")
    p = int(input("Enter Price: "))
    q = int(input("Enter Quantity: "))
    total=p*q
    t= t+total
    # yahan item save karna hai
    item = {
             'name':n,
             'price':p,
             'quantity':q
           }

    items.append(item)

    choice = input("Add another? yes/no: ")

    if choice == "no":
        break


dis=int(input("enter discount%:"))
import datetime
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")

def calculate_bill(p,q):
    return p * q

discount=(t*dis)/100
final_price=t-discount

print("           +--------------------------------+")
print("           |          YOUR BILL             |")
print("           |         KIRANA STORE")
print("           +--------------------------------+")
print("           |       ===== DATE & TIME =====")
print("           |        Date:",date)
print("           |        Time:",time)
print("           |       =======================")
for item in items:

    print("           +--------------------------------+")

    print("           |Item:", item["name"])
    print("           |Price:", item["price"])
    print("           |Quantity:", item["quantity"])
    print("           |item total:", item["price"] * item["quantity"])

    print("           +--------------------------------+")

print('           |total:',t)

print('           |discount:',discount)

print('           |final price:',final_price)


print("           +--------------------------------+")
