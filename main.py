from utils.deck import create_card, create_deck, compare_cards, shuffle
from game_logic.game import create_player, init_game, play_round

if __name__ == "__main__":
    # from utils

    print(create_card("2", "D"))
    p1 = create_card("A", "S")
    p2 = create_card("3", "D")
    print(compare_cards(p1, p2))

    print(create_deck())

    print(shuffle(create_deck()))

    # from game_logic
    print(create_player("ari"))
    print(create_player())

    print(init_game())
