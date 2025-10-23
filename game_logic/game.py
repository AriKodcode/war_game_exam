from utils.deck import create_card, create_deck, compare_cards, shuffle


def create_player(name: str = "AI") -> dict:
    result = {"name": "", "hand": [], "won_play": []}
    if name:
        result["name"] = name
    return result





def init_game() -> dict:
    player1 = create_player("Ari")
    player2 = create_player()
    new_deck = shuffle(create_deck())
    player1["hand"] = new_deck[26:]
    player2["hand"] = new_deck[:26]
    game_dict = {
        "deck": new_deck,
        "player1": player1,
        "player2": player2
    }

    return game_dict
print(init_game()["player1"])

def play_round(p1: dict, p2: dict):
    player1 = init_game()["player1"]
    print(player1)
    player2 = init_game()["player2"]
    print(player2)
    return None

