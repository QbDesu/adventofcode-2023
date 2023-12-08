lines = open("./input.txt", "r").readlines()

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
    pairs = 0
    triples = 0
    for card in set(hand):
        match hand.count(card):
            case 2:
                if triples == 1:
                    return HAND_TYPES["full house"]
                elif pairs == 1:
                    return HAND_TYPES["two pair"]
                pairs += 1
            case 3:
                if pairs == 1:
                    return HAND_TYPES["full house"]
                triples += 1
            case 4:
                return HAND_TYPES["four of a kind"]
            case 5:
                return HAND_TYPES["five of a kind"]
    if triples == 1:
        return HAND_TYPES["three of a kind"]
    elif pairs == 1:
        return HAND_TYPES["one pair"]
    else:
        return HAND_TYPES["high card"]

hands = [line.split() for line in lines]
hands = [(hand_type(hand), hand, int(bid)) for hand, bid in hands]
hands.sort(key=lambda x: (x[0], x[1].replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W"), x[2]))

result = sum((idx+1)*hand[2] for idx, hand in enumerate(hands))
print(result)
