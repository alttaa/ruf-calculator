from ruf_engine.cards import parse_card, card_to_str, parse_cards, full_deck


def test_ace_of_hearts():
    assert parse_card("Ah") == 50


def test_round_trip_every_card():
    for card in full_deck():
        assert parse_card(card_to_str(card)) == card


def test_parse_cards_with_and_without_spaces():
    assert parse_cards("Ah Kh") == parse_cards("AhKh") == [50, 46]


def test_deck_has_52_unique_cards():
    assert len(set(full_deck())) == 52
