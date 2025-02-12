class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"author": "William Shakespeare", "prompt": "Describe a moonlit night in a forest."},
            "2": {"author": "Mark Twain", "prompt": "Write about a mischievous adventure of a young boy in a small town."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a passage imitating the writing style of {t['author']} based on the following prompt: {t['prompt']}\nEnsure that your passage is coherent, stylistically accurate, and between 150 to 300 words. Pay special attention to capturing the unique linguistic style and themes of {t['author']}."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The passage should accurately imitate the writing style of {t['author']}.", "The content should be coherent and relevant to the given prompt.", "The passage length should be between 150 and 300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
