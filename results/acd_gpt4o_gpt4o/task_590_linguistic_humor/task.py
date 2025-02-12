class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "food", "pun": "I don't trust people who do acupuncture. They're back stabbers."},
            "2": {"context": "technology", "pun": "I changed my iPod's name to Titanic. It's syncing now."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "context" in t:
            context = t["context"]
            return f"Your task is to generate a pun based on the following context: {context}. Ensure your pun is clever and relevant to the context. Provide your pun in plain text format."
        elif "pun" in t:
            pun = t["pun"]
            return f"Your task is to interpret the following pun and explain why it is humorous: {pun}. Provide your explanation in plain text format. Your response should identify the wordplay or double meaning used in the pun and explain why it is humorous."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "context" in t:
            criteria = [
                "The pun should be clever and relevant to the given context.",
                "The pun should demonstrate a play on words or double meaning."]
        elif "pun" in t:
            criteria = [
                "The explanation should accurately interpret the humor in the pun.",
                "The explanation should identify the wordplay or double meaning used in the pun."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
