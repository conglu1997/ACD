class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "prompt": "Generate a funny joke about artificial intelligence."},
            "2": {"task_type": "transformation", "original_joke": "Why don't scientists trust atoms? Because they make up everything!", "target_style": "pun"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            return f"Generate a funny joke based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure that your joke is humorous and relevant to the given prompt. Submit your joke as a plain text string in the following format:\nJoke: [Your joke here]"
        elif t["task_type"] == "transformation":
            return f"Transform the following joke into the specified style while retaining its humor and core meaning:\n\nOriginal Joke: {t['original_joke']}\n\nTarget Style: {t['target_style']}\n\nFor example, if the original joke is a simple setup-punchline and the target style is a pun, ensure the transformed joke uses wordplay typical of puns.\n\nSubmit your transformed joke as a plain text string in the following format:\nTransformed Joke: [Your transformed joke here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generation":
            criteria = ["The joke should be funny.", "The joke should be relevant to artificial intelligence."]
        else:
            criteria = ["The transformed joke should retain the humor and core meaning of the original joke.", "The transformed joke should fit the target style."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
