class QuizBrain:
    def __init__(self, questionBank):
        self.questionNumber=0
        self.score=0
        self.questionList=questionBank
    
    def still_has_questions(self):
        return self.questionNumber<len(self.questionList)
    
    def next_question(self):
        currentQuestion= self.questionList[self.questionNumber]
        self.questionNumber+=1
        userAnswer=input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ").title()
        self.check_answer(userAnswer=userAnswer, correctAnswer=currentQuestion.answer)
        
    def check_answer(self, userAnswer, correctAnswer):
        if userAnswer==correctAnswer:
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.questionNumber}\n\n")
        
            