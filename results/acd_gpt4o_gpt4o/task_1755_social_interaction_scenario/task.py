class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A friend is upset because they feel ignored at a party."},
            "2": {"interaction": "Person A is expressing frustration to Person B about a missed deadline, and Person B is responding."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scenario' in t:
            return f"""Generate a plausible next step in the following social interaction scenario:

Scenario: {t['scenario']}

Describe how the interaction could proceed in a way that resolves the issue positively. Your response should include dialogue and actions for both parties. Provide your response in plain text format, and ensure it is at least 150 words."""
        else:
            return f"""Analyze the following social interaction:

Interaction: {t['interaction']}

Your analysis should include the dynamics of the interaction, the emotions involved, and any potential outcomes. Provide your response in plain text format, structured with an introduction, body, and conclusion. Your analysis should be at least 200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'scenario' in t:
            criteria = [
                "The response should be a plausible continuation of the given scenario.",
                "The interaction should aim to resolve the issue positively.",
                "The dialogue and actions should be realistic and empathetic.",
                "The response should be at least 150 words."
            ]
        else:
            criteria = [
                "The analysis should be detailed and cover the dynamics, emotions, and potential outcomes of the interaction.",
                "The explanation should be coherent and logically structured.",
                "The analysis should be at least 200 words."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
