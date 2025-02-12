class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"fields": ["biotechnology", "artificial intelligence"], "prompt": "Combine these fields to propose a new concept and explain its potential applications."},
            "2": {"fields": ["quantum physics", "psychology"], "prompt": "Combine these fields to propose a new concept and explain its potential applications."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        fields = ', '.join(t["fields"])
        return f"""Your task is to combine ideas from the following fields to create a new concept: {fields}. Explain the new concept and its potential applications in detail. Your explanation should be clear, logical, and demonstrate an understanding of both fields. Ensure that the concept is original and not a known idea. Provide your response in plain text format with the following structure:

- New Concept: [Your concept]
- Explanation: [Detailed explanation of the concept]
- Applications: [Potential applications of the concept]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should combine ideas from the given fields.", "The new concept should be original and innovative.", "The concept should be logically explained.", "The potential applications should be clearly described and plausible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
