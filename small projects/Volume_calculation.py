length = float(input('Enter the length of the triangle: '))
width = float(input('Enter the width of the triangle: '))
height = float(input('Enter the height of the triangle: '))

volume1 = int(length * width * height)

print(volume1)

if volume1 > 0:
  
  length1 = float(input('Add a different value: '))
  width2 = float(input('Add a different value: '))
  height2 =float(input('Add a different value: '))
  
  volume2 = int(length1 * width2 * height2)
  
  print(volume2)
  
if volume1 and volume2 > 100:
  print(volume1 + volume2)
else: 
  print('sorry its not possible')


# 