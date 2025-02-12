class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": "Analyze the following musical notation and describe the key, time signature, and any notable patterns or elements. Then, create a short musical composition (4 bars) in the same key and time signature. Ensure your response includes the analysis and the musical composition in plain text format.", "musical_notation": "C D E F | G A B C"},
            "2": {"instructions": "Write lyrics for a song based on the following theme: overcoming adversity. Ensure the lyrics fit a common song structure (e.g., verse-chorus-verse) and are emotionally resonant. Provide your lyrics in plain text format.", "theme": "overcoming adversity"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instructions']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'musical_notation' in t:
            criteria = ["The analysis should accurately describe the key, time signature, and notable patterns or elements.", "The composition should be in the same key and time signature.", "The musical composition should be 4 bars long."]
        elif 'theme' in t:
            criteria = ["The lyrics should fit the theme of overcoming adversity.", "The lyrics should fit a common song structure (e.g., verse-chorus-verse).", "The lyrics should be emotionally resonant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
