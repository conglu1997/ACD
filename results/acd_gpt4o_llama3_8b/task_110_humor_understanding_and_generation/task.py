class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "joke": "Why don't scientists trust atoms? Because they make up everything."
            },
            "2": {
                "prompt": "Create a joke involving a cat trying to use a computer." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'joke' in t:
            return f"""Interpret the following joke and explain why it is funny:

{t['joke']}

Your explanation should be clear, concise, and capture the humor in the joke. Submit your explanation as a plain text string."""
        elif 'prompt' in t:
            return f"""Generate a joke based on the following prompt:

{t['prompt']}

Ensure that the joke is original, humorous, and related to the prompt. Submit your joke as a plain text string."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'joke' in t:
            validation_criteria = ["The explanation should clearly capture the humor and relevance of the joke."]
        elif 'prompt' in t:
            validation_criteria = ["The joke should be original, humorous, and related to the given prompt."]
        else:
            validation_criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
