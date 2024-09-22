import random
choice=random.choice(['rock','paper','sissors'])
user=input('Type to select rock,paper or sissors: ')
print('I: ',choice)
print('YOU: ',user)
if choice==user:
    print('TIE')
elif user=='rock':
    if choice=='paper':
        print('I WIN')
    else:
        print('YOU WIN')
else:
    if choice=='sissor':
        print('I WIN')
    else:
        print('YOU WIN')


