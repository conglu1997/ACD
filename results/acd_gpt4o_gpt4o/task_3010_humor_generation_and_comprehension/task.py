class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a funny one-liner joke about programming."
            },
            "2": {
                "joke": "Why don't scientists trust atoms? Because they make up everything!"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return (
                f"Your task is to generate a humorous one-liner joke based on the following prompt:\n"
                f"Prompt: {t['prompt']}\n"
                "Provide your joke in plain text format. Ensure it is relevant to the prompt and clearly humorous."
            )
        elif 'joke' in t:
            return (
                f"Your task is to interpret the following joke and explain why it is funny:\n"
                f"Joke: {t['joke']}\n"
                "Provide your explanation in plain text format, clearly explaining the humor and any wordplay or context involved."
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'prompt' in t:
            criteria.append("The joke should be relevant to the prompt.")
            criteria.append("The joke should be humorous.")
        elif 'joke' in t:
            criteria.append("The explanation should clearly identify the humorous elements of the joke.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
