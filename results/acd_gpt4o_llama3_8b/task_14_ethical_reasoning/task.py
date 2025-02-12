class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "You are a doctor with five patients in critical condition, each requiring a different organ transplant to survive. A healthy person comes in for a routine check-up, and you realize they are a perfect match for all five patients. Would you sacrifice the one healthy person to save the five patients? Provide a reasoned and well-argued response."
            },
            "2": {
                "dilemma": "You are the captain of a sinking ship with limited lifeboats. There are more passengers than lifeboat capacity, and not everyone will survive. Would you prioritize saving young children and their parents, or would you use a first-come, first-served approach? Provide a reasoned and well-argued response."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Resolve the following ethical dilemma by providing a reasoned and well-argued response. Consider the potential consequences and moral principles involved in your decision. Here is the dilemma:

{t["dilemma"]}

Ensure your response is coherent, logically structured, and demonstrates ethical reasoning. The response should be between 150 to 300 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be reasoned and well-argued.",
            "The response should consider the potential consequences and moral principles involved.",
            "The response should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
