def weight_on_planets():
   # write your code here

   #weight is an integer to be input by the user
   weight = int(input('What do you weigh on earth? '))

   print('\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds.' % ((weight * 0.38),(weight * 2.34)))

if __name__ == '__main__':
   weight_on_planets()
