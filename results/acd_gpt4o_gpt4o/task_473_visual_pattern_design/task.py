class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create a visual pattern that alternates between circles and squares in a 3x3 grid. The circles should be filled with the color red, and the squares should be filled with the color blue."},
            "2": {"description": "Interpret the following visual pattern: 'A 4x4 grid where each row alternates between red circles and blue squares. The first row starts with a red circle.' Describe the rule it follows and predict the next row in the sequence."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to either create or interpret a visual pattern based on the given description.

Description: {description}

For creation tasks, describe the visual pattern in a way that clearly conveys the arrangement, colors, and shapes. For interpretation tasks, provide a detailed explanation of the rule or pattern you observe and predict the next row in the sequence.

Provide your response in the following format:

Pattern Description:
[Your pattern description]

Explanation:
[Your explanation for interpretation tasks]

Prediction:
[Your predicted next row for interpretation tasks]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "interpret" in instructions.lower():
            criteria = ["The explanation should clearly describe the rule of the visual pattern.", "The prediction for the next row should follow the identified rule."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
