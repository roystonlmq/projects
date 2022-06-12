import login_page
import level1
import time
import csv

def main():
    welcome()
    name = user()
    level_1(name)
    # calls for score & rank
    s = score(name)
    rank = ranker(s)
    next_rank(rank)


# returns score
def score(n: str) -> int:
    with open("scores.csv") as f:
        columns = ["name", "score"]
        reader = csv.DictReader(f, columns)
        data = [row for row in reader if row["name"] == n]
        score = int(data[0]["score"])
        return score
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
def ranker(r: int) -> tuple:
    if r >= 90:
        return "Math_Elite", r
    elif r >= 80:
        return "Math_Diamond", r
    elif r >= 60:
        return "Math_Platinum", r
    elif r >= 50:
        return "Math_Gold", r
    elif r >= 40:
        return "Math_Silver+", r
    elif r >= 30:
        return "Math_Silver", r
    elif r >= 20:
        return "Math_Bronze+", r
    elif r >= 10:
        return "Math_Bronze", r
    elif r >= 0: # eliminate possibility that r is negative
        return "Noob", r
    else:
        raise ValueError("r must be a non-negative integer")

def next_rank(r: tuple) -> str:
    # If tuple index 0 is Noob, look to the right of list and calculate (entry - score)
    # where entry = starting score of next rank
    ranks = ["Noob", "Math_Bronze", "Math_Bronze+", "Math_Silver",
    "Math_Silver+", "Math_Gold", "Math_Platinum", "Math_Diamond", "Math_Elite"
    ]
    entry = [0, 10, 20, 30, 40, 50, 60, 80, 90]
    for _ in ranks:
        i = ranks.index(r[0])
    try:
        # next rank
        n = ranks[i+1]
        # score to next rank
        s = entry[i+1] - int(r[1])
        print(f"You are currently {ranks[i]}. Next rank is {n}. You need to earn {s} more points to rank up!")
        return r
    except IndexError:
        print(f"Maximum rank of Math_Elite obtained... \nYou don't need a rank to keep improving on Mathematics, continue to work hard!;)")
        time.sleep(1.5)
        return r

def welcome():
    txt = "Name of program: Mathster\nCreated for: Primary School Kids\nPurpose: Make Math Fun!"
    d = 33 * "*"
    print(f"{d}\n{txt}\n{d}")
    # time.sleep(1.0)

def user():
    user = login_page.User()
    return user.homepage()

def level_1(n):
    level = level1.Level_One(n)
    print(level)
    level.check_ready()
    level.qall()



if __name__ == "__main__":
    main()

