class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of the first n natural numbers is (n * (n + 1)) / 2."},
            "2": {"proof": "Proof by induction:\nBase case: For n = 1, the sum is 1, and 1 * (1 + 1) / 2 = 1, which is true.\nInductive step: Assume the statement holds for n = k, i.e., 1 + 2 + ... + k = k * (k + 1) / 2.\nConsider n = k + 1:\n1 + 2 + ... + k + (k + 1) = (k * (k + 1)) / 2 + (k + 1)\n = (k * (k + 1) + 2 * (k + 1)) / 2\n = (k + 1) * (k + 2) / 2\nThus, the statement holds for n = k + 1. By induction, the statement is true for all natural numbers n.", "questions": ["What is the base case in this proof?", "How is the inductive step proven?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "statement" in t:
            return f"""Generate a mathematical proof for the following statement:\n\n{t['statement']}\n\nProvide a clear and detailed proof using appropriate mathematical reasoning."""
        else:
            return f"""Read the following mathematical proof and answer the questions below:\n\n{t['proof']}\n\nQuestions:\n1. {t['questions'][0]}\n2. {t['questions'][1]}\n\nProvide your answers as plain text strings in the following format:\nAnswer 1: [Your answer]\nAnswer 2: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "statement" in t:
            criteria = ["The proof should be logically valid.", "The proof should be coherent and detailed.", "The proof should use appropriate mathematical reasoning."]
        else:
            criteria = [
                "The answers should correctly address the questions based on the provided proof.",
                "The answers should demonstrate comprehension of the proof steps.",
                "The answers should be logically valid and coherent."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
