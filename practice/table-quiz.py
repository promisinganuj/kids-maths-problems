import random
from inputimeout import inputimeout, TimeoutOccurred

while True:
    try:
        num_questions = int(input("Enter the number of questions: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

correct_answers = 0

for _ in range(num_questions):
    num1 = random.randint(11, 16)
    num2 = random.randint(3, 12)
    while True:
        try:
            answer = int(inputimeout(prompt=f"{num1} * {num2} = ", timeout=6))
            break
        except ValueError:
            print("Please enter a valid integer.")
        except TimeoutOccurred:
            print("Times up!")
            break

    if answer == num1 * num2:
        print("Correct")
        correct_answers += 1
    else:
        print("Incorrect")

percentage_correct = (correct_answers / num_questions) * 100

print(f"\n====== Summary ======\n  Total Questions: {num_questions}\n  Correct Answers: {correct_answers}\n  Percentage Correct: {percentage_correct}%")
