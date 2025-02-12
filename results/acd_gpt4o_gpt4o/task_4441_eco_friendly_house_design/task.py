class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Design a small eco-friendly house for a family of four. The house should be energy-efficient, use sustainable materials, and include at least three eco-friendly features such as solar panels, rainwater harvesting, and a green roof."
            },
            "2": {
                "criteria": "Design a small eco-friendly house for an urban setting. The house should maximize space usage, be energy-efficient, and include at least two innovative eco-friendly features such as a vertical garden and greywater recycling system."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to design a small eco-friendly house based on the following criteria:\n\n{t['criteria']}\n\nEnsure that your design is practical, includes detailed descriptions of the features, and explains how each feature contributes to the eco-friendliness of the house. Provide your response in plain text format using the following structure:\n\nDesign: [Your detailed design]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should be practical and feasible.",
            "The design should include detailed descriptions of the eco-friendly features.",
            "The design should explain how each feature contributes to the eco-friendliness of the house."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
