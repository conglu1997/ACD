class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "The signing of the Treaty of Versailles in 1919",
                "prompt": "Analyze the historical significance of the Treaty of Versailles and its impact on Europe."
            },
            "2": {
                "scenario": "The fall of the Berlin Wall in 1989",
                "prompt": "Explain the events leading up to the fall of the Berlin Wall and its implications for the Cold War."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical scenario: '{t['scenario']}'. Provide a detailed explanation that includes:
1. A brief overview of the scenario.
2. The historical context surrounding the event.
3. The key figures involved.
4. The short-term and long-term implications of the event.

Submit your response as a plain text string in paragraph format. Ensure your analysis is coherent, well-structured, and historically accurate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should be historically accurate and relevant to the given scenario.",
            "The explanation should cover the historical context, key figures, and implications of the event.",
            "The response should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
