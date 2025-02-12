class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"income": 3000, "expenses": {"rent": 1000, "utilities": 200, "food": 300, "transportation": 150, "entertainment": 100, "savings": 0, "miscellaneous": 0}, "instructions": "Plan a monthly budget to ensure you save at least $500. Adjust the given expenses as necessary while maintaining a reasonable lifestyle. Note: You cannot exceed your total income."},
            "2": {"income": 4500, "expenses": {"rent": 1200, "utilities": 300, "food": 400, "transportation": 200, "entertainment": 200, "savings": 0, "miscellaneous": 0}, "instructions": "Plan a monthly budget to ensure you save at least $1000. Adjust the given expenses as necessary while maintaining a reasonable lifestyle. Note: You cannot exceed your total income."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your monthly income is ${t['income']}. Your current expenses are: {', '.join([f'{item}: ${amount}' for item, amount in t['expenses'].items()])}.\n{t['instructions']}\nSubmit your budget as follows:\nRent: $[Amount]\nUtilities: $[Amount]\nFood: $[Amount]\nTransportation: $[Amount]\nEntertainment: $[Amount]\nSavings: $[Amount]\nMiscellaneous: $[Amount]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The total expenses should not exceed the given income.", "The budget should ensure the specified savings are met.", "The budget should maintain a reasonable distribution across different expense categories.", "The submission should follow the required format.", "The adjusted expenses should be logical and reasonable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
