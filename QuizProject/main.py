from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"]) # Creating an object until end of the data set
    question_bank.append(new_question) # Assign all the object has been created to a list.

# print(question_bank[0].text)

an_object = QuizBrain(question_bank)

while an_object.still_has_question():
    an_object.next_question()

print("You've completed the quiz")
print(f"Your final score {an_object.score}/{len(question_bank)}")