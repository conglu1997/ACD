class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a joke involving a computer and a banana.",
                "context": "Joke creation"
            },
            "2": {
                "joke": "Why don't scientists trust atoms? Because they make up everything!",
                "context": "Joke comprehension"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"You are required to create a joke based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure that your joke is humorous and contextually appropriate. Submit your joke as a plain text string in the following format:\n\nJoke: [Your joke here]"
        else:
            return f"You are required to identify the punchline in the following joke:\n\nJoke: {t['joke']}\n\nSubmit your punchline as a plain text string in the following format:\n\nPunchline: [Your punchline here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            validation_criteria = [
                "The response should be a joke that is humorous and contextually appropriate."]
        else:
            validation_criteria = [
                "The response should correctly identify the punchline of the joke."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
