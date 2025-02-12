class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A landlord and a tenant negotiating the terms of a lease renewal."},
            "2": {"scenario": "Two business partners discussing the division of profits in a new venture."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"""Generate a negotiation dialogue between two parties based on the following scenario:

Scenario: {scenario}

The dialogue should be coherent, contextually appropriate, and demonstrate strategic thinking and empathy from both parties. Include at least five exchanges (ten lines) of dialogue. Submit your dialogue as a plain text string in the following format:

Person A: [First line]
Person B: [Second line]
Person A: [Third line]
Person B: [Fourth line]
...
Ensure each line is labeled with the speaker's name and follows logically from the previous one.

Criteria for evaluation:
1. Coherence: The dialogue should be logically structured and contextually appropriate.
2. Empathy: Each party should acknowledge and respond to the other party's concerns.
3. Strategic Thinking: The dialogue should show negotiation strategies, such as compromise, persuasion, or concession."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be logically structured and contextually appropriate.",
            "Each party should acknowledge and respond to the other party's concerns.",
            "The dialogue should show negotiation strategies, such as compromise, persuasion, or concession."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
