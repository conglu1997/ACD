class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A friend is feeling down because they failed an important exam. Respond to your friend to comfort them. Make sure to acknowledge their feelings, offer support, and suggest a positive outlook."},
            "2": {"scenario": "You are meeting a new colleague for the first time at a company social event. Start a conversation to get to know them better and make them feel welcome. Ask about their background, interests, and how they are finding the new job."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a realistic social interaction based on the following scenario:

{t["scenario"]}

Your response should be empathetic, appropriate for the situation, and demonstrate good conversational skills. Format your response as a dialogue or a piece of advice in plain text. Ensure your response is natural and realistic, and avoid overly formal language."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be empathetic.",
            "The response should be appropriate for the situation.",
            "The response should demonstrate good conversational skills.",
            "The response should be realistic and natural."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
