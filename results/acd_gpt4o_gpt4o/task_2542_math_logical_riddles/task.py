class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"riddle": "I am a three-digit number. My tens digit is five more than my ones digit, and my hundreds digit is eight less than my tens digit. What number am I?"},
            "2": {"riddle": "There are three boxes, each containing two marbles. One box has two red marbles, one has two blue marbles, and the last has one red and one blue marble. The boxes are labeled, but all the labels are incorrect. You may pick one marble from one box without looking inside. By picking one marble, how can you correctly label all the boxes?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following riddle using mathematical reasoning and logical deduction:

Riddle: {t['riddle']}

Provide your answer in a clear and concise manner, explaining your reasoning step by step. Your response should be in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['riddle'] == "I am a three-digit number. My tens digit is five more than my ones digit, and my hundreds digit is eight less than my tens digit. What number am I?":
            criteria = [
                "The answer should be 194.",
                "The explanation should logically follow the clues given in the riddle."
            ]
        elif t['riddle'] == "There are three boxes, each containing two marbles. One box has two red marbles, one has two blue marbles, and the last has one red and one blue marble. The boxes are labeled, but all the labels are incorrect. You may pick one marble from one box without looking inside. By picking one marble, how can you correctly label all the boxes?":
            criteria = [
                "The answer should explain that you should pick a marble from the box labeled 'one red and one blue'.", 
                "The explanation should logically deduce the correct labeling of all boxes based on the outcome of picking the marble."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
