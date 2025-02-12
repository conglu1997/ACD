class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement", "questions": ["What is quantum entanglement?", "Why is it important in quantum computing?"]},
            "2": {"concept": "Photosynthesis", "questions": ["Describe the process of photosynthesis.", "What are the main products and reactants involved?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        questions = "\n".join(t["questions"])
        return f"""Explain the following scientific concept in simple terms and answer the specified questions about it.\nConcept: {concept}\nQuestions:\n{questions}\nEnsure your explanation is clear, concise, and accurate. Submit your response as a plain text string with each answer on a new line, labeled with the respective question number. For example:\n1. Your answer to the first question\n2. Your answer to the second question\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
