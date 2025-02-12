class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Invent a fictional culture. Provide a detailed description of the following aspects: social structure, key traditions, and daily life. Ensure that your description is coherent and vivid, bringing the culture to life."
            },
            "2": {
                "prompt": "Imagine a fictional culture that lives on floating islands in the sky. Describe their social hierarchy, main festivals, and a typical day for an average citizen. Make your description as imaginative and detailed as possible."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Invent a fictional culture based on the prompt provided. Your description should cover the following aspects:
1. Social Structure: Describe the hierarchy and organization of the society.
2. Traditions: Highlight key traditions, festivals, and rituals that are significant in this culture.
3. Daily Life: Detail what a typical day looks like for an average citizen.

Ensure that your description is imaginative, coherent, and vivid. Bring the culture to life with rich details and thoughtful explanations.

Prompt: {t['prompt']}

Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be coherent and vivid.",
            "The social structure, traditions, and daily life should be well-explained.",
            "The response should demonstrate creativity and cultural understanding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
