class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event_description": "The signing of the Magna Carta in 1215.", "question": "What were the main reasons behind the signing of the Magna Carta, and what were its immediate and long-term impacts on the English monarchy and society?"},
            "2": {"event_description": "The Industrial Revolution in the 18th century.", "question": "How did the Industrial Revolution transform European societies, and what were some of the key factors that contributed to its onset?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with a brief description of a historical event. Your task is to interpret the event and reason about its causes and implications. Ensure that your response is comprehensive, accurate, and demonstrates a deep understanding of the historical context.

Event Description: {t['event_description']}

Question: {t['question']}

Your response should follow this format:
1. Introduction: Briefly introduce the event.
2. Causes: Discuss the main reasons behind the event.
3. Immediate Impacts: Describe the immediate impacts of the event.
4. Long-term Impacts: Explain the long-term implications of the event.
5. Conclusion: Summarize your response.

Example response format:
1. Introduction: The signing of the Magna Carta in 1215 was a significant event in English history.
2. Causes: The main reasons behind the signing of the Magna Carta were...
3. Immediate Impacts: The immediate impacts of the Magna Carta included...
4. Long-term Impacts: The long-term implications of the Magna Carta were...
5. Conclusion: In summary, the Magna Carta...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the causes and implications of the event.",
            "The response should demonstrate a deep understanding of the historical context.",
            "The response should be well-organized and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
