class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a customer service representative helping a customer with an issue with their order. The customer received the wrong item and is frustrated."},
            "2": {"scenario": "You are a teacher helping a student understand a complex topic in mathematics, specifically the concept of limits in calculus. The student is struggling and needs clear explanations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a multi-turn dialogue based on the given scenario. Maintain coherence and context throughout the conversation.

Scenario: {t['scenario']}

Start the dialogue by greeting the other party and introducing yourself. Respond to each prompt and keep the conversation relevant to the scenario. Make sure your responses are clear, helpful, and maintain a natural flow of conversation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should maintain coherence and context.",
            "The responses should be relevant to the scenario.",
            "The conversation should flow naturally.",
            "The responses should be clear and helpful." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
