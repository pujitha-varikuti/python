'''import random
me_chossing=int(input("type0:rock type1:paper type2:scissor : "))
computer_chossing=random.randint(0,2)
print("computer_chossing:")
print(computer_chossing)
if me_chossing>=3 and me_chossing>=0:
  print("you take an invalid input you see again")
elif me_chossing==computer_chossing:
    print("you are draw agian you can do this")
elif computer_chossing==0 and me_chossing==2:
    print("you win")
elif me_chossing==2 and computer_chossing==0:
elif me_chossing>computer_chossing:
        print("you lose")
elif computer_chossing>me_chossing:
        print("you lose")    
elif me_chossing>computer_chossing:
            print("you win")
else:
    print("you see again")'''
    #🪨 📃 ✂️

'''rock = '🪨'
paper = "📃"
scissors = '✂'
gameIcons = [rock, paper, scissors]
import random
choice = [0, 1, 2]
compChoice = random.choice(choice)
userChoice = int(input('What is your choice 0-rock,1-paper & 2- Scissors? '))
if userChoice < 0 or userChoice > 2:
    userChoice = int(input('Please make a valid choice.0-rock,1-paper & 2- Scissors: '))
    # To improve use loop function?
if compChoice == userChoice:
    print('You have a draw. Click to play again.')
elif userChoice == 0 and compChoice == 2:
    print('You win')
elif compChoice == 0 and userChoice == 2:
    print('You lose!')
elif compChoice > userChoice:  
    print('You lose. Click enter to play another round')
else: 
    print('You win.')
print(f'Computer chooses , {gameIcons[compChoice]}')
print(f'You choose ,{gameIcons[userChoice]}')'''
rock='🪨'
paper='📃'
scissor='✂️'
gameimages=[rock,paper,scissor]
import random
choice=[0,1,2]
computer_choice=random.choice(choice)
print("computer_choice")
print(computer_choice)
user_choice=int(input("type0:rock,type1:papaer,type2:scissor : "))
if user_choice==computer_choice:
    print("draw")
elif computer_choice>user_choice:
    print("you lose")
elif user_choice>computer_choice:
    print("you win")
else:
    print("check onnce try agian")
print(f"computer choose{gameimages[computer_choice]}")  
print(f"user chosse{gameimages[user_choice]}")      
