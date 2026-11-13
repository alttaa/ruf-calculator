from collections import Counter

from ruf_engine.cards import RANKS


def rank_groups(cards: list[int]) -> list[tuple[int, int]]:
    """[(count, rank), ...] sorted biggest first.

    A♥ A♠ K♦ 7♣ 2♥ -> [(2, 12), (1, 11), (1, 5), (1, 0)]
    """
    ranks = [card // 4 for card in cards]   # 50 // 4 = 12 (ace)
    counts = Counter(ranks)                  # {12: 2, 11: 1, 5: 1, 0: 1}
    return sorted(((n, r) for r, n in counts.items()), reverse=True)

#demo block 

