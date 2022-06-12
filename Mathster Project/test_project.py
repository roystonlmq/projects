from project import score, ranker, next_rank, welcome, user, level_1
import csv
import pytest

# tester1,10
# test,10
# troy,30
# roy,120


def test_score():
    assert score("roy") == int(case_1)
    assert score("troy") == int(case_2)
    assert score("test") == int(case_3)
    assert score("tester1") == int(case_4)
    with pytest.raises(IndexError):
        # looks up a non-existent user, expects IndexError
        score("sadjas@3232!")


"""
returns rank according to score
>90 - "Math_Elite"
80-89 - "Math_Diamond"
60-79 - "Math_Platinum"
50-59 - "Math_Gold"
40-49 - "Math_Silver+"
30-39 - "Math_Silver"
20-29 - "Math_Bronze+"
10-19 - "Math_Bronze"
"""
def test_ranker():
    assert ranker(50) == ("Math_Gold", 50)
    assert ranker(3) == ("Noob", 3)
    assert ranker(89) == ("Math_Diamond", 89)
    assert ranker(1337) == ("Math_Elite", 1337)
    assert ranker(0) == ("Noob", 0)
    # tests for non-integer
    with pytest.raises(TypeError):
        assert ranker('cat')

    # tests for non-negative integer
    with pytest.raises(ValueError):
        assert ranker(-1)

def test_next_rank():
    assert next_rank(('Math_Gold', 50)) == ("Math_Gold", 50)
    assert next_rank(('Math_Elite', 99)) == ("Math_Elite", 99)
    with pytest.raises(ValueError):
        assert next_rank('nonsense')

def test_welcome():
    assert welcome() == None

def test_user():
    with pytest.raises(OSError):
        assert user()

def test_level_1():
    with pytest.raises(OSError):
        assert level_1('roy')


def main():
    test_score()
    test_ranker()
    test_next_rank()
    test_welcome()
    test_user()
    test_level_1()

with open("scores.csv") as f:
    columns = ["name", "score"]
    reader = csv.DictReader(f, columns)
    for row in reader:
        name_key = row["name"]
        score_key = row["score"]
        if name_key == "roy":
            case_1 = score_key
        elif name_key == "troy":
            case_2 = score_key
        elif name_key == "test":
            case_3 = score_key
        elif name_key == "tester1":
            case_4 = score_key
