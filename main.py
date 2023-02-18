# score dependent on speed of input/correct/incorrect
# grading system A,b,c
# print which answers user entered incorrectly!
# store random int to be repeated if person fails to give valid input
# include different difficulty settings. I.e. easy is 2 x 3, medium is 12 x 7, hard is 14 x 25

# graphics
# start button that fades out when you click it
# question fades in number/sign/number individually
# 3 choices, 2 are randomly generation one is correct solution

import random
import time

def display_options():
    list_options=["Would you like to play?","1. Yes", "2. No"]
    for option in list_options:
        print(option)

def select_option():
    while True:
        operation = input("")
        if operation == "yes" or operation == "1":
            return operation
        elif operation == "no" or operation == "2":
            print("Okay, we're done")
            quit()
        else:
            print("Invalid input. Please try again: ")

def gen_problem(operation):
    num1 = random.randint(2,49)
    num2 = random.randint(2,49)
    if operation == "1" or operation == "yes":
        problem = f"{num1} + {num2}"
        solution = num1 + num2
    else:
        print("invalid operation")
    return problem, solution


def get_user_solution(problem):
    print(problem, end="")
    while True:
        try:
            result = int(input(" = "))
            return result
        except ValueError:
            print("Try again")
            print(problem, end="")

def main():
    display_options()
    option = select_option()
    correct = 0
    score = 0
    begin = time.time()

    if option == "1" or option == "yes":

        #Q1

        prob, solution = gen_problem(option)
        user_answer = get_user_solution(prob)
        if user_answer == solution:
            print("correct")
            correct += 1
            T1 = time.time()
            elapsed = T1 - begin
            if elapsed < 3:
                score += 5
            elif elapsed < 5:
                score += 3
            elif elapsed > 5:
                score += 1
        else:
            print("incorrect")

        #Q2

        prob, solution = gen_problem(option)
        user_answer = get_user_solution(prob)
        if user_answer == solution:
            print("correct")
            correct += 1
            T2 = time.time()
            elapsed = T2 - T1
            if elapsed < 3:
                score += 5
            elif elapsed < 5:
                score += 3
            elif elapsed > 5:
                score += 1
        else:
            print("incorrect")

        #Q3

        prob, solution = gen_problem(option)
        user_answer = get_user_solution(prob)
        if user_answer == solution:
            print("correct")
            correct += 1
            T3 = time.time()
            elapsed = T3 - T2
            if elapsed < 3:
                score += 5
            elif elapsed < 5:
                score += 3
            elif elapsed > 5:
                score += 1

        else:
            print("incorrect")

    if correct > 0:
        print("Congratulations, you got", correct, "out of 3 answers correct!")
        print("Score: ", score)
    else:
        print("Unlucky. You got 0 out of 3 answers correct.")
        print("Score: ", score)

main()