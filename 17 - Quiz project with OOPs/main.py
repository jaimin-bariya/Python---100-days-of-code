from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from os import system




# step 1 - List Creation, fetch text and answer, add text and ans after created new object
question_bank = []

for q in question_data:
    que_text = q["text"]
    que_answer = q["answer"]
    new_question = Question(text=que_text, answer=que_answer)
    question_bank.append(new_question)


# how to access first object's text and aswer
# print(question_bank[0].text)
# print(question_bank[0].ans)

# for i in range(len(question_bank)):
#     print(f" Q.{i} {question_bank[i].text} - {question_bank[i].ans} \n")


# step 2 - ask question
quiz = QuizBrain(question_bank)


while (quiz.is_stil_has_question()):
    quiz.nextQuestion()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")

