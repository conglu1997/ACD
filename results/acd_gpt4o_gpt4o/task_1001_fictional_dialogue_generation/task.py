class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Two characters, Alice and Bob, are stuck in an elevator. Alice is claustrophobic and Bob is trying to keep her calm. Write a dialogue between them."},
            "2": {"scenario": "A futuristic setting where a human, Jamie, is having a conversation with their personal AI assistant, Alex, about planning a surprise birthday party. Write a dialogue between them."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a creative and contextually appropriate dialogue between the given characters in the provided scenario. Ensure that the dialogue is engaging, maintains character consistency, and fits the context of the scenario. Provide your response in plain text format.\n\nScenario: {t['scenario']}\n\nResponse format:\n[Your dialogue here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be engaging.", "The dialogue should maintain character consistency.", "The dialogue should fit the context of the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
