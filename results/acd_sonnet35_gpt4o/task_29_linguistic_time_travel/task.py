import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "concept": "social media influencer",
                "year": 1750,
                "language": "English"
            },
            "2": {
                "concept": "electric car",
                "year": 1890,
                "language": "English"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the modern concept '{t['concept']}' into {t['language']} as it might have been expressed in the year {t['year']}. Your response should include:

1. A translation of the concept into language appropriate for the specified time period (1-2 sentences).
2. An explanation of key linguistic choices in your translation, including any archaic terms or phrases used (2-3 sentences).
3. A brief description of the historical context that informs your translation, including any related concepts or technologies that existed at the time (2-3 sentences).

Ensure your response is historically accurate and linguistically appropriate for the time period."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a translation of '{t['concept']}' in {t['language']} appropriate for the year {t['year']}.",
            "The response should explain the linguistic choices made in the translation.",
            "The response should provide relevant historical context for the translation.",
            "The translation and explanation should be historically accurate and linguistically appropriate for the specified time period."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
