class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A bustling city street at night during a light rain."},
            "2": {"prompt": "A quiet forest clearing at dawn with morning dew on the leaves."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed visual description of the following scene:

{t['prompt']}

Ensure that your description is vivid, coherent, and contextually appropriate. Include details about the environment, lighting, sounds, textures, and any other relevant elements. Your description should be at least 150 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid and detailed.", "The description should be coherent and contextually appropriate.", "The description should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
