class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A mid-sized city is experiencing rapid population growth. The current infrastructure is struggling to keep up with the increased demand for housing, transportation, and public services. The city is also facing environmental challenges such as air pollution and limited green spaces. Provide a comprehensive urban planning recommendation to address these issues.",
                "factors": ["population growth", "infrastructure", "environmental impact", "community well-being"]
            },
            "2": {
                "scenario": "A coastal town is planning to expand its tourism sector to boost the local economy. However, there are concerns about the environmental impact of increased tourism, including waste management, water usage, and the preservation of natural habitats. Provide a detailed urban planning strategy that balances economic growth with environmental sustainability and community interests.",
                "factors": ["economic growth", "environmental sustainability", "community interests"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following urban development scenario and provide a comprehensive recommendation based on the given factors.

Scenario: {t['scenario']}

Factors to consider: {', '.join(t['factors'])}

Your recommendation should be detailed, taking into account the various factors and their interdependencies. Ensure your recommendation is practical and balances the needs of the community, environment, and infrastructure. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recommendation should be comprehensive and address all given factors.",
            "The recommendation should demonstrate an understanding of the interdependencies between the factors.",
            "The recommendation should be practical and feasible.",
            "The recommendation should balance the needs of the community, environment, and infrastructure.",
            "The recommendation should be presented in a clear and structured format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
