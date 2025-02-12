class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a funny short story about a day in the life of a dog who thinks it's a cat."},
            "2": {"text": "Why don't scientists trust atoms? Because they make up everything!", "context": "This is an example of a pun."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            return f"Your task is to generate a humorous short story based on the following prompt:\n\n{t['prompt']}\n\nMake sure your story is funny and engaging."
        elif "text" in t:
            return f"Your task is to determine if the following text contains a joke and explain why it is or isn't funny:\n\n{t['text']}\n\nContext: {t['context']}\n\nProvide your response in the following format:\n\nIs it a joke: [Yes/No]\nExplanation: [Your detailed explanation]"
        else:
            raise ValueError("Invalid task format.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = ["The story should be funny.", "The story should be engaging."]
        elif "text" in t:
            criteria = ["The response should correctly identify if the text is a joke.", "The explanation should clearly justify why the text is or isn't funny."]
        else:
            raise ValueError("Invalid task format.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
