class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzles": [
                    "Puzzle 1: What has keys but can't open locks?",
                    "Puzzle 2: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
                ],
                "answers": [
                    "A piano",
                    "An echo"
                ],
                "generation_example": "Puzzle: I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"
            },
            "2": {
                "puzzles": [
                    "Puzzle 1: What comes once in a minute, twice in a moment, but never in a thousand years?",
                    "Puzzle 2: The more you take, the more you leave behind. What am I?"
                ],
                "answers": [
                    "The letter 'm'",
                    "Footsteps"
                ],
                "generation_example": "Puzzle: I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzles_text = '\n'.join(t['puzzles'])
        return f"""Your task is to solve the following puzzles and then generate a new puzzle based on the provided example.

Puzzles:
{puzzles_text}

Generation Example:
{t['generation_example']}

Provide your solutions and new puzzle in the following format:
Solutions: [Your solutions]
New Puzzle: [Your generated puzzle]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        t_solutions = t['answers']
        instructions = TaskFamily.get_instructions(t)
        submission_lines = submission.split('\n')
        if len(submission_lines) < 2:
            return 0.0
        try:
            solutions = eval(submission_lines[0].split(': ')[1])
            new_puzzle = submission_lines[1].split(': ')[1]
        except:
            return 0.0
        if solutions == t_solutions and new_puzzle.startswith("Puzzle:"):
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria=["The new puzzle should be in the correct format and solvable."]) else 0.0
        return 0.0
