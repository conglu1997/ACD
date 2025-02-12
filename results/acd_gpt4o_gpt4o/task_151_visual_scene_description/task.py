class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine you are standing in a bustling city square during a festival. Describe the scene in detail, including the people, activities, decorations, and overall atmosphere."},
            "2": {"prompt": "Picture a serene beach at sunset. Describe the scene in detail, including the colors of the sky, the waves, the sand, and any other elements you find important."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the following visual scene in detail based on the given prompt:
{t['prompt']}
Ensure your description is vivid, detailed, and captures the essence of the scene. Your response should be between 150 and 300 words. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid and detailed.", "The description should capture the essence of the scene described in the prompt.", "The response should be between 150 and 300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
