class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "device": "metaphor",
                    "example": "The world is a stage."
                }
            },
            "2": {
                "data": {
                    "device": "personification",
                    "example": "The sun smiled down on us."
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        device = t['data']['device']
        example = t['data']['example']
        return f"""Identify the literary device used in the following example and create an original example of the same device.

Example: {example}

Your response should include:
1. Identification: [Identify the literary device used in the example]
2. Original Example: [Create an original example of the same literary device]

Submit your response as a plain text string in the following format:

Identification: [Your identification]
Original Example: [Your original example]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The identification should correctly name the literary device used in the example.",
            "The original example should clearly demonstrate the same literary device.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
