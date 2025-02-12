class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "The average rainfall in millimeters for the past 5 years in City A: Year 1: 800, Year 2: 850, Year 3: 780, Year 4: 820, Year 5: 810."},
            "2": {"data": "The quarterly sales figures for a company in thousands of dollars: Q1: 50, Q2: 75, Q3: 60, Q4: 90."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given numerical data and perform the required calculations.

Data: {t['data']}

For Task 1: Calculate the average rainfall over the 5 years and determine the year with the highest rainfall.
For Task 2: Calculate the total sales for the year and determine the quarter with the highest sales.

Provide your response in plain text format as follows:

Calculations:
1. [Your step-by-step calculations here]
2. [Continue if needed]

Results:
1. [Your results here]
2. [Continue if needed]

Example format:

Calculations:
1. (800 + 850 + 780 + 820 + 810) / 5 = 812 mm
2. Highest rainfall year: Year 2 with 850 mm

Results:
1. Average rainfall: 812 mm
2. Year with highest rainfall: Year 2"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include correct calculations based on the given data.",
            "The results should accurately reflect the calculations performed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
