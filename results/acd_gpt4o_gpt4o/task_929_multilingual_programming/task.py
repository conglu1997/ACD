class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"language": "Python", "problem": "Write a function that takes a list of integers and returns the sum of all even numbers in the list."},
            "2": {"language": "JavaScript", "problem": "Write a function that takes a string and returns the string reversed."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a function in {t['language']} to solve the following problem:

Problem: {t['problem']}

Ensure that your solution is correct, syntactically valid, and follows the conventions of the specified programming language. Provide your solution in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be syntactically valid in {t['language']}.",
            "The solution should correctly solve the given problem.",
            "The solution should follow the conventions of the specified programming language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
