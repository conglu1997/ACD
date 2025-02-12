class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A canvas filled with swirling shades of blue and green, with sharp red lines cutting through the center.",
                "title": "Conflict in Tranquility"
            },
            "2": {
                "description": "An explosion of yellow and orange brushstrokes, with small, dark spots scattered throughout.",
                "title": "Joy Amidst Chaos"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        title = t["title"]
        instructions = f"""Your task is to interpret the following description of an abstract piece of art and explain its potential meaning or emotional impact.

Title: {title}
Description: {description}

Your response should include:
1. A detailed interpretation of the potential meaning or message conveyed by the artwork.
2. An analysis of the emotional impact the artwork might have on a viewer.
3. A thorough explanation of how the elements in the description (e.g., colors, shapes) contribute to your interpretation.

Provide your response in plain text format, ensuring that it is comprehensive and insightful.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a coherent and plausible interpretation of the artwork's meaning or message.",
            "The response should describe the potential emotional impact of the artwork.",
            "The response should include a thorough explanation of how the elements in the description contribute to the interpretation.",
            "The response should be comprehensive and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
