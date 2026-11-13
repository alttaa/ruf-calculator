"""Cards are stored as integers 0-51: card = rank * 4 + suit."""

RANKS = "23456789TJQKA"   # index 0..12  ('2' is 0, 'A' is 12)
SUITS = "cdhs"            # clubs, diamonds, hearts, spades -> 0..3


def parse_card(text: str) -> int:
    """'Ah' -> 50"""
    rank = RANKS.index(text[0].upper())
    suit = SUITS.index(text[1].lower())
    return rank * 4 + suit


def card_to_str(card: int) -> str:
    """50 -> 'Ah'"""
    rank, suit = divmod(card, 4)
    return RANKS[rank] + SUITS[suit]


def parse_cards(text: str) -> list[int]:
    """'Ah Kh' or 'AhKh' -> [50, 46]"""
    text = text.replace(" ", "")
    return [parse_card(text[i:i + 2]) for i in range(0, len(text), 2)]


def full_deck() -> list[int]:
    return list(range(52))
