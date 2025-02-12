class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "There are three houses in a row. Each house is painted a different color (red, blue, green) and inhabited by a person with a different pet (cat, dog, bird). The person in the red house lives next to the person with the dog. The person with the bird lives in the blue house. The green house is not at either end. Who lives in the green house and what pet do they have?"},
            "2": {"puzzle": "In a group of five people standing in a line, each person has a different favorite fruit (apple, banana, cherry, date, elderberry). The person who likes apples is not standing next to the person who likes bananas. The person who likes cherries is standing to the left of the person who likes dates. The person who likes elderberries is at the far right. Who is standing next to the person who likes elderberries?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logic puzzle and explain your solution process.

Puzzle:
{t['puzzle']}

Instructions:
1. Analyze the given clues.
2. Determine the solution to the puzzle.
3. Provide a detailed explanation of your solution process, including the reasoning behind each step.

Format your response as follows:

Solution:
[Your solution]

Explanation:
[Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must be correct and match the given clues.",
            "The explanation must be detailed and logical, demonstrating the reasoning process."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
