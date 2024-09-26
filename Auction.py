from replit import clear
from art import logo_auction as logo 

def cl_logo():
    clear()
    print(logo)

def validate_and_check(response):
    if response in ["y", "n"]:
        return False, response == "y"
    else:
        print("\nAnswer is not valid. Choose again.")
        return True, None
    

def winner(bets):
    cl_logo()
    winner = ""
    max_bid = 0
    tie_bidders = []

    for player in bets:
        bid = bets[player]
        if bid > max_bid:
            winner = player
            max_bid = bid
            tie_bidders = [player]
        elif bid == max_bid:
            tie_bidders.append(player)

    if len(tie_bidders) >1 :
        new_bets(bets, tie_bidders, max_bid)
    else:
        winner = tie_bidders[0]
        print(f"\nThe winner is {winner} with a bid of ${max_bid}")

def new_bets(bets, tie_bidders, max_bid):
    tie_bets={}
    
    for names in bets:
        bit = True
        for i in range (len(tie_bidders)):
            if tie_bidders[i] == names:
                while bit:
                    cl_logo()
                    print(f"\nIt's a tie between: {','.join(tie_bidders[:-1])} and {tie_bidders[-1]}! Let's do this again! The bid strats from: ${max_bid}\nYou can get out of auction by offering $0!")
                    price1 = int(input(f"\n{names}, what is your new bid?: $"))
                    if price1 == 0:
                        bit = False
                        print(f"\nDear {names}, thank you for participating! See you next time!")
                        input("Please press Enter!")
                    elif max_bid >= price1:
                        print(f"\nDear {names}, please offer a bit bigger that ${max_bid}")
                        input("Please press Enter!")
                    else:
                        bit = False
                        tie_bets[names] = price1
    
    winner(tie_bets)



bets= {}
auction = True

while auction:
    bet = True 
    while bet:
        cl_logo()
        print("Welcome to online PyAuction!")

        name = input("\nWhat is your name? ")
        price = int(input("What is your bid?: $"))

        bets[name] = price

        invalid_input = True
        while invalid_input:
            n = input("\nAre there any other bidders? Type 'y' for yes or 'n' for no: ")
            invalid_input, bet = validate_and_check(n) 
    
    if not bet:
        cl_logo()
        winner(bets)

    invalid_input = True
    while invalid_input:
        answer = input("\nIs there any other auction? Type 'y' for yes or 'n' for no: ")
        invalid_input, auction = validate_and_check(answer)

    if not auction:
        cl_logo()
        print("See you next time!")
