class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"visual_stimulus": "A serene landscape with rolling hills, a small cottage by a river, and a rising sun."},
            "2": {"visual_stimulus": "A bustling cityscape at night, with towering skyscrapers, bright lights, and a busy street filled with people and vehicles."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative description and interpretation of the following visual stimulus:

Visual Stimulus: {t["visual_stimulus"]}

Your response should include:
1. A vivid and detailed description of the scene.
2. An interpretation of the emotions or themes conveyed by the scene.

Submit your response as a plain text string in the following format:

Description: [Your detailed description]
Interpretation: [Your interpretation of the emotions or themes]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a vivid and detailed description of the scene.",
            "The response should include an interpretation of the emotions or themes conveyed by the scene."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
