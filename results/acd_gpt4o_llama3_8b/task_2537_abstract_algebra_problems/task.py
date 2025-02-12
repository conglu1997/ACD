class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Let G be a group with the binary operation *. Prove that if G is a group, then the identity element e of G is unique."},
            "2": {"problem": "Let R be a commutative ring with unity. Show that if a and b are elements of R such that a * b = 0, then either a = 0 or b = 0 if and only if R is an integral domain."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t['problem']
        return f"""Solve the following problem involving concepts from abstract algebra:

Problem: {problem}

Provide a detailed solution with all necessary steps and justifications. Your solution should be well-structured, logically sound, and complete. Submit your response as a plain text string in the following format:

Solution: [Your detailed solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be well-structured and logically sound.",
            "The solution should include all necessary steps and justifications.",
            "The solution should be complete and address all parts of the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
