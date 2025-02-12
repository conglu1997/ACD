class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'prompt': 'Create a humorous sentence using a pun based on the word "bark".'
            },
            '2': {
                'prompt': 'Create a humorous sentence using a pun based on the word "jam".'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous sentence based on the following prompt. Your sentence should use wordplay to create humor. Ensure that your sentence is original and contextually appropriate.

Prompt: {t['prompt']}

Ensure that your content is original and not copied from any sources."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The sentence should use wordplay to create humor.',
            'The content should be original and not copied from any sources.',
            'The sentence should be contextually appropriate.']
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
