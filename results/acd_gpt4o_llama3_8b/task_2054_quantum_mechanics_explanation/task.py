class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement",
                "prompt": "Explain the concept of quantum entanglement and its implications in quantum computing. Ensure your explanation covers the key aspects, including the EPR paradox and Bell's theorem, is logically structured, scientifically accurate, and at least 300 words long."
            },
            "2": {
                "concept": "Schrodinger's Cat",
                "prompt": "Explain the thought experiment of Schrödinger's Cat and its significance in quantum mechanics. Ensure your explanation covers the key aspects, including the concept of superposition and the observer effect, is logically structured, scientifically accurate, and at least 300 words long."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following concept in quantum mechanics based on the given prompt. Ensure your explanation is detailed, logically structured, scientifically accurate, and at least 300 words long.

Concept: {t['concept']}
Prompt: {t['prompt']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be detailed and logically structured.",
            "The explanation should cover the key aspects mentioned in the prompt.",
            "The explanation should be scientifically accurate.",
            "The explanation should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
