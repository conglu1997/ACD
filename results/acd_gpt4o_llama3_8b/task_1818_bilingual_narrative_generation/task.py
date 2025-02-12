class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a short story about a time traveler exploring different historical periods.", "languages": ["English", "Spanish"]},
            "2": {"prompt": "Create a narrative about a scientist discovering a new element that changes the world.", "languages": ["English", "French"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        languages = ' and '.join(t['languages'])
        return f"Generate a coherent and engaging narrative based on the following prompt: '{t['prompt']}'. Each paragraph should alternate between {languages}. Ensure that the narrative maintains logical progression and plot development across both languages. The story should be at least 500 words long and should be an original creation. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be coherent and logically consistent across both languages.",
            "The narrative should switch languages in each paragraph.",
            "The narrative should be engaging and maintain the reader's interest.",
            "The narrative should have a clear beginning, middle, and end.",
            "The narrative should be at least 500 words long.",
            "The narrative should be an original creation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
