class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'prompt': 'Write a short story that conveys a sense of nostalgia. The story should be between 200 and 400 words long.'
            },
            '2': {
                'prompt': 'Write a short scene that conveys a sense of suspense. The scene should be between 200 and 400 words long.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a short story or scene based on the following prompt. Ensure that your writing clearly conveys the specified emotional tone. The length of your submission should be between 200 and 400 words. Submit your response as a plain text string.

Prompt: {t['prompt']}

Ensure that your content is original and not copied from any sources."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The submission should be between 200 and 400 words long.',
            'The writing should clearly convey the specified emotional tone.',
            'The content should be original and not copied from any sources.']
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
