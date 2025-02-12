class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "derivative",
                "prompt": "Explain the concept of a derivative using a creative analogy."
            },
            "2": {
                "concept": "integral",
                "prompt": "Explain the concept of an integral using a creative analogy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a creative analogy to explain the following mathematical concept:

Concept: {t['concept']}

Prompt: {t['prompt']}

Ensure that your analogy is clear, creative, and accurately represents the mathematical concept. Provide a detailed explanation of how your analogy relates to the concept. Additionally, include examples of how this analogy helps in understanding the concept in different contexts. Your response should be in plain text format as follows:

Analogy: [Your analogy]
Explanation: [Your explanation]
Examples: [Your examples]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should be creative and clear.",
            "The analogy should accurately represent the mathematical concept.",
            "The explanation should detail how the analogy relates to the concept.",
            "The examples should demonstrate the analogy's applicability in different contexts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
