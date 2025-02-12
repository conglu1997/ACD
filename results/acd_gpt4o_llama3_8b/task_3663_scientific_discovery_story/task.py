class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"discovery": "discovery of a new exoplanet with potential signs of life", "scientific_field": "astronomy"},
            "2": {"discovery": "development of a revolutionary new battery technology", "scientific_field": "materials science"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        discovery = t['discovery']
        scientific_field = t['scientific_field']
        return f"""You are tasked with writing a short story centered around a scientific discovery or phenomenon. The discovery you need to incorporate into your story is: {discovery} in the field of {scientific_field}. Your story should include the following elements:

1. A vivid description of the discovery or phenomenon.
2. The impact of the discovery on the scientific community or society.
3. The challenges or obstacles faced during the discovery process.
4. The personal experiences and emotions of the main characters involved in the discovery.

Ensure that your story is engaging, scientifically accurate, and well-structured. Submit your response as a plain text string in the following format:

Title: [Your story title here]

Story:
[Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be engaging and well-structured.",
            "The story should include a vivid description of the discovery or phenomenon.",
            "The story should accurately reflect the scientific discovery or phenomenon.",
            "The story should describe the impact on the scientific community or society.",
            "The story should include challenges or obstacles faced during the discovery process.",
            "The story should convey the personal experiences and emotions of the main characters."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
