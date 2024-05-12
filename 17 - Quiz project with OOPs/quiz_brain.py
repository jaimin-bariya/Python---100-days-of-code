class QuizBrain:
    
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def is_stil_has_question(self):
    
        if (self.question_number < len(self.question_list)-1):
            return True
        else:
            False


    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (true/false) :").capitalize()
        self.checkAnswer(user_answer, current_question.ans)

    
    def checkAnswer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Your answer is correct")
            
        else:
            print(f"Your answer {user_answer} was wrong")
            print(f"Correct answer was {correct_answer}")
        print(f"Your current score {self.score}/{self.question_number} \n")

    

            
