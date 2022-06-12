# MATHSTER
#### Video Demo: https://youtu.be/Kc-vUw5-J7w

#### Description:
A terminal-run Python program that features a login system, a mathematics quiz, and a ranking system.

**The login system has the following features:**

1. Login with username, email & password
2. Register a new username (system will check if it exists), with email, security question and password
3. If you forget your password, you may recover it via the 'Forget Password' function which will prompt you for the email, username, and security question and answer

**The mathematics quiz is the core of this program:**

As I am a part-time tutor for Primary School Mathematics, I discovered that a common problem amongst these students were the inability to correlate fractions, decimals and percentages. Hence, a huge part of the quiz's design centred around that. The Class object allows questions to be added, greater difficulty.

**Currently, the quiz has the following features:**

1. Integration with the login system such that the username logged in is tagged to the player's score
2. 10 questions of easy difficulty with 3 attempts for each question before lowering the score by 1 point
3. Tracking of total score based on past attempts


**Finally, the ranking system has the following features:**

1. Outputs a ranking system based on that total score
2. Informs the player of how many more points required to reach the next rank
3. More ranks can be added easily through easy modifications in the code

**Files Descriptions**
1. level1.py has a Level_One class centred around Primary School Mathematics fundamentals
    - The object requires a 'name' to be included in its parameters in order for it to be instantiated
    - Features a counter that keeps track of the player's score
        - Stores in a database called **scores.csv** with the username and its score
        - If the user plays again, the previous score will be stored and accumulated under the same username so there will be no double inputs
    - Personalised messages addressing the player's name
    - Hints and correct answer after a fixed number of attempts

2. login_page.py has a User class which allows it to be used as a basic authentication system
    - Login system with username and password
        - System checks if the username exists in **userbase.csv** file then checks in the same file if the password is a match
            - Results in a successful login message
    - Registration system
        - Prompts for username, password, email, answer to a basic security question
            - Stores the username, password, email in userbase.csv file
            - Email and answer to question is stored in **security.csv** file
    - Forget password system
        - Prompts user for the registered username
            - System checks if the username exists in userbase.csv
        - Prompts user for the registered email
            - System checks if the email exists in userbase.csv
        - Prompts user for their answer to the security question
            - System checks if the email and the answer are in the same row in the security.csv file
        - If all three prompts end with a 'true' statement, the password is returned to the user
    - Exit program
        - Allows the user to exit the program as the login page is placed on an infinite loop unless the user logins successfully

3. project.py serves as the final cog in the system which links up the User object and the Level_One object. It also introduces a ranking system and its associated functions which allows for it to be tested via pytest.
    - Instantiates the login system
    - Login system returns with the user's name if login was successful
    - The name is passed to the Level_One object and is then instantiated
        - Scores are then saved under that particular name
            - If the name exists, score will become cumulative
    - Level_One object returns the score which is passed through a ranking system
    - **Ranking system is as follows:**
            Score - Rank
            >90 - "Math_Elite"
            80-89 - "Math_Diamond"
            60-79 - "Math_Platinum"
            50-59 - "Math_Gold"
            40-49 - "Math_Silver+"
            30-39 - "Math_Silver"
            20-29 - "Math_Bronze+"
            10-19 - "Math_Bronze"
    - Ranking system takes the returned score and pairs it with the rank in that score range
        - Outputs the difference between the current score and the next rank's entry score
            - Entry score is defined as the lowest number in a rank's range
        - Informs the user of how many more points is required to reach the next rank
        - Informs the user of his current rank

4. test_project.py is a unit test of the functions found in project.py
    - The following functions are tested: score, ranker, next_rank
        - the score function is tested by checking whether the value of the score matches the score found in the csv file
        - the ranker function is tested by checking if given a score value, r, integer, whether it matches to the correct rank
        - the next_rank function is tested by checking to see if it returns the tuple, r which is formatted as ('rank: str', score: int)
            - Unable to see if it returns a particular string due to limitations of pytest

**What have I learnt from this project?**
Login system:
I was particularly proud with how I took advantage of Object-Oriented Programming and used Class to define a User object. I learnt that when instantiated the object remembers the values and these variables containing these values can be used in other methods of the object. This made designing the login system intuitive. It gave me a lot of practice in File I/O, delving into what happens if you try to read the same .csv file twice. I found out that a simple '.seek(0)' solved the problem.

However, after researching the login system, I have come to realise that reinventing the wheel is extremely difficult. I remembered watching crytography videos relating to Python, explaining what 'salt' was and being overwhelmed. I decided to create a basic authentication system so I could improve on it in future projects.

Ranking system:
Initially, I wanted to implement something similar to an elo system in competitive online games such as DOTA and CSGO. However, given that the program currently only runs in the terminal, I opted for a simpler ranking system. I created the names, trying my best to associate it with games and math, and then assigned arbitrary values to them. My hope for a ranking system is to drive users to keep working hard on finding methods to solve the questions.

Math Game:
This was the lengthiest .py file I have ever written. Much of the code was the questions. The questions needed an input and an answer, it also required a counter to keep track of the questions left and the score obtained thus far.

**What I want to learn more about**
After going through CS50P, I want to know more about how to write code more efficiently. Right now, I think that means learning more about OOP and learning how to write effective functions. I also want to start creating actual programs. On my own time, I have been researching a lot on how to dig deeper into Python, so I hope to take action in that aspect.



