class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene": "A swirling vortex of colors with a hint of metallic sheen, floating above a reflective surface that distorts the colors further."
            },
            "2": {
                "scene": "A vast, empty desert under a sky filled with shimmering, abstract shapes that seem to move and change as you look at them."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scene = t["scene"]
        instructions = f"""Your task is to describe the following abstract visual scene in detailed and imaginative language.

Scene: {scene}

Your description should include:
1. A vivid portrayal of the visual elements.
2. Imaginative and creative language that captures the essence of the scene.
3. A coherent and engaging narrative that ties the visual elements together.

Provide your description in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include a vivid portrayal of the visual elements.",
            "The description should use imaginative and creative language.",
            "The description should be coherent and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
