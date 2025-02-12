class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "story_snippet": "Once upon a time, in a small village surrounded by mountains, there lived a young girl named Elara. She had always dreamed of exploring the world beyond the peaks, but...",
                "constraints": "The story must include a magical creature, a hidden treasure, and a moral lesson. The tone should be adventurous and whimsical."
            },
            "2": {
                "story_snippet": "In the heart of the city, there was an old library that many believed to be haunted. On a rainy evening, a curious boy named Leo decided to step inside, and...",
                "constraints": "The story must include a surprising twist, a historical figure, and a lesson on courage. The tone should be mysterious and engaging."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following story snippet by adhering to the given constraints. Ensure the story is coherent, follows the specified tone, and incorporates the required elements:

Story Snippet: {t['story_snippet']}

Constraints: {t['constraints']}

Submit your completed story as a plain text string.

Example:
Story Snippet: Once upon a time, there was a brave knight named Sir Galahad who embarked on a quest to find the lost Grail. Along the way, he encountered...
Constraints: The story must include a dragon, a riddle, and a moral about perseverance. The tone should be heroic and inspiring.

Completed Story: Once upon a time, there was a brave knight named Sir Galahad who embarked on a quest to find the lost Grail. Along the way, he encountered a fierce dragon guarding a bridge. The dragon posed a riddle that Sir Galahad had to solve to pass. After many attempts and unwavering determination, Sir Galahad solved the riddle and crossed the bridge, learning that perseverance was the key to overcoming any obstacle."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The story must be coherent.", "The story must follow the specified tone.", "The story must incorporate the required elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
