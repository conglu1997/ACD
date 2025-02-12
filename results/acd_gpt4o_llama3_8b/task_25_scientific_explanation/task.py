class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Photosynthesis",
                "analogy": "Explain photosynthesis as if you are describing it to a 10-year-old using an analogy."
            },
            "2": {
                "concept": "Quantum Entanglement",
                "analogy": "Explain quantum entanglement as if you are describing it to a 10-year-old using an analogy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific concept in simple terms as if you are describing it to a 10-year-old. Additionally, provide an analogy to make the concept more understandable. Here is the concept:

{t["concept"]}

Ensure your explanation is clear, easy to understand, and includes a creative analogy. Your response should be coherent and logically structured. Submit your explanation and analogy as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and easy to understand.",
            "The analogy should be creative and help in understanding the concept.",
            "The response should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
