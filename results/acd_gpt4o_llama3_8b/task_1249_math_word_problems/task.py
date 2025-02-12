class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Jane has 3 apples. She buys 4 more apples. How many apples does she have in total?"},
            "2": {"criteria": "Create a word problem involving multiplication, where the main character is a farmer and the quantities involve fields and crops. The problem should require at least two steps to solve."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'problem' in t:
            return f"""Solve the following mathematical word problem:

{t['problem']}

Provide your solution as a plain text string, showing all necessary calculations and the final answer in the following format:

Calculations: [Your calculations]
Answer: [Your final answer]

Example:
Calculations: 3 + 4 = 7
Answer: 7"""
        elif 'criteria' in t:
            return f"""Generate a new mathematical word problem based on the following criteria:

{t['criteria']}

Ensure that the problem is clear, solvable, and mathematically correct. Submit your problem as a plain text string in the following format:

Problem: [Your generated word problem]

Example:
Problem: A farmer has 5 fields. Each field has 4 rows of crops. How many rows of crops are there in total?"""
        else:
            raise ValueError("Invalid task data.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
