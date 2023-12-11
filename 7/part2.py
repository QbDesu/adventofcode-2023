import sys

lines = open(sys.argv[1] if len(sys.argv)>1 else "./input.txt", "r").readlines()

HAND_TYPES = {
    "high card": 1,
    "one pair": 2,
    "two pair": 3,
    "three of a kind": 4,
    "full house": 5,
    "four of a kind": 6,
    "five of a kind": 7
}

def hand_type(hand: str) -> int:
    jokers = hand.count("J")
    if jokers==5:
        return HAND_TYPES["five of a kind"]
    
    counts = (hand.count(card) for card in set(hand.replace("J", "")))
    triples = 0
    pairs = 0
    for count in sorted(counts, reverse=True):
        count += jokers
        match count:
            case 5:
                return HAND_TYPES["five of a kind"]
            case 4:
                return HAND_TYPES["four of a kind"]
            case 3:
                triples += 1
            case 2:
                if triples == 1:
                    return HAND_TYPES["full house"]
                pairs += 1
        jokers = 0
    if triples == 1:
        return HAND_TYPES["three of a kind"]
    elif pairs == 2:
        return HAND_TYPES["two pair"]
    elif pairs == 1:
        return HAND_TYPES["one pair"]
    else:
        return HAND_TYPES["high card"]
    


hands = [line.split() for line in lines]
hands = [(hand_type(hand), hand, int(bid)) for hand, bid in hands]
hands.sort(key=lambda x: (x[0], x[1].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "0"), x[2]))

for hand in hands:
    print(f"{hand[0]}: {hand[1]}")

result = sum((idx+1)*hand[2] for idx, hand in enumerate(hands))
print(result)
