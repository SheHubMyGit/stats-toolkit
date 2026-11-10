
def mean(values):
  """Returns the quotient of the sum of all the numbers in a non-empty list divided by the number of components in the list"""
  if len(values)==0:
    raise ValueError("mean of 0 numbers cannot be found")
  sum = 0
  for num in values:
    sum = sum + num
  return sum/len(values)

def median(values):
  """Returns the median of a non-empty list"""
  if len(values) == 0:
    raise ValueError("at least 1 number is required to determine median")
  v = sorted(values)
  if len(v)%2 == 0:
    md = (v[(len(v)//2)-1] + v[len(v)//2])/2
  else:
    md = v[len(v)//2]
  return md

def sqrt(values):
  """Returns the square root of a number"""
  s = values**0.5
  return s

def std_dev(values):
  """Returns the sample standard deviation from a list of more than 2 numbers"""
  total = 0
  if len(values) < 2:
    raise ValueError("std_dev needs more than 1 data point to measure spread")
  m = mean(values)
  for num in values:
    total = total + (num-m)**2
  return sqrt(total/(len(values)-1))

def to_number(values):
  """Returns the float value of a number. If it is unable to do so, it will return none"""
  try:
    return float(values)
  except ValueError:
    return None

def is_valid_score(value):
  """" Checks if a score is possible in a 0-100 grading scale"""
  if 0<=value<=100:
   return True
  else:
    return False
