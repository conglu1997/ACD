class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have a 3-gallon jug and a 5-gallon jug. How can you measure exactly 4 gallons of water using these jugs?"},
            "2": {"puzzle": "There are three boxes, one contains only apples, another contains only oranges, and the third contains both apples and oranges. The boxes are labeled incorrectly. You are allowed to pick one fruit from one box. How can you correctly label all the boxes?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logical puzzle:

{t["puzzle"]}

Provide your solution in plain text format, including a detailed explanation of the steps you took to arrive at the solution. Format your response as follows:

Solution: [Your solution]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a correct solution to the logical puzzle.",
            "The response should include a detailed explanation of the steps taken to arrive at the solution.",
            "The response should be logically coherent and clearly structured.",
            "The explanation should include all necessary steps to solve the puzzle without skipping any intermediate steps."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
