#taking information

name=input('tumhara name kya hai? =')
clas=input('tum kon se class me padhte ho? =')
age=int(input('tumhara age kitna/kitni hai? ='))

hindi=int(input('tumhare hindi mein kitne marks hai? ='))
english=int(input('tumhare english me kitne marks hai? ='))
math=int(input('tumhare maths me kitne marks hai? ='))
social=int(input('tumhare social science me kitne marks hai? ='))
science=int(input('tumhare science me kitne marks hai? ='))

# main calculator

mark=(hindi+english+math+social+science)/5

if mark>= 90:
   print('EXCELLENT,hats off to you💯')
   print(mark)

elif mark>= 80:
     print('very good👍')
     print(mark)

elif mark>= 60:
     print('good✅')
     print(mark)

elif mark< 60:
     print('need improvement📖📚')
     print(mark)
else:
    print('wrong imformation,please try again!')





