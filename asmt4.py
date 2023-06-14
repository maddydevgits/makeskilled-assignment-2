try:
  a=int(input('enter a value '))
  b=int(input('enter a value '))
  a=a/b
  print(a)
except ValueError:
  print("non-integer value")
except ZeroDivisionError:
  print('please enter non zero values')
finally: 
    print('exceuted all the times')