class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine a square with a side length of 8 units. Inside this square, there is a circle perfectly inscribed. Calculate the area of the region outside the circle but inside the square. Provide your calculations and the final answer.",
                "answer": "21.46"
            },
            "2": {
                "description": "You have a right-angled triangle with legs of lengths 5 units and 12 units. Calculate the length of the hypotenuse and the area of the triangle. Provide your calculations and the final answers.",
                "answer": "13, 30"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometric puzzle based on the given description:

Description:
{t['description']}

Provide your solution with the necessary calculations and final answer. Submit your response as a plain text string in the following format:

Calculations: [Your calculations]
Answer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The calculations should be logically sound and lead to the correct final answer.",
            "The final answer should match the expected answer."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
