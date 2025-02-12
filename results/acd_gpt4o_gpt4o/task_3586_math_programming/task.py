class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Find all prime numbers up to 100."},
            "2": {"problem": "Calculate the Fibonacci sequence up to the 20th term."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to write a Python script to solve the following mathematical problem:\n\n{problem}\n\nEnsure your script is correctly formatted and solves the problem accurately. Provide your solution as a Python code block."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The Python script should be correctly formatted.",
            "The script should solve the problem accurately.",
            "The solution should be provided as a Python code block."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
