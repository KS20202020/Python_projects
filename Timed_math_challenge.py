import random
import time

operator = ["+", "-", "*"]
min_value = 3
max_value = 15
total_question = 10


def generate_problems():
    left = random.randint(min_value, max_value)
    right = random.randint(min_value, max_value)
    oprt = random.choice(operator)

    question = str(left) + " " + oprt + " " + str(right)

    answer = eval(question)
    return question, answer


wrong = 0
input("Press enter to start.")
print("---------------------")

start_time = time.time()

for i in range(total_question):
    ques, answer = generate_problems()
    while True:
        guess = input("Problem#" + str(i + 1) + " " + ques + " :  ")
        if guess == str(answer):
            break
        wrong += 1
        print("Wrong ", wrong)

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("---------------------")
print("Nice work. You did it in ", total_time, " second!")
