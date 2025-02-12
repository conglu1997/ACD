class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Photosynthesis",
                "illustration_format": "text"
            },
            "2": {
                "concept": "Newton's Second Law of Motion",
                "illustration_format": "text"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t['concept']
        illustration_format = t['illustration_format']
        return f"""Explain the scientific concept of {concept} clearly and engagingly. Use an illustrative example to help explain the concept. Ensure that your explanation is accurate, easy to understand, and effectively communicates the key principles of the concept. Your illustration should be in {illustration_format} format.

Submit your response as a plain text string in the following format:

Explanation: [Your explanation]
Illustrative Example: [Your illustrative example]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be accurate and cover the key principles of the concept.",
            "The explanation should be clear and easy to understand.",
            "The illustrative example should effectively support the explanation and make the concept more engaging.",
            "The overall response should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
