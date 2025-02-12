class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork": "Mona Lisa by Leonardo da Vinci", "task": "describe"},
            "2": {"artwork": "Starry Night by Vincent van Gogh", "task": "story"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'describe':
            return f"""Your task is to describe the following artwork in detail:

Artwork: {t['artwork']}

Ensure your description captures the visual elements, emotions, and any notable features of the artwork. Provide your description in plain text format."

Desired format:
Description: [Your detailed description]"""
        elif t['task'] == 'story':
            return f"""Your task is to create a story inspired by the following artwork:

Artwork: {t['artwork']}

Ensure your story is imaginative, coherent, and captures the essence of the artwork. Provide your story in plain text format."

Desired format:
Story: [Your imaginative story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'describe':
            criteria = [
                "The description should be detailed and coherent.",
                "The description should capture the visual elements and emotions of the artwork.",
                "The description should highlight any notable features of the artwork."
            ]
        elif t['task'] == 'story':
            criteria = [
                "The story should be imaginative and coherent.",
                "The story should capture the essence of the artwork."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
