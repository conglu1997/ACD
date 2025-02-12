class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are at a formal dinner party and accidentally spill a drink on your host's expensive outfit."},
            "2": {"scenario": "You receive a gift from a friend that you do not like at all, and your friend is eagerly waiting for your reaction."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Read the following social etiquette scenario:

Scenario: {scenario}

Generate an appropriate and culturally sensitive response to this situation. Your response should demonstrate understanding of social norms, politeness, and empathy. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be appropriate for the given social situation.", "The response should demonstrate understanding of social norms, politeness, and empathy."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
