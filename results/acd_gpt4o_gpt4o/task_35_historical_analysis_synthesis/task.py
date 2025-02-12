class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the causes and effects of the French Revolution. Provide a synthesized narrative that includes the main events, key figures, and the socio-political impact. Discuss both short-term and long-term effects. Incorporate multiple perspectives, including those of different social classes and political factions. Compare and contrast at least two different historiographical interpretations."},
            "2": {"prompt": "Discuss the key factors that led to the fall of the Roman Empire. Provide a synthesized narrative that includes the main events, key figures, and the socio-political impact. Address both internal and external factors. Incorporate multiple perspectives, including those of different regions and social classes. Compare and contrast at least two different historiographical interpretations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following historical event and provide a synthesized narrative. Ensure that your narrative includes the main events, key figures, and the socio-political impact. Discuss both short-term and long-term effects where applicable. Incorporate multiple perspectives and compare and contrast at least two different historiographical interpretations:

{t['prompt']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should include the main events.",
            "The narrative should mention key figures.",
            "The narrative should discuss the socio-political impact.",
            "The narrative should address both short-term and long-term effects where applicable.",
            "The narrative should address both internal and external factors where applicable.",
            "The narrative should incorporate multiple perspectives.",
            "The narrative should compare and contrast at least two different historiographical interpretations.",
            "The narrative should be coherent and well-synthesized."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
