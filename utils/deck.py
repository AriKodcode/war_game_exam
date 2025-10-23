# H = heart לב
# C = club תלתן
# D = dimond יהלום
# S = spade עלה

def create_card(rank: str, suite: str) -> dict:
    result = {"rank": rank, "suite": suite, "value": 0}
    if rank.isdigit():
        rank = int(rank)
        if 1 < rank < 11:
            result["value"] = rank
            return result
    elif rank == "J":
        result["value"] = 11
        return result
    elif rank == "Q":
        result["value"] = 12
        return result
    elif rank == "K":
        result["value"] = 13
        return result
    elif rank == "A":
        result["value"] = 14
        return result
    return result


# p1 = create_card("5","S")
# p2 = create_card("3", "D")

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    win = ""
    if p1_card["value"] > p2_card["value"]:
        win = "p1"
    if p1_card["value"] < p2_card["value"]:
        win = "p2"
    if p1_card["value"] == p2_card["value"]:
        win = "WAR"
    return win


# print(compare_cards(p1,p2))

def create_deck() -> list[dict]:
    result = []
    for rank in range(2,15):
        if rank < 11:
            for suite in range(4):
                if suite == 0:
                    suite = "H"
                    rank = str(rank)
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 1:
                    suite = "C"
                    rank = str(rank)
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 2:
                    suite = "D"
                    rank = str(rank)
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 3:
                    suite = "S"
                    rank = str(rank)
                    new_card = create_card(rank,suite)
                    result.append(new_card)
        elif rank == 11:
            rank = "J"
            for suite in range(4):
                if suite == 0:
                    suite = "H"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 1:
                    suite = "C"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 2:
                    suite = "D"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 3:
                    suite = "S"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
        elif rank == 12:
            rank = "Q"
            for suite in range(4):
                if suite == 0:
                    suite = "H"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 1:
                    suite = "C"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 2:
                    suite = "D"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 3:
                    suite = "S"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
        elif rank == 13:
            rank = "K"
            for suite in range(4):
                if suite == 0:
                    suite = "H"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 1:
                    suite = "C"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 2:
                    suite = "D"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 3:
                    suite = "S"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
        elif rank == 14:
            rank = "A"
            for suite in range(4):
                if suite == 0:
                    suite = "H"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 1:
                    suite = "C"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 2:
                    suite = "D"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
                elif suite == 3:
                    suite = "S"
                    new_card = create_card(rank,suite)
                    result.append(new_card)
    return result

# print(create_deck())
# print(len(create_deck()))


def shuffle(deck: list[dict]) -> list[dict]:

    return []
