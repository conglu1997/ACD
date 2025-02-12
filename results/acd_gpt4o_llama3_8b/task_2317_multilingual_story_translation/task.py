class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "story": "Once upon a time in a small village in Spain, there lived a young girl named Maria. She loved to explore the forests and meadows surrounding her village. One day, while wandering through the woods, she found a magical flower that granted her wishes. Maria was overjoyed and used the flower to help her family and friends. The village prospered, and Maria became known as the girl with the magical flower.",
                "source_language": "English",
                "target_language": "Spanish"
            },
            "2": {
                "story": "Il était une fois dans un petit village en France, un jeune garçon nommé Pierre. Il aimait explorer les forêts et les prairies entourant son village. Un jour, en se promenant dans les bois, il trouva une fleur magique qui exauçait ses souhaits. Pierre était ravi et utilisa la fleur pour aider sa famille et ses amis. Le village prospéra et Pierre devint connu sous le nom de l'enfant à la fleur magique.",
                "source_language": "French",
                "target_language": "English"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following story from {t['source_language']} to {t['target_language']} while maintaining the original story's tone, style, and coherence:

Story:
{t['story']}

Ensure that the translation is accurate, preserves the narrative structure, and retains the original tone and style of the story. Submit your translated story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The translation should be accurate.", "The translated story should maintain the original tone, style, and coherence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
