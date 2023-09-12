class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

class QuizApp:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for question in self.questions:
            print(question.question)
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")

            user_answer = input("Enter the number of your answer: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.options):
                    if question.is_correct(question.options[user_answer - 1]):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print(f"Wrong! The correct answer was: {question.correct_answer}\n")
                else:
                    print("Invalid input. Please select a valid option.\n")
            else:
                print("Invalid input. Please enter a number.\n")

        print(f"Quiz completed! Your score is: {self.score}/{len(self.questions)}")


# Create quiz questions
question1 = QuizQuestion("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
question2 = QuizQuestion("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars")
question3 = QuizQuestion("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale", "Horse"], "Blue Whale")

# Create a quiz app
quiz_app = QuizApp()
quiz_app.add_question(question1)
quiz_app.add_question(question2)
quiz_app.add_question(question3)

# Run the quiz app
quiz_app.run()
