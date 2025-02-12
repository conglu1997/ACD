class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You have been given a million dollars to start a new business. Generate a detailed business plan, including the type of business, target market, initial investment areas, and projected timeline for the first year."},
            "2": {"scenario": "You are tasked with organizing a week-long international conference on renewable energy. Generate a detailed plan, including key topics, potential speakers, venue selection, and any logistical considerations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed plan for the following hypothetical scenario:

Scenario: {t["scenario"]}

Ensure your plan is comprehensive, logical, and creative. Provide your response in plain text format and structure it as follows:

1. Overview
2. Detailed Plan
3. Timeline
4. Any additional considerations"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should include a clear overview.",
            "The plan should be logically structured and comprehensive.",
            "The timeline should be detailed and realistic.",
            "The plan should demonstrate creativity and strategic thinking.",
            "All sections (Overview, Detailed Plan, Timeline, Additional Considerations) should be present."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
