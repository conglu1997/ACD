class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {'source_language': 'English', 'target_language': 'Japanese', 'text': 'The early bird catches the worm.'},
            '2': {'source_language': 'Spanish', 'target_language': 'English', 'text': 'A caballo regalado no se le mira el diente.'}
        }
        assert len(tasks) == 2, 'There should be exactly two tasks.'
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following text from {t['source_language']} to {t['target_language']} and explain any cultural nuances or contexts that may differ between the two languages.

Text: {t['text']}

Your response should be structured as follows:
1. Translation: [Translated text]
2. Cultural Context: [Explanation of cultural nuances and contexts]
Ensure your translation is accurate and your explanation is clear and informative. Avoid direct translation if it does not convey the correct cultural meaning.
Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The translation should be accurate.',
            'The cultural context explanation should be clear and informative.',
            'The response should demonstrate understanding of both languages and their cultural contexts.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
