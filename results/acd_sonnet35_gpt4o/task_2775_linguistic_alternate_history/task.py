import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "language": "Latin",
                "historical_period": "Fall of the Western Roman Empire",
                "linguistic_change": "Latin retains its case system"
            },
            "2": {
                "language": "Old English",
                "historical_period": "Norman Conquest of England",
                "linguistic_change": "Old English does not adopt Norman French loanwords"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate and analyze an alternate historical timeline based on a hypothetical change in language evolution. Your task focuses on {t['language']} during the {t['historical_period']}, with the linguistic change: {t['linguistic_change']}. Your response should include:

1. Linguistic Analysis (200-250 words):
   a) Explain the actual historical linguistic change that occurred during this period.
   b) Describe the hypothetical linguistic change and its immediate effects on the language.
   c) Analyze how this change might have affected the language's subsequent evolution.

2. Alternate Timeline (250-300 words):
   a) Create a plausible alternate historical timeline stemming from this linguistic change.
   b) Describe at least three major historical events or developments that might have occurred differently.
   c) Explain how these changes logically follow from the initial linguistic alteration.

3. Societal and Cultural Impact (200-250 words):
   a) Discuss the potential effects of this alternate timeline on society and culture.
   b) Analyze how literature, art, or philosophy might have developed differently.
   c) Consider any implications for social structures, education, or power dynamics.

4. Linguistic Butterfly Effect (150-200 words):
   a) Propose how this change might have affected other languages or language families.
   b) Discuss any potential global linguistic consequences of your alternate timeline.

5. Comparative Analysis (150-200 words):
   a) Compare and contrast your alternate timeline with actual historical events.
   b) Discuss what this comparison reveals about the role of language in shaping history.

6. Reflection and Extrapolation (100-150 words):
   a) Reflect on the plausibility and limitations of your alternate history.
   b) Suggest how this exercise might inform our understanding of linguistic and historical processes.

Ensure your response demonstrates a deep understanding of historical linguistics, cultural evolution, and causal reasoning in history. Be creative in your alternate timeline while maintaining logical consistency and plausibility. Use appropriate terminology from linguistics and historical studies.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of historical linguistics and cultural evolution.",
            "The alternate timeline is creative yet logically consistent and plausible.",
            "The analysis shows clear causal reasoning linking the linguistic change to historical developments.",
            "The response considers a wide range of potential impacts across various domains (e.g., society, culture, literature).",
            "The comparative analysis provides insightful reflections on the role of language in shaping history."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
