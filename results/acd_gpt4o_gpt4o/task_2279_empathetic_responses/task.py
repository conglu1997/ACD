class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Your friend just lost their job unexpectedly and is feeling very down."
            },
            "2": {
                "scenario": "A colleague at work has been working extra hours but hasn't been recognized for their efforts. They feel unappreciated and demotivated."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate an empathetic response to the following scenario:\n\n{t['scenario']}\n\nEnsure that your response is supportive, understanding, and demonstrates emotional intelligence. The response should be context-specific and avoid generic statements. Provide your response in plain text format with a length of at least 100 words."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be supportive and understanding.",
            "The response should demonstrate emotional intelligence.",
            "The response should be contextually appropriate and empathetic.",
            "The tone of the response should be appropriate to the scenario.",
            "The response should avoid generic statements and be at least 100 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
