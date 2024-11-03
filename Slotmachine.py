import random


symbols = ["A", "B", "C", "D"]
payouts = {"A": 10, "B": 5, "C": 3, "D": 2}


balance = 100

while True:
    print(f"Current balance: ${balance}")
    if input("Press enter to play (q to quit): ").lower() == "q":
        break

    bet = int(input("Enter your bet amount: $"))
    if bet > balance:
        print("Insufficient balance!")
        continue

    
    balance -= bet

    
    reels = [random.choice(symbols) for _ in range(3)]
    print(" | ".join(reels))

    
    if reels[0] == reels[1] == reels[2]:
        win = payouts[reels[0]] * bet
        print(f"You won ${win}!")
        balance += win
    else:
        print("No win this time.")


print(f"Thanks for playing! Your final balance is ${balance}")




















