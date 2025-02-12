class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A serene lake surrounded by tall pine trees, with a small wooden cabin on the left side and a snow-capped mountain in the background. The sky is clear with a few fluffy clouds and the sun is setting, casting an orange glow over the scene.",
            },
            "2": {
                "description": "A bustling city street at night, with tall skyscrapers on both sides. Neon signs and billboards illuminate the street, where people are walking and cars are driving. There is a street vendor selling hot dogs on the corner, and a musician playing the guitar near the vendor."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed description of an image based on the following textual description:

Description:
{t['description']}

Ensure your description captures all the key elements and provides a clear, vivid visualization of the scene. Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should include all key elements mentioned in the original description.",
            "The description should be vivid and provide a clear visualization of the scene.",
            "The narrative should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
