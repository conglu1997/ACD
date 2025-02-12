class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirements": "Given a 4x4 grid of letters, identify the pattern and determine the missing letter in the sequence. The grid follows a pattern based on the alphabetical order.\nGrid:\nA B C D\nE F G H\nI J K L\nM N O _\n"
            },
            "2": {
                "requirements": "Given a 3x3 grid of shapes, determine the missing shape based on the pattern. Shapes are represented by their first letters: C (circle), S (square), T (triangle). The grid follows a pattern based on the sequence and rotation of shapes.\nGrid:\nC S T\nT C S\nS T _\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the spatial reasoning puzzle by identifying the pattern and determining the missing element.

Requirements:
{t['requirements']}

Submit your response in the following format:
Answer: [Your answer]

Note: Carefully analyze the pattern in the grid and ensure your answer fits consistently."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should identify the correct missing element based on the pattern.", "The answer should be a single character or shape identifier that fits the given grid pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
