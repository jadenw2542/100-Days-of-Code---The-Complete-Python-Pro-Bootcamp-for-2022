from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while(quiz.still_has_question()):
    quiz.next_question()

print("You've completed the quix")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")