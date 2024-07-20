import random
def guess_numbers():
  while True:
    target_number = random.randint(1, 100) #makes the computer choose a number between 1 and 100 (technically 1-99)
    attempts = 1
    
    print('Welcome to the guessing game.')
    number_of_guesses = int(input('Enter the number of guesses you wish to have: '))
    if number_of_guesses > 20:
      print(f"REALLY? you're THAT unlucky?! fine man... {number_of_guesses} number of guesses it is.")

    print(f'guess a number between 1 and 100. you have {number_of_guesses} attempts left.')

    while attempts <= number_of_guesses:
      guess = int(input("Enter your guess: "))
    #   if guess == ' ': ## will update later to see how this can work
    #     print('Do you hate yourself to not even have the dignity to choose ANY number?') 
      
      if guess == target_number:
        print(f"Congratulations! you've guessed the correct number at your {attempts} attempt!")
        break
      elif guess < 1 or guess > 100:
        print('between 1 and 100 please. stop being an idiot? Have some mercy on yourself? Please? Thanks?')
        print(f'You also just wasted an Attempt. you are on your {attempts} attempt right now.')
      elif guess < target_number:
        print(f'try higher! you are at your {attempts} attempt.')
      elif guess > target_number:
        print(f'try lower! you are at your {attempts} attempt.')

      if attempts == number_of_guesses -1:
        print('Be quick! you only got 1 guess left!')
        
        
      if attempts == 15:
        print('Quick! only 5 attempts left!')
            
      attempts +=1
      
    if attempts == number_of_guesses:
      print(f"Sorry you've reached the maximum amount of attempts. the correct answer was {target_number}!")

    play_again = input('Do you want to play again? (yes or no): ')
    if play_again != 'yes':
      break
    else:
      guess_numbers()
    
      
guess_numbers()


###########################################
# add more difficulty levels: difficulty_level = input('Enter your difficulty level (easy, medium, hard): ')
