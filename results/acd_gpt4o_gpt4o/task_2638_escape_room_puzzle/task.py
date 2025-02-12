class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzles": [
                    {
                        "description": "You find yourself in a locked room with three boxes. Each box has a different color: red, blue, and green. Inside one of the boxes is a key to the door. There is a note that reads: 'The key is not in the red or green box.' Which box contains the key?",
                        "solution": "blue"
                    },
                    {
                        "description": "After finding the key, you open the door to another room. This room has a series of numbers on the wall: 2, 4, 8, 16, ? What is the next number in the sequence?",
                        "solution": "32"
                    }
                ]
            },
            "2": {
                "puzzles": [
                    {
                        "description": "You enter a new room with a chessboard and a single note: 'Place a knight on the board such that it can attack exactly two other knights. How many possible squares can the knight be placed on?'",
                        "solution": "16"
                    },
                    {
                        "description": "In the final room, you see a combination lock with a clue: 'The code is the square of 5, followed by the cube of 2.' What is the code?",
                        "solution": "2538"
                    }
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You are in a virtual escape room. Solve the following puzzles to escape. Each puzzle must be solved in sequence. Provide your answers in plain text, each answer on a new line. For example, if the answers to the puzzles are 'blue' and '32', your response should be:\nblue\n32"
        for idx, puzzle in enumerate(t['puzzles'], 1):
            instructions += f"\nPuzzle {idx}: {puzzle['description']}"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = [puzzle['solution'] for puzzle in t['puzzles']]
        criteria = [f"The answer to Puzzle {idx+1} is '{solution}'." for idx, solution in enumerate(correct_answers)]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
