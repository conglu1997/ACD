class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Plastic pollution in the oceans is a growing concern. Propose a comprehensive strategy to reduce plastic waste entering the oceans, considering scientific, economic, and social factors."},
            "2": {"problem": "Deforestation is leading to loss of biodiversity and contributing to climate change. Suggest a multi-faceted approach to combat deforestation, taking into account environmental, economic, and social dimensions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['problem']}

Your response should include:
1. A detailed description of the proposed solution.
2. Scientific reasoning to support your solution.
3. Consideration of economic and social factors.
Ensure your proposal is practical, comprehensive, and well-justified. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be detailed and practical.",
            "The solution should be supported by scientific reasoning.",
            "The solution should consider economic and social factors.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0