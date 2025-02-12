class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Why did the chicken cross the road?"
            },
            "2": {
                "prompt": "What do you get when you cross a snowman with a vampire?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a joke based on the following prompt and explain why it is funny:

Prompt: {t['prompt']}

Your response should include:
1. The joke.
2. A brief explanation of why the joke is humorous. Your explanation should include the type of humor used (e.g., wordplay, irony, absurdity) and how it creates a humorous effect.

Submit your response as a plain text string in the following format:

Joke: [Your joke]
Explanation: [Your explanation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The joke should be based on the given prompt.",
            "The joke should be coherent and resemble recognized forms of humor.",
            "The explanation should clearly detail why the joke is humorous, including the type of humor used and how it creates a humorous effect."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
