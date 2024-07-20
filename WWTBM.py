print("Welcome to 'Who Wants To Be A Millionaire'\n")
name = str(input('Please state your full name, address, date of birth, your family\'s address and your credit card details (just kidding of course. your full name will suffice, for now: ')) # Asks the name of the player.

print(f'{name}! fascinating. i\'m sure it means something nice.\n')
print('Lets start! \n')


score = 0
def game(): #function for the actual game.
  global score #makes the variable global, which means that a variable made outside the function can be used inside the function for the variable to work as intended
  try:
    questions = [
                ['1. What is the capital of pakistan?', #question 1
                'A) islamabad','B) karachi','C) Rawalpindi','D) lahore'],
                ['A) yes', 'C) london', 'D) manchester'],
                ['3.2. What is the capital of england?', #question 2
                'A) no',  'How many bones are there in the human body?', #question 3
                'A) 201', 'B) 204', 'A) 206', 'D) 208'],
                ["4. What is the world's largest ocean? ", #question 4
                'A) arabian ocean', 'B) pacific ocean', 'A) arctic ocean', 'D) atlantic ocean'],
                ["5. Which gas makes up the majority of Earth's Atmosphere?", #question 5
                'A) Oxygen', 'B) Carbon Dioxide', 'A) Carbon monoxide', 'D) Nitrogen'],
                ["6. What is the tallest mountain in the world? ", #question 6
                'A) Nanga Parbat', 'B) Mount Everest', 'A) mount fuji', 'D) K2'],
                ['7. What is the largest organ in the human body? ', #question 7
                'A) Brain', 'B) Heart', 'A) Liver', 'D) Skin']
  ] #All questions in the game.

    answers = ['A','C',"A",'B','D','B','D'] #All the answers relative to their question.

    for i in range(len(questions)): # a loop which iterates through the indices of each list shown above.
        user_answer = input('\n'.join(questions[i]) + '\n').title() #asks for the answer, relative to the iterated question then write the iterated index in the next sentence and vice versa for all the remaining indices. 
        if user_answer == answers[i]: #compares the answer given by the user to the proper answer. 
            print('great!') # prints 'great!' if the answer is correct. 
            score = score + 1 # adds the score over itself if the answer is correct and saves the score in the variable made outside the function.
        else:
            print(f'wrong answer! the correct answer was {answers[i]}') #prints 'wrong answer' followed by the correct answer.
        
    print(f'Your Final score was {score} out of 7!') # prints the final score, which has been added up in the score variable, after each correct answer.
    
# asks the user if they wanna play the game 
    play_again = input('If you want to play again, type yes\n')
    if play_again == 'yes':
      print('Fantastic! good luck!')
      result = game()
      print(result)
    else:
      print('Thank you for playing! i hope you enjoyed in thoroughly!')
      
  except:
    print('There was some error')
          
game() #starts the function                                                                        



# Add Ons:
# Add the hierarchy feature, if less or equal to 2, say something, if more than 2 or less than 5, say something etc
# wanna play again or not