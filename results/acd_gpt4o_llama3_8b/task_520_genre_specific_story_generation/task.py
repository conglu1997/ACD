class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'genre': 'science fiction',
                'prompt': 'In a future where AI governs society, a human discovers a secret about their origins that could change everything.'
            },
            '2': {
                'genre': 'fantasy',
                'prompt': 'In a world where magic is forbidden, a young wizard discovers their powers and must decide whether to hide or fight for their freedom.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        genre = t['genre']
        prompt = t['prompt']
        return f'Write a short story based on the following genre and prompt:\n\nGenre: {genre}\nPrompt: {prompt}\n\nYour story should be between 300 to 500 words. Ensure that it adheres to the conventions of the specified genre and is engaging and coherent. Submit your story as a plain text string.'

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The story should adhere to the conventions of the specified genre.',
            'The story should be between 300 to 500 words.',
            'The story should be engaging and coherent.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
