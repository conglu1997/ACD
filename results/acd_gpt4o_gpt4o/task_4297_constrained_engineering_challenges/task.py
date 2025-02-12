class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design a bridge that can hold a minimum weight of 1000 kg across a 10-meter gap using only the following materials: 10 steel beams (each 1 meter long), 20 wooden planks (each 2 meters long), and 30 meters of rope.",
                "resources": ["10 steel beams (1 meter each)", "20 wooden planks (2 meters each)", "30 meters of rope"]
            },
            "2": {
                "problem": "Design a water filtration system that can provide clean drinking water for a small village using only the following materials: 2 sand filters, 5 charcoal filters, 10 meters of PVC pipe, and 1 water pump.",
                "resources": ["2 sand filters", "5 charcoal filters", "10 meters of PVC pipe", "1 water pump"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a solution to the following engineering problem using only the specified resources. Be creative and detailed in your explanation.

Problem: {t["problem"]}
Resources: {', '.join(t["resources"])}

Your response should include:
1. A detailed description of your design.
2. Justification for your choice of materials and their use.
3. Any potential challenges or limitations of your design and how you would address them.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should use only the specified resources.",
            "The design should address the problem effectively.",
            "The explanation should be clear and detailed.",
            "The justification for the choice of materials should be logical and well-reasoned.",
            "Any challenges or limitations should be addressed thoughtfully."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
