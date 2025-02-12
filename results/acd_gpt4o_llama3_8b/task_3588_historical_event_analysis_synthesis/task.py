class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Fall of the Berlin Wall in 1989", "hypothetical": "What if the Berlin Wall had not fallen in 1989?"},
            "2": {"event": "The signing of the Treaty of Versailles in 1919", "hypothetical": "What if the Treaty of Versailles had been more lenient towards Germany?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event and then synthesize a hypothetical scenario based on an alternate outcome:

Historical Event: {t['event']}

Hypothetical Scenario: {t['hypothetical']}

Your response should include:
1. A brief analysis of the historical event, including key facts and significance.
2. A detailed hypothetical scenario based on the alternate outcome, considering possible political, economic, and social impacts.

Submit your response as a plain text string with clearly labeled sections for 'Analysis' and 'Hypothetical Scenario'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief analysis of the historical event with key facts and significance.",
            "The hypothetical scenario should be detailed and consider political, economic, and social impacts.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
