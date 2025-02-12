class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire", "description": "Analyze the fall of the Roman Empire. Identify the key factors that led to its decline and collapse. Make connections to any other historical events or periods that share similar factors."},
            "2": {"event": "The Industrial Revolution", "description": "Analyze the Industrial Revolution. Identify the key factors that contributed to its onset and development. Make connections to any other historical events or periods that share similar factors."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event:\n\nEvent: {t['event']}\n\n{t['description']}\n\nSubmit your analysis as a plain text string. Ensure your analysis is detailed, logically sound, and demonstrates a deep understanding of the historical context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should identify key factors leading to the historical event.", "The response should make connections to other historical events or periods.", "The response should be logically sound and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
