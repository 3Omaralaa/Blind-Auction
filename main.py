import art
print(art.logo)

def highest_bid(bidders):
    highest_price = 0
    winner = ""
    for name in bidders:
        price = bidders[name]
        if price > highest_price:
            highest_price += price
            winner = name
    print(f"The Highest Bid is ${highest_price}, The Winner Is {winner}")

dictionary = {}
restart = True
while restart:
    name = input("What Is Your Name? ")
    bid_price = int(input("What Is Your Bid?  $"))  # تحويل السعر لرقم
    dictionary[name] = bid_price

    other_one = input("Are there any other bidders? Type yes or no ").lower()
    if other_one == "yes":
        print("\n" * 200)
    else:
        restart = False
        highest_bid(dictionary)