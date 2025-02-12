class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The American Revolution", "alternative_outcome": "The British won the war"},
            "2": {"event": "The fall of the Berlin Wall", "alternative_outcome": "The Berlin Wall never fell"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to reimagine the given historical event with the specified alternative outcome. Explain how this different outcome would have altered the course of history and its potential impact on the modern world. Ensure your analysis is detailed, logical, and well-structured. Provide your response in the following format:

Event: {t['event']}
Alternative Outcome: {t['alternative_outcome']}

Analysis:
1. Immediate Consequences: [Describe the immediate consequences of the alternative outcome]
2. Long-term Impact: [Analyze the long-term impact on global politics, economy, and society]
3. Modern World: [Explain how the modern world would be different as a result of this alternative outcome]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and logical.",
            "The immediate consequences should be well-explained.",
            "The long-term impact should be thoroughly analyzed.",
            "The impact on the modern world should be clearly described.",
            "The response should demonstrate a strong understanding of the historical event."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
