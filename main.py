class Question:
    def __init__(self, text, yes, no):
        self.text = text
        self.yes = yes
        self.no = no


class GameContext:
    def showquestion(self, question):
        print(question.text)

    def end_game(self):
        print("End")


class Game:
    def __init__(self, game_context):
        self.game_context = game_context
        self.questions = [
            Question(
                "Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?", 1,
                'end'),
            Question(
                "Does it provide the object creation mechanism that enhances the flexibilities of the existing code?",
                2, 3),
            Question("Does it ensure you have at most one instance of a class in your application?", 9, 10),
            Question("Is it responsible for how one class communicates with others?", 4, 7),
            Question("Does it provide a mechanism to the context to change its behavior?", 5, 6),
            Question("Is Changing behavior built into its scheme?",11, 12),
            Question("Does it allow a group of objects to be notified when some state changes?", 13, 14),
            Question(
                "Does it explain how to assemble objects and classes into larger structure and simplifies the structure by identifying the relationships?",
                8, 'end'),
            Question("Does it attach additional behavior to an object dynamically at run-time?", 15, 16),
            Question("Is it Singleton Pattern?", 17, 18),
            Question("Is it Builder Pattern?", 17, 18),
            Question("Is it State pattern?", 17, 18),
            Question("Is it Strategy Pattern?", 17, 18),
            Question("Is it Observer Pattern?", 17, 18),
            Question("Is it Command Pattern?", 17, 18),
            Question("Is it Decorator pattern?", 17, 18),
            Question("Is it Adapter Pattern?", 17, 18),
            Question("Woohoo!guessed it! Try again?", 0, 'end'),
            Question("Oops!Something went wrong!Try again?", 0, 'end')
        ]
        self.current_question = 0

    def start(self):
        self.game_context.showquestion(self.questions[self.current_question])

    def answer_yes(self):
        next_question = self.questions[self.current_question].yes
        self.process_answer(next_question)

    def answer_no(self):
        next_question = self.questions[self.current_question].no
        self.process_answer(next_question)

    def process_answer(self, next_question):
        if next_question == 'end':
            self.game_context.end_game()
        else:
            self.current_question = next_question
            self.game_context.showquestion(self.questions[self.current_question])


def main():
    """
    The main function that runs the game.
    Creates a game context and a game object, starts the game, and handles player input until the game ends.
    """
    game_context = GameContext()
    game = Game(game_context)
    game.start()

    while True:
        answer = input("").lower()
        if answer == "yes":
            game.answer_yes()
        elif answer == "no":
            game.answer_no()
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")


if __name__ == '__main__':
    main()
