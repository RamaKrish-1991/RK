import random
games=''
while games=='':
    try:
        games=int(input("How many games would you like to play"))
    except:
        print("Please enter a number")
for game in range(0,games):
    pick=random.randint(1,26)
    guess=None
    attempts=0
    while pick!=guess:
        try:
            guess=int(input("Enter a number"))
        except:
            print("Please enter a number")
            continue
        if guess!=pick:
            attempts+=1
            if guess>pick:
                print("Too High")
            else:
                print("Too Low")
        else:
            print("Correct! It took %s attempts",attempts)