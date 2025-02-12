class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The fall of the Berlin Wall in 1989"
            },
            "2": {
                "historical_event": "The signing of the Treaty of Versailles in 1919"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following historical event: '{t['historical_event']}'.\n\nProvide a detailed analysis of the event, including its causes and immediate consequences. Then, based on historical continuity and causal reasoning, predict at least two plausible future scenarios that could emerge from this event. Your response should be at least 300 words long, well-structured, and coherent. Ensure your predictions are logical and consider various historical factors. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should include the causes and immediate consequences of the historical event.",
            "The response should predict at least two plausible future scenarios based on historical continuity and causal reasoning.",
            "The response should be at least 300 words long.",
            "The response should be well-structured and coherent.",
            "The historical analysis should be accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
