class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Use the idiom 'break the ice' in a sentence that describes a social scenario." 
            },
            "2": {
                "prompt": "Create a metaphor comparing a busy city to a beehive." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a sentence using the following prompt: {t['prompt']}. Ensure that the sentence uses the idiom, metaphor, or simile correctly and is contextually appropriate. The sentence should be creative and meaningful in the given context. Submit your sentence as a plain text string.

Example:
Prompt: Use the idiom 'kick the bucket' in a sentence describing a person's passing.
Sentence: 'After a long and fulfilling life, Grandpa finally kicked the bucket last autumn, leaving behind a legacy of love and laughter.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The sentence should correctly use the idiom, metaphor, or simile.", "The sentence should be contextually appropriate and meaningful.", "The sentence should demonstrate creativity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
