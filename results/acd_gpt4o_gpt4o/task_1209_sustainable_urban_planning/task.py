class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"city_area": "a coastal city of 100,000 people in a developing nation", "existing_issues": ["frequent flooding", "high unemployment rate", "limited green spaces"]},
            "2": {"city_area": "an inland city of 500,000 people in a developed nation", "existing_issues": ["air pollution", "traffic congestion", "affordable housing shortage"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a sustainable urban plan for the following city area:

City Area: {t['city_area']}

Existing Issues: {', '.join(t['existing_issues'])}

Consider environmental, social, and economic factors in your plan. Your proposal should cover the following aspects:
1. Transportation
2. Housing
3. Green spaces
4. Economic development
5. Environmental sustainability

Provide a detailed proposal that includes specific measures to address the existing issues, promote sustainability, and improve the quality of life for residents. Ensure your proposal is clear, well-structured, and feasible. Provide your response in plain text format with sections for each of the aspects mentioned above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proposal should address all the existing issues mentioned.",
            "The proposal should consider environmental, social, and economic factors.",
            "The proposal should cover transportation, housing, green spaces, economic development, and environmental sustainability.",
            "The proposal should be clear, well-structured, and feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
