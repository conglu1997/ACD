class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"content": "An advertisement for a winter clothing line", "original_context": "North America", "target_context": "Japan"},
            "2": {"content": "A short story about a summer festival", "original_context": "Brazil", "target_context": "India"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to adapt the following piece of content to fit a different cultural context:

Content: {t['content']}

Original Context: {t['original_context']}

Target Context: {t['target_context']}

Ensure that the adapted content maintains the original intent and message while making it culturally relevant to the target context. The adapted content should be between 100 and 300 words. Provide your adapted content in plain text format.

Example:

Original Context: An advertisement for a summer sale in the USA.
Target Context: Adapted for the UK.
Original: "Get ready for the hottest deals this summer! Visit our stores for up to 50% off on all summer apparel."
Adapted: "Prepare for the best deals this summer! Visit our stores for up to 50% off on all summer clothing.""" 
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The adapted content should maintain the original intent and message.",
            "The adaptation should be culturally relevant and appropriate for the target context.",
            "The adaptation should be clear and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0