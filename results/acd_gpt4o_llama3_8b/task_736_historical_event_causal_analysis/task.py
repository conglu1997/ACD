class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": "The assassination of Archduke Franz Ferdinand, The start of World War I", "synthetic_examples": ["The fall of the Berlin Wall, The reunification of Germany"]},
            "2": {"events": "The signing of the Treaty of Versailles, The rise of Adolf Hitler", "synthetic_examples": ["The invention of the printing press, The spread of the Renaissance"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Analyze the following historical events and identify the causal relationships between them. Explain how the first event led to the second event in a logical and coherent manner. Your analysis should be clear, concise, and demonstrate a deep understanding of historical causality.

Events: {t['events']}

Additional examples:
{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            from src.eval_helper import eval_with_llm_judge
            instructions = TaskFamily.get_instructions(t)
            criteria = [f"The response should logically explain the causal relationship between the events: {t['events']}"]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            return 0.0
