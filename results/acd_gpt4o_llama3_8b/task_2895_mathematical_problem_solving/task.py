class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following problem: A car travels at a constant speed of 60 miles per hour. How long will it take to travel 180 miles? Provide your answer in hours. Format your response as follows: Answer: [Your answer in hours]. Remember to use the formula: time = distance / speed."
            },
            "2": {
                "problem": "Solve the following problem: If the sum of three consecutive integers is 72, what are the integers? Provide your answer as a comma-separated list of the three integers. Format your response as follows: Answer: [integer1, integer2, integer3]. Note that consecutive integers follow the pattern n, n+1, n+2."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['problem']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should be correct based on standard mathematical principles.",
            "The answer should be formatted as specified in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
