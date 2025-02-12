class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "historical_context": "Ancient Greece during the Peloponnesian War", "prompt": "Describe a day in the life of a soldier in the Athenian army."},
            "2": {"type": "analyze", "historical_context": "Renaissance Italy", "text": "In the early 16th century, the political landscape of Italy was dominated by city-states such as Florence, Venice, and Rome. These city-states were centers of art, culture, and political intrigue.", "question": "How did the political structure of Renaissance Italy influence its cultural achievements?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generate':
            return f"""Your task is to generate a response based on the specified historical context. Here is the context:

Historical Context: {t['historical_context']}

Prompt: {t['prompt']}

Ensure your response is historically accurate, contextually appropriate, and detailed. Provide your submission in plain text format."""
        elif t['type'] == 'analyze':
            return f"""Your task is to analyze the given text based on the specified historical context. Here is the context and text:

Historical Context: {t['historical_context']}

Text: {t['text']}

Question: {t['question']}

Ensure your response accurately addresses the question, is contextually appropriate, and demonstrates a deep understanding of the historical context. Provide your submission in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'generate':
            criteria.append("The response should be historically accurate and contextually appropriate.")
        elif t['type'] == 'analyze':
            criteria.append("The analysis should accurately address the question and demonstrate a deep understanding of the historical context.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
