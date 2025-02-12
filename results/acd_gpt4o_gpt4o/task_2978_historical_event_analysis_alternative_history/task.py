class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Fall of the Berlin Wall", "year": 1989},
            "2": {"event": "The Moon Landing", "year": 1969}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: analysis and creation.

Part 1: Analysis
Analyze the given historical event, considering its causes, key players, and impact on the world.

Event: {t['event']}
Year: {t['year']}

Provide your analysis in the following format:
Analysis:
- Causes: [Describe the causes of the event]
- Key Players: [Identify the key players involved]
- Impact: [Explain the impact of the event on the world]

Part 2: Alternative History
Create a scenario where the outcome of the historical event is different. Describe how this alternative outcome could have changed the course of history. Ensure your scenario is coherent, plausible, and historically grounded.

Provide your alternative history in the following format:
Alternative History:
- Scenario: [Describe the alternative outcome]
- Changes: [Explain how this outcome changes the course of history]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately describe the causes, key players, and impact of the event.",
            "The alternative history should be coherent, plausible, and historically grounded.",
            "The submission should cover both parts: analysis and alternative history.",
            "The response should follow the specified format." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
