class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pattern_description": "A circle with four smaller circles inside, each touching the larger circle's circumference.",
                "criteria": "Create a new pattern that includes a square and triangles."
            },
            "2": {
                "pattern_description": "A hexagon with alternating colored stripes and a central dot.",
                "criteria": "Create a new pattern that includes hexagons and circles in a symmetrical arrangement."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the given geometric pattern in detail and generate a new pattern based on the specified criteria.

Pattern Description: {t['pattern_description']}
Criteria: {t['criteria']}

Your response should include:
1. A detailed description of the given pattern, explaining its components and their arrangement.
2. A new pattern based on the specified criteria, described clearly and comprehensively.

Example response format:
- Description: The given pattern is a circle with four smaller circles inside it. The smaller circles are evenly spaced and touch the circumference of the larger circle.
- New Pattern: A square with four triangles inside, each triangle's base touching one side of the square, and the triangles pointing towards the center.

Ensure your descriptions are clear and accurate, and your new pattern is creative and adheres to the given criteria. Submit your response as a plain text string in the following format:
- Description: [Your description here]
- New Pattern: [Your new pattern here]

Make sure to follow the specified format exactly and provide a comprehensive description. The new pattern must include all required elements, be symmetrical if specified, and show creativity in arrangement."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture the given pattern's components and arrangement.",
            "The new pattern should be creative and adhere to the specified criteria.",
            "The response should follow the specified format precisely.",
            "The new pattern should include all the required elements mentioned in the criteria.",
            "The new pattern description should be clear and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
