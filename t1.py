numbers=[]
even=0
odd=0
n=int(input("how may number do you want?:"))
for i in range(n):
    num = int(input("Enter number: "))

    numbers.append(num)
    if num%2 ==0:
       even=even+1
    elif num%2 !=0:
         odd=odd+1

print('sum of all numbers:',sum(numbers))
print('maximum of all numbers:',max(numbers))
print('minimum of all numbers:',min(numbers))
print('average of all numbers:',sum(numbers)/(len(numbers)))
print('number of even numbers:',(even))
print('number of odd numbers:',(odd))



