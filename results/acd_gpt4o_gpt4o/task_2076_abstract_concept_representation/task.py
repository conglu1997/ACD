class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "freedom"},
            "2": {"concept": "time"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a creative story or description that metaphorically represents the following abstract concept:

Concept: {t['concept']}

Your response should be at least 150 words long and should provide a clear, metaphorical representation of the concept. Be creative and ensure that your narrative or description conveys the essence of the abstract idea. 

Please provide your response in the following format:

Response: [Your story or description here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story or description should be at least 150 words long.",
            "The story or description should metaphorically represent the abstract concept provided.",
            "The narrative should be coherent and creative.",
            "The response should be provided in the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
