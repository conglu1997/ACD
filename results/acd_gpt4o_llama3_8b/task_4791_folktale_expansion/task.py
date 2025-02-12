class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "folktale": "The Tortoise and the Hare",
                "culture": "Western"
            },
            "2": {
                "folktale": "The Monkey and the Crocodile",
                "culture": "Indian"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Expand the following traditional folktale into a short narrative, ensuring it retains the cultural relevance and coherence of the original story. Your expanded story should be engaging and provide additional details while staying true to the original themes and characters.

Folktale: {t['folktale']}
Culture: {t['culture']}

Your response should be a coherent and culturally relevant short story, no longer than 500 words. Submit your story as a plain text string in the following format:

Expanded Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The expanded story should retain the cultural relevance of the original folktale.",
            "The story should be coherent and engaging.",
            "The expanded story should stay true to the original themes and characters.",
            "The response should be no longer than 500 words.",
            "The response should follow the specified format: 'Expanded Story: [Your story here]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
