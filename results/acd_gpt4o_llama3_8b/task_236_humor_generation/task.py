class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a short, funny story about a day in the life of a talking cat."
            },
            "2": {
                "prompt": "Generate a humorous dialogue between two robots arguing about which one is more human-like."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous piece of content based on the given prompt:

Prompt:
{t['prompt']}

Ensure that the content is funny, creative, and appropriate. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The content should be humorous.",
            "The content should be creative.",
            "The content should be appropriate and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
