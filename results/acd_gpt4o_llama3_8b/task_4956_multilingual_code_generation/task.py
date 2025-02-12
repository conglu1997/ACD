class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Given a list of integers, return a new list with each integer squared.", "languages": ["Python", "JavaScript"]},
            "2": {"problem": "Write a function that calculates the factorial of a number.", "languages": ["Java", "C++"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        languages = t["languages"]
        return f"""Generate code snippets that solve the following problem in both {languages[0]} and {languages[1]}:

Problem: {problem}

Ensure that each code snippet is syntactically correct and solves the problem as described. The code should not rely on any external libraries or dependencies that are not standard for the specified languages. Submit your response as a plain text string in the following format:

{languages[0]} Code:
[Your code in {languages[0]}]

{languages[1]} Code:
[Your code in {languages[1]}]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The code snippets should be syntactically correct in both specified languages.",
            "Each code snippet should correctly solve the given problem.",
            "The code should not rely on any external libraries or dependencies that are not standard for the specified languages."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
