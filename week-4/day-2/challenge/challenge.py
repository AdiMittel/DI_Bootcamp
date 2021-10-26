date_birth =input('Enter date of birth DD/MM/YYYY: ')
date_list = date_birth.split('/')
years = int(date_list[-1])
age = 2021-years

year_last_num = age % 10 

# print(candle)
candle = '__' + 'i'*year_last_num + '__'


cake = f'''
         {candle}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~ 
'''
print(cake)