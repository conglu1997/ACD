class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Prove that the group of integers under addition, \( \mathbb{Z} \), is an abelian group. Include a detailed explanation of the group properties and why they hold for \( \mathbb{Z} \)."},
            "2": {"prompt": "Show that the set of all 2x2 invertible matrices with real entries, under matrix multiplication, forms a group. Provide a detailed proof including the verification of group properties: closure, associativity, identity, and inverses."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following problem in abstract algebra. Provide a clear and detailed proof or solution, ensuring that you use appropriate mathematical notation and rigor. Structure your response with a step-by-step explanation and include any necessary definitions or theorems.

{t['prompt']}

Response format:
1. Introduction
2. Step-by-step proof or solution
3. Conclusion
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be mathematically correct.",
            "The solution should be clear and detailed.",
            "The solution should use appropriate mathematical notation.",
            "The solution should demonstrate logical reasoning and rigor.",
            "The solution should follow the specified response format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
