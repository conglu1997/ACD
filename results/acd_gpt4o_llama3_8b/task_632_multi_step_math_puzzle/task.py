class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "You have 12 balls; one is either heavier or lighter than the others. You have a balance scale that you can use only three times. Determine which ball is different and whether it is heavier or lighter."
            },
            "2": {
                "puzzle": "You have 9 marbles; one is heavier than the others. You have a balance scale that you can use only twice. Determine which marble is heavier."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical puzzle:

Puzzle: {t['puzzle']}

Your solution should include all the steps and logical reasoning used to arrive at the answer. Ensure that your explanation is clear and detailed. Submit your solution as a plain text string in the following format:

1. Identify the different ball or marble.
2. Specify if the different ball is heavier or lighter (if applicable).
3. Provide a step-by-step explanation of your reasoning process, including each weighing and its outcome.

Format:
1. Different ball/marble: [Your answer]
2. Heavier or lighter (if applicable): [Your answer]
3. Reasoning process:
   - Step 1: [Your detailed explanation]
   - Step 2: [Your detailed explanation]
   - Step 3: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should identify the different ball or marble.",
            "The solution should specify whether the different ball is heavier or lighter (if applicable).",
            "The solution should include all the steps and logical reasoning used to arrive at the answer.",
            "The explanation should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
