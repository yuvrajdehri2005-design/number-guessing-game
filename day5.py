

#taking input

name=input('what is your name? :')
clas=input('In which class you are studiying? :')
hindi=int(input('how many marks do you get in hindi? :'))
english=int(input('how many marks do you get in english? :'))
maths=int(input('how many marks do you get in maths? :'))
social=int(input('how many marks do you get in social science? :'))
science=int(input('how many marks do you get in science? :'))


#result seting


if hindi>100:
   print('invalid marks!')
   exit()
elif english>100:
     exit('invalid marks!')

elif maths>100:
     exit('invalid marks!')

elif social>100:
     exit('invalid marks!')

elif science>100:
     exit('invalid marks!')

elif hindi<33:
     print('you are fail in, hindi!')
     exit('you are fail')

elif english<33:
     print('you are fail in, english!')
     exit('you are fail')

elif maths<33:
     print('you are fail in, maths!')
     exit('you are fail')

elif social<33:
     print('you are fail in, social sceince!')
     exit('you are fail')

elif science<33:
     print('you are fail in, science!')
     exit('you are fail')


#main program
marks=(hindi+english+maths+social+science)/5

#output seting

if marks>=90:
   print('EXCELLENT💯,you got A+🔥')
   print('congratulations,you got',(marks),'percent in your exam')

elif marks>=75:
     print('very good👍')
     print('congratulations,you got',(marks),'percent in your exam')

elif marks>=50:
     print('good👍,but you can do better')
     print('congratulations,you got',(marks),'percent in your exam')

elif marks<50:
     print('you need to improve, try for your best')
     print('you got',(marks),'percent in your exam')

