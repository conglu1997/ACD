class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "calculus",
                "task": "Generate a complex calculus problem and provide a detailed solution to it. Ensure the problem involves multiple steps and covers advanced concepts such as integrals, derivatives, or series."
            },
            "2": {
                "topic": "linear algebra",
                "task": "Generate a complex linear algebra problem and provide a detailed solution to it. Ensure the problem involves multiple steps and covers advanced concepts such as eigenvalues, eigenvectors, or matrix decompositions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to generate a complex mathematical problem based on the given topic and provide a detailed solution to it. Ensure the problem involves multiple steps and covers advanced concepts within the topic.

Topic: {t['topic']}

Task: {t['task']}

Submit your response as a plain text string in the following format:

Problem: [Your problem]
Solution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The problem should be complex and involve multiple steps.",
            "The problem should cover advanced concepts within the given topic.",
            "The solution should be detailed and correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
