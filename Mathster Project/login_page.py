# To create a Login object
import csv
import sys
import time
from pwinput import pwinput
import validators


class User:
    def email(self):
        self.email = input("Email: ").strip()
        if validate(self.email) != True:
            print("Email found to be invalid.")
            return None
        else:
            return self.email

    def login(self):
        self.username = input("Username: ")
        #self.email = input("Email: ")
        self.password = pwinput()
        user_data = {"username": self.username, "password": self.password}
        with open("userbase.csv") as file:
            reader = csv.DictReader(file, fieldnames=["username", "password"])
            for row in reader:
                if row["username"] == user_data["username"] and row["password"] == user_data["password"]:
                    return ("Success")
        return ("Unsuccessful")


    def register(self):
        # creating a new e-mail function as 2FA for forget password feature
        if self.email() == None:
            return None
           # checking to see if username exists in userbase.csv
        with open("userbase.csv") as file:
            reader = csv.DictReader(file, fieldnames=["username", "password", "email"])
            file.seek(0)
            for row in reader:
                if row["email"] == self.email:
                    print("Email is registered with an account already.")
                    return None
        self.username = input("Username: ").lower().strip()
        # checking to see if username exists in userbase.csv
        with open("userbase.csv") as file:
            reader = csv.DictReader(file, fieldnames=["username", "password"])
            file.seek(0)
            for row in reader:
                if row["username"] == self.username:
                    print("Username already exists")
                    return None
        # requests for confirmation of password
        while True:
            pw = pwinput(prompt="Enter desired password: ")
            print("Password length:", len(pw))
            pw_2 = pwinput(prompt="Confirm password: ")
            if pw != pw_2:
                print("Password did not match")
                continue
            else:
                password = pw
                self.password = password
                break
        # saves username and password into a csv file
        with open("userbase.csv", "a") as file:
            file.seek(0)
            writer = csv.DictWriter(file, fieldnames=["username", "password", "email"])
            writer.writerow({"username": self.username, "password": self.password, "email": self.email})
        ans_question = input("Which Primary School did you go to?\n")
        with open("security.csv", "a") as file:
            file.seek(0)
            writer = csv.DictWriter(file, fieldnames=["answer", "email"])
            writer.writerow({"answer": ans_question.strip(), "email": self.email.strip()})
        return "Success"

    def forget(self):
        self.email = input("Enter the email address you registered with.\n")
        self.username = input("Enter the username you registered with.\n")
        ans_question = input("Security Question: Which Primary School did you go to?\n")
        security_data = {"answer": ans_question, "email": self.email}
        y = '' # just a random variable for control-flow purposes
        with open("security.csv") as file:
            file.seek(0)
            reader = csv.DictReader(file, fieldnames=["answer", "email"])
            for row in reader:
                if row == security_data:
                    y = 'true' # allows method to print forgotten password
        if y != 'true':
            return
        with open("userbase.csv") as file:
            file.seek(0)
            reader = csv.DictReader(file, fieldnames=["username", "password", "email"])
            for row in reader:
                if row["username"] == self.username:
                    print(f"Your password was... {row['password']}")
                    return "Success"

    def homepage(self):
        i = 2
        while i < 3:
            print_slow("Hello, welcome to the login page.\n")
            txt = "1. Login\n2. Register\n3. Forgot Password\n4. Exit Program\n"
            choice = input(txt)
            _choice = ["1", "2", "3", "4"]

            if choice not in _choice:
                i += 1
                print(f"Invalid choice selected. 1-4 only. Try again. {i}/3")

            elif choice == _choice[0]: # Login feature
                if self.login() != "Success":
                    print("Login was unsuccessful")

                else:
                    print(f"{self.username} has logged into the program successfully.")
                    return self.username

            elif choice == _choice[1]: # Registration feature
                if self.register() != "Success":
                    print("Registration was unsuccessful")
                else:
                    print(f"{self.username}'s registration was successful.")


            elif choice == _choice[2]: # Forget password feature
                if self.forget() != "Success":
                    print("Invalid information was inputted.")
                else:
                    print("Password successfully recovered.")
            elif choice == _choice[3]:
                sys.exit("Exiting program now...")
        sys.exit("Quitting")


# typewriter effect
# source: Stackoverflow
def print_slow(str):
    for char in str:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

# for validating email addresses
def validate(s):
    return (validators.email(s))


