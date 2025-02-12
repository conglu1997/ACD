class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Why did the ..."
            },
            "2": {
                "joke": "I told my wife she was drawing her eyebrows too high. She looked surprised."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Generate a joke based on the following prompt:

Prompt: {t['prompt']}

Ensure the joke is original, coherent, and humorous while following the structure implied by the prompt. Submit your joke as a plain text string."""
        else:
            return f"""Analyze the humor elements in the following joke:

Joke: {t['joke']}

Your analysis should include:
1. Identification of the type of joke (e.g., pun, wordplay, situational).
2. Explanation of why the joke is funny.
3. Any cultural or linguistic elements that contribute to the humor.

Submit your analysis as a plain text string in the following format:

Type of Joke: [Type]
Explanation: [Explanation]
Cultural/Linguistic Elements: [Elements]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            validation_criteria = [
                "The joke should be original and coherent.",
                "The joke should follow the structure implied by the prompt.",
                "The joke should be humorous."
            ]
        else:
            validation_criteria = [
                "The analysis should correctly identify the type of joke.",
                "The analysis should explain why the joke is funny.",
                "The analysis should mention any cultural or linguistic elements contributing to the humor."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
