class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "In a country, there are only two types of people: knights and knaves. Knights always tell the truth, and knaves always lie. You meet three people: A, B, and C. A says, 'B is a knight.' B says, 'A and C are of the same type.' C says, 'B is a knave.' Determine who is a knight and who is a knave, if possible.",
                "solution": "A is a knave, B is a knight, C is a knave."
            },
            "2": {
                "puzzle": "You have 12 identical-looking balls, but one of them is either heavier or lighter than the rest. You also have a balance scale. Determine the minimum number of weighings required to identify the odd ball and whether it is heavier or lighter. Explain your reasoning clearly.",
                "solution": "3 weighings." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logic puzzle:

{t['puzzle']}

Provide your solution in a clear and concise format. Submit your response as a plain text string in the following format:

Solution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ['The solution should be correct and match the expected answer.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
