import random

total_questions:list[list[str]] = [
    ["A slug's blood is green.", "True"],
    ["The loudest animal is the African Elephant." , "False"],
    ["Approximately one quarter of human bones are in the feet.", "True"],
    ["The total surface area of a human lungs is the size of a football pitch." , "True"],
    ["In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
             "to eat." , "True"],
    ["In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral." , "False"],
    ["It is illegal to pee in the Ocean in Portugal." , "True"],
    ["You can lead a cow down stairs but not up stairs." , "False"],
    ["Google was originally called 'Backrub'." , "True"],
    ["Buzz Aldrin's mother's maiden name was 'Moon'." , "True"],
    ["No piece of square dry paper can be folded in half more than 7 times." , "False"],
    ["A few ounces of chocolate can to kill a small dog.", "True"]
]

points:int = 0
Q:int = 0

used_question:list[list[str]] = []
question:list[str] = random.choice(total_questions)

print(question[0])

used_question.append(question)
answer:str = input("True/False: ")
if answer == question[1]:
    Q = Q + 1
    points = points + 1
    print(f"Your current score is {points}/{Q}")
else:
    Q = Q + 1
    print(f"Your current score is {points}/{Q}")