class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "time", "analogy": "A tree is to a forest as a star is to the sky."},
            "2": {"concept": "knowledge", "analogy": "A key is to a lock as a clue is to a mystery."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Generate an analogy based on the given concept: '{t["concept"]}'. Your analogy should be creative, accurate, and not overly simplistic. Avoid analogies that are too direct or obvious; instead, aim for analogies that capture the essence of the concept in a nuanced way.

2. Interpret the provided analogy: '{t["analogy"]}'. Explain the relationship between the elements in the analogy and what it represents. Ensure your interpretation provides a deep understanding of the analogy.

Submit your responses as a plain text string in the following format:

Analogy Generation: [Your analogy]
Analogy Interpretation: [Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated analogy should be creative and accurately represent the given concept.",
            "The generated analogy should not be overly simplistic or direct.",
            "The interpretation should clearly explain the relationship between the elements in the provided analogy and what it represents.",
            "The interpretation should provide a deep understanding of the analogy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
