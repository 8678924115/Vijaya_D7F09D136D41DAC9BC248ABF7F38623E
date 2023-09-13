#Leap year

"""
year% 4==0&
year% 100! =0/
year@0=0

"""
def isLeapYear(year):
  if(year% 4==0):
    return True
  else:
    return False 

year=2017
if isLeapYear(year):
  print('{} is a leap year.'.format)
else:
  print('{} is not a leap year. '.format(year))





