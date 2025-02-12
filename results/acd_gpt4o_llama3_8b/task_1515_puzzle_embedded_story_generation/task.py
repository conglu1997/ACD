class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a detective who is solving a series of riddles left by a mysterious figure. Ensure the story is engaging and the riddles are logically solvable within the narrative context. The story should be between 500 to 700 words."},
            "2": {"prompt": "Write a short story about a group of adventurers who must solve ancient puzzles to find a hidden treasure. Ensure the story is engaging and the puzzles are logically solvable within the narrative context. The story should be between 500 to 700 words."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a short story based on the following prompt: '{t['prompt']}'. Ensure that the story is engaging, the puzzles are logically solvable within the narrative context, and the overall length is between 500 to 700 words. Submit your story as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be engaging and coherent.", "The embedded puzzles should be logically solvable within the narrative context.", "The overall length should be between 500 to 700 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
