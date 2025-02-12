class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Select all columns from the employees table where the department is 'Sales'."},
            "2": {"description": "Count the number of distinct customers from the orders table."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following natural language description into an SQL query. Ensure the query is syntactically correct and formatted properly:

{t['description']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The SQL query should accurately reflect the natural language description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
