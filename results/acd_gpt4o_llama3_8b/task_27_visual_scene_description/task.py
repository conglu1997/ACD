class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene": "Imagine a bustling city street at sunset. There are tall buildings on either side of the street, cars honking, people walking, and street vendors selling various items. Describe this scene in detail, focusing on the atmosphere, the sounds, and the people you see."
            },
            "2": {
                "scene": "Imagine a quiet forest clearing on a sunny day. There are trees surrounding the clearing, a small stream running through it, and various animals such as deer and birds. Describe this scene in detail, focusing on the sights, sounds, and the feeling of the place."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed description of the following visual scene:

{t['scene']}

Ensure your description captures the atmosphere, sounds, and significant details of the scene. The response should be at least 150 words long and submitted as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The description should be at least 150 words long.", "The description should capture the atmosphere, sounds, and significant details of the scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
