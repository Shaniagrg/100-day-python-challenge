import random
class Quiz:

    all_question:dict[str,str] = {}
    def __init__(self):
        self.all_question = {"A slug's blood is green.":"True",
        "The loudest animal is the African Elephant." :"False",
        "Approximately one quarter of human bones are in the feet." : "True",
        "The total surface area of a human lungs is the size of a football pitch." : "True",
        "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
                "to eat." : "True",
        "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral." : "False",
        "It is illegal to pee in the Ocean in Portugal." : "True",
        "You can lead a cow down stairs but not up stairs." : "False",
        "Google was originally called 'Backrub'." : "True",
        "Buzz Aldrin's mother's maiden name was 'Moon'." : "True",
        "No piece of square dry paper can be folded in half more than 7 times." : "False",
        "A few ounces of chocolate can to kill a small dog.": "True"}
        

    def start_quiz(self):
        user_total_points:list[int] = [0,0]
        used_question:set[str] = set()
        while True:
            question:list[str] = random.choice(list(self.all_question.items()))
            if len(used_question) == len(self.all_question):
                self.end_game(user_total_points)
                break
            elif question[0] in used_question:
                continue
            else:
                self.check_answer(question,user_total_points,used_question)
            
    def end_game(self,points:list[int]):
        print("Thanks for completing that")
        print(f"Your final score is:{points[0]}/{points[1]}")
        exit_quiz:str = input("Process finish with exit code 0: ")

    def check_answer(self,question:list[str],user_total_points:list[int], used_question:set[str]):
        points:int = user_total_points[0]
        Q_count:int = user_total_points[1]
        while True:
                    print(question[0])
                    used_question.add(question[0])
                    answer:str = input("True/False: ")
                    if answer == "True" or answer == "False":
                        if answer == question[1]:
                            Q_count = Q_count + 1
                            points = points + 1
                            print(f"You got it right!!!")
                            print(f"The correct answer was: {question[1]}")
                            print(f"Your current score is {points}/{Q_count}")
                        else:
                            Q_count = Q_count + 1
                            print("That's incorrect")
                            print(f"The correct answer was: {question[1]}")
                            print(f"Your current score is {points}/{Q_count}")
                        break
                    else:
                        print("Type the correct word.")
                        continue
        user_total_points[0] = points
        user_total_points[1] = Q_count
        #return(user_total_points)

Quiz_sam:Quiz = Quiz()
Quiz_sam.start_quiz()