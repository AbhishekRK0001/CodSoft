import random

choices = ["rock", "paper", "scissors", "rr", "ss", "pp"]

mapping = {"rr": "rock", "ss": "scissors", "pp": "paper"}

def play():
    while True:  
        goal = int(input("\n Please set the winning score (e.g., 3, 5, 10): "))
        user_points = 0
        comp_points = 0
        
        while True: 
            user = input("\nChoose rock[rr], paper[pp], or scissors[ss] \\[(q to quit)]// : ").lower()
            
            if user == 'q':
                print("Game's over ! Final Score ===> You:", user_points, "| Computer:", comp_points)
                return 
            
            if user in mapping:
                user = mapping[user]

            if user not in ["rock", "paper", "scissors"]:
                print("\n Already fumbling, got scared🫵🤣 ")
                continue

            comp = random.choice(["rock", "paper", "scissors"])
            print("Computer chose:", comp)

            if user == comp:
                print("Never mind, it's a tie! \n")
            
            elif (user == "rock" and comp == "scissors") or \
                 (user == "paper" and comp == "rock") or \
                 (user == "scissors" and comp == "paper"):
                print("You win this round!\n")
                user_points += 1
            else:
                print("Looser Looser hahaha 🤣 \n")
                comp_points += 1

            print(f"Score => You: {user_points} | Computer: {comp_points}")

            if user_points >= goal:
                print(f"\n🎉 Congrates! You Win {goal}, but i did'nt lose ")
                break
            elif comp_points >= goal:
                print(f"\n💀 Computer reached {goal} points. You lost! 💀")
                break

        again = input("\nUp for another round ??(y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

play()
