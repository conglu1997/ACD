class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prose_passage": "The sun set over the horizon, painting the sky with hues of orange and pink. Birds chirped their final songs of the day, and a gentle breeze rustled the leaves. The world seemed to hold its breath, savoring the last moments of daylight before night embraced the earth."
            },
            "2": {
                "prose_passage": "In the heart of the bustling city, a small garden flourished. Amidst the concrete and steel, vibrant flowers bloomed, offering a splash of color and a breath of fresh air. People paused in their hurried steps to admire the beauty, finding a moment of peace in the urban jungle."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following prose passage into a poem:

Prose Passage: {t['prose_passage']}

Ensure that the poem captures the essence of the original passage, uses poetic language, and follows a consistent rhythm or meter. The poem should be at least four lines long but no longer than ten lines. Avoid directly copying phrases from the prose; instead, creatively transform the ideas into poetic form. Use poetic devices such as imagery, metaphor, and rhyme where appropriate. Submit your poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem should capture the essence of the original prose.",
            "The poem should use poetic language and imagery.",
            "The poem should follow a consistent rhythm or meter.",
            "The poem should be at least four lines long but no longer than ten lines.",
            "The poem should avoid directly copying phrases from the prose.",
            "The poem should use poetic devices such as imagery, metaphor, and rhyme where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
