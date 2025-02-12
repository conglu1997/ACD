class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "complex_concept": "Quantum Entanglement",
                "simple_terms": "Explain how two particles can be interconnected in such a way that the state of one instantly influences the state of the other, even when separated by large distances, using an everyday analogy."
            },
            "2": {
                "complex_concept": "Blockchain Technology",
                "simple_terms": "Explain how a blockchain works as a decentralized ledger that records transactions across many computers, ensuring security and transparency, using an everyday analogy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an educational analogy to explain the following complex concept using simpler, everyday terms:

Complex Concept: {t['complex_concept']}

Task: {t['simple_terms']}

Ensure that your analogy is clear, accurate, and easy to understand. Submit your analogy as a plain text string in the following format:

Analogy: [Your analogy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogy should accurately represent the complex concept.",
            "The analogy should be easy to understand and relatable to everyday terms.",
            "The analogy should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
