def bmi():
  height_m = float(input('Enter you height in meters: '))
  weight_kg = int(input('Enter you weight in kg: '))
  bmi = weight_kg / (height_m ** 2)
  
  if bmi < 25:
    print(f'your bmi is {bmi}, which means that you are not overweight.')
  else: 
    print(f'your bmi is {bmi}, which means that you are overweight.')

bmi()


# Add-Ons for later:  what should be the optimal weight for the desired height

