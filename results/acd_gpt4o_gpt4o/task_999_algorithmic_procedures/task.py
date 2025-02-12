class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Develop an algorithm to sort an array of integers in ascending order using the bubble sort method.",
                "scenario": "Write a detailed step-by-step procedure for sorting an array of integers in ascending order using the bubble sort algorithm. Ensure that each step is clearly explained and logically follows the previous step."
            },
            "2": {
                "problem": "Design an algorithm to find the greatest common divisor (GCD) of two integers using the Euclidean algorithm.",
                "scenario": "Write a detailed step-by-step procedure for finding the greatest common divisor (GCD) of two integers using the Euclidean algorithm. Ensure that each step is clearly explained and logically follows the previous step."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate a clear and logical step-by-step procedure for the given algorithmic problem. Ensure that each step is clearly explained and logically follows the previous step.\n\nProblem:\n\"{t['problem']}\"\n\nScenario:\n\"{t['scenario']}\"\n\nProvide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The procedure should be clear and logical.",
            "Each step should be clearly explained and logically follow the previous step.",
            "The procedure should correctly solve the algorithmic problem.",
            "The procedure should avoid unnecessary steps and be as concise as possible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
