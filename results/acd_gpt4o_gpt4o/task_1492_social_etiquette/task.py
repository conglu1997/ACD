class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are at a formal dinner party and someone accidentally spills their drink on you. How do you respond?"},
            "2": {"scenario": "You are meeting your partner's parents for the first time and they ask you about your future plans. How do you respond?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a social scenario. Your task is to generate an appropriate response that demonstrates good social etiquette and cultural awareness. Consider the context and the cultural norms that may apply.

Scenario: {t['scenario']}

Your response should be polite, respectful, and contextually appropriate.

Example Response:
Scenario: You are at a friend's birthday party and someone asks you to dance. How do you respond?
Response: Thank you for asking! I'd love to dance. Let's go!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be polite and respectful.",
            "The response should be contextually appropriate.",
            "The response should demonstrate cultural awareness."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
