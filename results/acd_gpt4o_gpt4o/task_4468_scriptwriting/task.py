class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre": "comedy", "prompt": "A misunderstanding at a coffee shop."},
            "2": {"genre": "science fiction", "prompt": "First contact with an alien species."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a script for a short scene based on the given genre and prompt.

Genre: {t['genre']}
Prompt: {t['prompt']}

The script should include dialogue, character actions, and scene descriptions. Ensure that the script is consistent with the conventions of the specified genre and that the story is engaging and coherent."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The script should include dialogue, character actions, and scene descriptions.",
            "The script should be consistent with the conventions of the specified genre.",
            "The story should be engaging and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
