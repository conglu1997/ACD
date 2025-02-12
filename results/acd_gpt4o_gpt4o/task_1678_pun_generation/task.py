class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "fruits"},
            "2": {"prompt": "computers"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a pun based on the following prompt:

Prompt: {t['prompt']}

A pun is a form of wordplay that exploits multiple meanings of a term or similar-sounding words for humorous or rhetorical effect. Ensure that your pun is clear, clever, and relevant to the given prompt. Provide your response in plain text format.

Example:

Prompt: animals
Pun: Why don't elephants use computers? Because they're afraid of the mouse!

Another Example:

Prompt: music
Pun: Why did the musician get locked out of his house? Because he left his keys inside!"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The pun should demonstrate clear wordplay.",
            "The pun should be relevant to the given prompt.",
            "The pun should be humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0