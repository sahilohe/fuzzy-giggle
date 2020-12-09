#Rock Paper Scissors Game

import random 
from PIL import Image

choices = ['Rock', "Paper", 'Scissors']

guess = random.choices(choices)
print(guess)

if guess == ['Paper']:

    img = Image.open('img/paper.png')
    img.show()

elif guess == ['Rock']:

    img = Image.open('img/rock.png')
    img.show()

elif guess == ['Scissors']:

    img = Image.open('img/scissors.png')
    img.show()

else:
    print("Something went Wrong")
    exit()
