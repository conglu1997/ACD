class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'problem': 'You are given a list of numbers. Write a function to find the maximum product of any three numbers in the list.', 'example': '[1, 10, 2, 6, 5, 3] -> 300 (10 * 6 * 5)'},
            '2': {'problem': 'Solve the following logic puzzle: There are three boxes, each with two balls inside. One box has two red balls, one has two blue balls, and one has one red and one blue ball. You cannot see inside the boxes. You are allowed to pick one ball from one box (without looking inside) and based on the color of the ball, you must determine the contents of each box. How do you do it?', 'example': 'If you pick a red ball from the box labeled "one red and one blue", you can determine the contents of all boxes.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given problem using a combination of logic, mathematical reasoning, and programming where necessary. Make sure your solution is clear, well-structured, and correct.

Problem: {t['problem']}

Example: {t['example']}

Provide your response in plain text format, including any code you write as part of your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly solve the problem.", "Any provided code should be syntactically correct and functional.", "The explanation should be clear and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
