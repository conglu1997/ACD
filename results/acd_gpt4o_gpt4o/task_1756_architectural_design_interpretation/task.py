class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "interpretation",
                "design_url": "https://example.com/design1.jpg"
            },
            "2": {
                "task_type": "generation",
                "constraints": "Design a modern residential house with eco-friendly features, including a green roof, solar panels, open living spaces, large windows for natural light, energy-efficient appliances, and a garden."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Your task is to interpret the following architectural design and describe its features in detail.

Design URL: {t['design_url']}

Consider elements such as the style, materials, function, and any unique characteristics. Provide your description in plain text format. Your description should be at least 150 words.

Expected format:
Description: [Your description]
"""
        elif t['task_type'] == 'generation':
            return f"""Your task is to generate a description for an architectural design based on the following constraints:

Constraints: {t['constraints']}

Ensure your description includes details about the style, materials, layout, eco-friendly features, large windows for natural light, energy-efficient appliances, and a garden. Provide your response in plain text format. Your description should be at least 200 words.

Expected format:
Design Description: [Your description]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = [
                "The description should accurately reflect the elements of the design.",
                "The description should include details about the style, materials, and function of the design.",
                "The description should mention any unique characteristics of the design.",
                "The description should be at least 150 words long."
            ]
        elif t['task_type'] == 'generation':
            criteria = [
                "The description should include details about the style and materials of the design.",
                "The description should include eco-friendly features such as a green roof and solar panels.",
                "The description should mention the layout, large windows for natural light, energy-efficient appliances, and a garden.",
                "The description should be at least 200 words long."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
