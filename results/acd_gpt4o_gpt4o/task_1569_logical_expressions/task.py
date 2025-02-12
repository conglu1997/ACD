class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "(A AND B) OR (NOT A AND C)",
                "variables": {"A": True, "B": False, "C": True}
            },
            "2": {
                "expression": "(X AND Y) OR (Y AND Z) OR (NOT X AND NOT Z)",
                "variables": {"X": False, "Y": True, "Z": False}
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        expression = t["expression"]
        variables = ', '.join([f'{k} = {v}' for k, v in t["variables"].items()])
        instructions = f"""Your task is to evaluate the following logical expression based on the given variable values:

Expression: {expression}

Variables: {variables}

Determine the truth value of the expression and provide a step-by-step explanation of your evaluation process. Your explanation should detail each logical operation in the order they are applied, showing intermediate results. Your response should be structured as follows:

Step-by-Step Explanation: [Your explanation]
Final Answer: [True/False]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        expression = t["expression"]
        variables = t["variables"]
        criteria = [f"The evaluation should be based on the logical expression '{expression}' and variable values {variables}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
