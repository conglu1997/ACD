class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write a pseudocode to find the largest number in an array of integers."},
            "2": {"pseudocode": "1. Start\n2. Initialize a variable 'max' with the value of the first element of the array\n3. For each element 'num' in the array\n   a. If 'num' is greater than 'max'\n      i. Set 'max' to 'num'\n4. End For\n5. Return 'max'\n6. End"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            instructions = f"""Your task is to write a pseudocode based on the following natural language description:\n\nDescription: {t['description']}\n\nEnsure that your pseudocode is clear, logically structured, and accurately represents the steps needed to solve the problem. Provide your pseudocode in plain text format."""
        else:
            instructions = f"""Your task is to interpret the following pseudocode into a natural language description:\n\nPseudocode: {t['pseudocode']}\n\nEnsure that your description is clear, logically structured, and accurately conveys the steps outlined in the pseudocode. Provide your description in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'description' in t:
            criteria.append("The pseudocode should accurately represent the steps needed to solve the problem described.")
            criteria.append("The pseudocode should be clear and logically structured.")
        else:
            criteria.append("The description should accurately convey the steps outlined in the pseudocode.")
            criteria.append("The description should be clear and logically structured.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
