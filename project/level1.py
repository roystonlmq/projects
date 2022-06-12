# level1.py
# contains list of dictionary of questions

import sys
import csv

class Level_One:
    def __init__(self, name, questions=10):
        self.questions = questions
        self.counter = 0 # score of player
        self.name = name


    def __str__(self):
        print(f"Hi, {self.name}. There are a total of {self.questions} questions. Do your best!")
        return (f"Each question is worth 1 mark. Current score is {self.counter}.")

    # # deprecated
    # @classmethod
    # def get(cls):
    #     name = input("Choose a player name: ").lower()
    #     return cls(name)

    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, questions):
        try:
            if questions == 0:
                if self.counter == 10:
                    self.save_score()
                    print(f"Congratulations, {self.name}. Perfect score of {self.counter}! Completed level one.")
                    return
                else:
                    self.save_score()
                    print(f"Congratulations, {self.name}. Completed level one with a score of {self.counter}. Keep it up!")
                    return
            self._questions = questions
        except IndexError:
            with open("scores.csv", "a") as f:
                f.seek(0)
                columns = ["name", "score"]
                writer = csv.DictWriter(f, columns)
                writer.writerow({"name": self.name, "score": self.counter})
                print(f"Congratulations, {self.name}. Completed level one with a score of {self.counter}. Keep it up!")
                return
    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, counter):
        self._counter = counter

    def check_ready(self):
        while True:
            status = input("Ready? Y/N\n")
            if status.lower() == "y":
                break
            elif status.lower() == "n":
                continue
            else:
                print("Invalid input. Try again.")
                continue

    def save_score(self):
        with open("scores.csv", "r+") as f:
            columns = ["name", "score"]
            reader = csv.DictReader(f, columns)
            # creates a list of dictionaries with name not matching player name
            filtered_output = [line for line in reader if line["name"] != self.name]

            # resets read position of csv file
            f.seek(0)
            # creates a list of dictionary with name matching player name to store score key-value pair
            past_record = [line for line in reader if line["name"] == self.name]
            # indexes into list, using score as a key to obtain its valuem, then adding to current score
            score = int((past_record[0])["score"]) + self.counter
            # dictionary
            update = {"name": self.name, "score": score}
            filtered_output.append(update)

            # resets read position of csv file
            f.seek(0)
            writer = csv.DictWriter(f, columns)
            # rewrites the file
            writer.writerows(filtered_output)
            return score


    def q1(self):
        question = input("If 1/10 is 0.1, what is 2/10 in decimal?\n")
        solution = "0.2"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: The numerator matches the tenth place for fractions with 10 as denominator. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 0.2. Try better next time!")
            self.questions -= 1

    def q2(self):
        question = input("If 5/10 is 0.5, what is 50/100 in decimal?\n")
        solution = "0.5"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: The numerator matches the tenth place for fractions with 10 as denominator. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 0.5. Try better next time!")
            self.questions -= 1


    def q3(self):
        question = input("If 23/100 is 0.23, what is 46/100 in decimal?\n")
        solution = "0.46"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: What does the numerator and the tenth & hundredth place have in common? Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 0.46. Try better next time!")
            self.questions -= 1

    def q4(self):
        question = input("If 888/1000 is 0.888, what is 463/1000 in decimal?\n")
        solution = "0.463"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: What does the numerator and the tenth, hundredth & thousandth place have in common? Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 0.463. Try better next time!")
            self.questions -= 1

    def q5(self):
        question = input("What is 3 divided by 4 in fraction?\n")
        solution = "3/4"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: Try writing it out using the division sign. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 3/4. Try better next time!")
            self.questions -= 1

    def q6(self):
        question = input("What is 5 divided by 10 in fraction?\n")
        solution = "1/2"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: Remember to simplify! Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 1/2. Try better next time!")
            self.questions -= 1

    def q7(self):
        question = input("If 1% is 0.01, what is 2% in decimal?\n")
        solution = "0.02"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: Take a closer look at the hundredth place. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 0.02. Try better next time!")
            self.questions -= 1

    def q8(self):
        question = input("If 20% is 1/5, what is 40% in fraction?\n")
        solution = "2/5"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint: 40% is 20% multiplied by 2. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 2/5. Try better next time!")
            self.questions -= 1

    def q9(self):
        question = input("If 1/2 x 1/2 is 1/4, what is 2/4 x 2/4?\n")
        solution = "1/4"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint:\nMultiplying fractions mean that you can only multiply the numerator together and the denominator together, respectively. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 1/4. Try better next time!")
            self.questions -= 1

    def q10(self):
        question = input("If 1/4 x 1/2 is 1/8, what is 1/2 x 1/8?\n")
        solution = "1/16"
        if question == solution:
            self.counter += 1
            print("Current score:", self.counter)
            self.questions -= 1
        else:
            i = 1
            while i < 4:
                print(f"Hint:\nMultiplying fractions mean that you can only multiply the numerator together and the denominator together, respectively. Try again!\nAttempt {i}: ", end="")
                attempt = input()
                if attempt == solution:
                    self.counter += 1
                    print("Current score:", self.counter)
                    self.questions -= 1
                    return
                else:
                    i += 1
            print("The correct answer is 1/16. Try better next time!")
            self.questions -= 1

# method to call all questions
    def qall(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
        self.q5()
        self.q6()
        self.q7()
        self.q8()
        self.q9()
        self.q10()


