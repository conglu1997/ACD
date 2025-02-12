class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Photosynthesis",
                "instructions": "Explain the process of photosynthesis in plants in a way that a high school student can understand. Your explanation should include the key steps: light absorption, water splitting, oxygen release, carbon dioxide fixation, and glucose production. Also, explain the overall significance of photosynthesis for life on Earth. Submit your explanation as a plain text string."
            },
            "2": {
                "phenomenon": "Quantum Entanglement",
                "instructions": "Generate an analogy to explain the concept of quantum entanglement to a layperson. Ensure that the analogy captures the essence of the phenomenon and is easy to understand. Your analogy should avoid technical jargon and focus on conveying the fundamental idea of entanglement. Submit your analogy as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given scientific phenomenon and generate the requested content.

Phenomenon: {t['phenomenon']}

Instructions: {t['instructions']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation or analogy should be clear and accurate.",
            "The content should be appropriate for the specified audience (high school student or layperson).",
            "The content should demonstrate a good understanding of the scientific phenomenon.",
            "The explanation or analogy should cover all requested aspects of the phenomenon."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
