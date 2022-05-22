from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

# TODO: asking the questions
quiz = QuizBrain(question_bank)
quiz.next_question()

# TODO: checking if  the answer was correct


# TODO: checking if we're the end of the quiz
