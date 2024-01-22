name=(input("enter the name! >> "))

answer_yes = ["Yes","YES", "Y", "yes", "y",]
answer_no = ["No","NO", "N", "no", "n"]
drive = ["D", "DRIVE", "Drive", "d", "drive"]


print(f"""\n
    WELCOME {name}!\n                   LET'S START THE ADVENTURE!
    
    
    You are going home in your car when you see a woman in dirty clothes running towards you and asking for a ride home.
    
    will you give her a ride a home. (Yes / No)
        \n""")


ans1 = input("Enter Yes or No >> ")

if ans1 in answer_yes:
    print("\nAfter 5 minutes, you are stopped at a checkpoint and police asks you if you seen a suspicious woman. will you say (Yes / No)\n")

    ans2 = input("\nEnter Yes or No >> ")

    if ans2 in answer_yes:
        print("\nYou are an honest person. She was a murderer & You won the Game\n")

    elif ans2 in answer_no:
        print("\nYou helped a murderer. Now, go to jail. GAME OVER\n")

    else:
        print("\nYou typed the wrong input. GOODBYE\n")




elif ans1 in answer_no:
    print("\nNow, She is trying to kill you. will, you knock her down? (Yes / No / Drive)\n")

    ans3 = input("\nEnter Yes or No >> ")

    if ans3 in answer_no:
        print("\nSorry! You are dead. She was a murderer & She killed you. GAME OVER")

    elif ans3 in answer_yes:
        print("\n  Congrates! She was a murderer & You helped the poilce to catch her with you bravery.")




    if ans3 in drive:
        print("\n you drove the car, after 5 min, you are stopped at a checkpoint and police asks you if you seen a suspicious woman. will you say (Yes / No)\n ")
        ans4 = input("\nEnter Yes or No >> ")


        if ans4 in answer_yes:
            print(f"\n Congrates!{name} She was a murderer & You helped the poilce to catch her with you bravery.")

        elif ans4 in answer_no:
            print(f"\nSorry {name} You helped a murderer. Now you go to jail. GAME OVER")

