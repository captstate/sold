while True:
  
  correct_password = 'mouse'
  number_of_guesses = int(input('Enter the amount of guesses you want to have: '))

  
  while number_of_guesses > 0:
    user_password = input('Enter your password: ')
    
    if user_password == correct_password:
      print('Access granted!')
      break
    else:
      print('access denied.')
      number_of_guesses -= 1
      print(f'your have {number_of_guesses} attempts left.')
      if number_of_guesses == 0:
        print(f'sorry! better left next time.')
        
#
  again = input('Do you want to play again? (yes/no): ')
  if again.lower() != 'yes':
    break        

