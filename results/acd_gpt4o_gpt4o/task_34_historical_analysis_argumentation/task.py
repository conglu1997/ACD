class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire in the 5th century.", "question": "What were the primary causes of the fall of the Roman Empire? Provide a reasoned argument based on historical evidence."},
            "2": {"event": "The signing of the Treaty of Versailles in 1919.", "question": "How did the Treaty of Versailles contribute to the conditions leading to World War II? Provide a reasoned analysis based on historical context."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        question = t["question"]
        instructions = f"""Your task is to analyze the following historical event and provide a reasoned argument or analysis based on the given facts and historical context:

Event: {event}

Question: {question}

Your analysis should be clear, logical, and well-supported by historical evidence. Ensure that you address all relevant aspects of the event and apply appropriate historical principles. Provide your analysis in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should address all relevant aspects of the historical event.",
            "The argument should be well-supported by historical evidence.",
            "The analysis should be clear, logical, and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
