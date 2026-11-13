from ruf_engine.cards import parse_cards
from ruf_engine.evaluator import rank_groups


def test_rank_groups_one_pair():
    assert rank_groups(parse_cards("Ah As Kd 7c 2h")) == [(2, 12), (1, 11), (1, 5), (1, 0)]


def test_rank_groups_full_house():
    # three kings, two fives
    assert rank_groups(parse_cards("Kh Ks Kd 5c 5h")) == [(3, 11), (2, 3)]