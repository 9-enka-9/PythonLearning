from os import system
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from time import TIME

_=system("cls")
questionBank=[]
for item in question_data:
    newQuestion=Question(text=item["question"], answer=item["correct_answer"])
    questionBank.append(newQuestion)

quiz=QuizBrain(questionBank=questionBank)
while quiz.still_has_questions():
    quiz.next_question()
    TIME.sleep(2000)
    _=system("cls")
print("You've completed the quiz.")
print(f"Your final score was {quiz.score}/{len(quiz.questionList)}")
