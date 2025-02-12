class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A car rental company charges a flat fee of $50 per day plus $0.20 per mile driven. If a customer rents a car for 3 days and drives 150 miles, what is the total cost?"
            },
            "2": {
                "problem": "A rectangular garden has a length that is twice its width. If the perimeter of the garden is 60 meters, what are the length and width of the garden?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to solve the given math word problem. "
            "Read the problem carefully and provide your solution in plain text format. "
            "Ensure your solution includes the steps you took to arrive at the answer. "
            "Please format your response as follows: \n\n"
            "1. Restate the problem in your own words. \n"
            "2. List the known values and variables. \n"
            "3. Write down the formulas or equations used. \n"
            "4. Show the calculation steps. \n"
            "5. State the final answer clearly."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly restate the problem.",
            "The known values and variables should be listed accurately.",
            "The formulas or equations used should be correct.",
            "The calculation steps should be clear and logical.",
            "The final answer should be accurate and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
