class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a detective solving a mysterious case in a haunted mansion."},
            "2": {"prompt": "Create a narrative about an astronaut discovering an alien civilization on a distant planet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a coherent and engaging narrative based on the following prompt: '{t['prompt']}'. Ensure that the narrative has a clear beginning, middle, and end, with logical progression and plot development. The story should be at least 500 words long and should be an original creation. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be coherent and logically consistent.",
            "The narrative should be engaging and maintain the reader's interest.",
            "The narrative should have a clear beginning, middle, and end.",
            "The narrative should be at least 500 words long.",
            "The narrative should be an original creation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
