class Question:
    """
    A class representing a question in the game.

    Attributes:
    text (str): The text of the question.
    yes (int or str): The index of the next question to ask if the answer is 'yes', or the value 'end' if the game ends.
    no (int or str): The index of the next question to ask if the answer is 'no', or the value 'end' if the game ends.
    """
    def __init__(self, text, yes, no):
        """
        Initializes a new Question object.

        Parameters:
        text (str): The text of the question.
        yes (int or str): The index of the next question to ask if the answer is 'yes', or the value 'end' if the game ends.
        no (int or str): The index of the next question to ask if the answer is 'no', or the value 'end' if the game ends.
        """
        self.text = text
        self.yes = yes
        self.no = no


class GameContext:
    """
    A class representing the context of the game.
    """
    def showquestion(self, question):
        """
        Displays the text of the given question.

        Parameters:
        question (Question): The question to display.
        """
        print(question.text)

    def end_game(self):
        """
        Displays a message indicating that the game has ended.
        """
        print("End")


class Game:
    """
    A class representing the game.

    Attributes:
    game_context (GameContext): The context of the game.
    questions (list of Question): The list of questions in the game.
    current_question (int): The index of the current question in the game.
    """
    def __init__(self, game_context):
        """
        Initializes a new Game object.

        Parameters:
        game_context (GameContext): The context of the game.
        """
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
        """
        Starts the game by displaying the first question.
        """
        self.game_context.showquestion(self.questions[self.current_question])

    def answer_yes(self):
        """
        Processes the player's answer of 'yes' by displaying the next question based on the current question's 'yes' attribute.
        """
        next_question = self.questions[self.current_question].yes
        self.process_answer(next_question)

    def answer_no(self):
        """
        Processes the player's answer of 'no' by displaying the next question based on the current question's 'no' attribute.
        """
        next_question = self.questions[self.current_question].no
        self.process_answer(next_question)

    def process_answer(self, next_question):
        """
        Processes the player's answer by updating the current question and displaying the next question or ending the game.

        Parameters:
        next_question (int or str): The index of the next question to display or the value 'end' to end the game.
        """
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
