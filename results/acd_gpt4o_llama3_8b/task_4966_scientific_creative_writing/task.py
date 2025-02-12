class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement"
            },
            "2": {
                "concept": "The Fibonacci Sequence"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a piece of creative writing based on the following scientific or mathematical concept:

Concept: {t['concept']}

Your writing should creatively incorporate the concept in a way that is both engaging and informative. It can be a short story, a poem, or any other form of creative expression. Ensure that the concept is accurately represented and plays a central role in your piece. Submit your response as a plain text string in the following format:

Creative Writing: [Your writing here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The writing should be engaging and creative.",
            "The scientific or mathematical concept should be accurately represented.",
            "The concept should play a central role in the piece."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
