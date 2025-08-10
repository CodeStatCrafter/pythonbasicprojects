rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock,paper,scissors]
import random
choice = int(input("what do you choose 0 for rock or 1 for paper or 2 for scissors"))
print(images[choice])
print(f"you choose{choice}")
comp_choice = random.randint(0,2)
print(images[comp_choice])
print(f"computer choose{comp_choice}")
if choice == 0 and comp_choice==2:
    print("you win")
elif choice == 2 and comp_choice==0:
    print("you loose")
elif comp_choice>choice:
    print("you loose")
elif comp_choice == choice:
    print("draw")
elif choice>=3:
    print("inavlid move")
