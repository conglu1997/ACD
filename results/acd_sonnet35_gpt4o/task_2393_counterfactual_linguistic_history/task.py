class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language": "Latin",
                "historical_period": "Fall of the Western Roman Empire",
                "linguistic_change": "Latin retains its complex case system (the system of noun, pronoun, and adjective endings that indicate grammatical function)"
            },
            "2": {
                "language": "Old English",
                "historical_period": "Norman Conquest of England",
                "linguistic_change": "Old English resists Norman French influence"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Construct an alternative historical narrative based on a counterfactual change in the evolution of {t['language']} during the {t['historical_period']}. The linguistic change to consider is: {t['linguistic_change']}. Your response should include:

1. Alternative Historical Narrative (250-300 words):
   a) Describe how the specified linguistic change might have occurred.
   b) Explain the immediate consequences of this change on the language and its speakers.
   c) Outline the potential long-term effects on historical events, cultural developments, and geopolitical dynamics.
   d) Discuss how this change might have affected the global linguistic landscape up to the present day.

2. Linguistic Analysis (200-250 words):
   a) Describe the key features of the hypothetical modern version of the language resulting from this change.
   b) Compare and contrast these features with those of the actual modern descendants or relatives of the language.
   c) Explain how these features might have influenced the language's spread, usage, or cultural significance.
   Use appropriate linguistic terminology throughout your analysis.

3. Sample Text (100-150 words):
   a) Construct a short text (2-3 sentences, totaling 30-40 words) in this hypothetical modern language. The text should be about a significant historical event or cultural practice in your alternative timeline.
   b) Provide a translation of this text into modern English.
   c) Explain key linguistic features demonstrated in your constructed text.

4. Reflection (100-150 words):
   a) Discuss the plausibility of your alternative historical narrative and linguistic evolution.
   b) Identify any potential logical inconsistencies or challenges in your scenario.
   c) Suggest one way this exercise could contribute to our understanding of actual linguistic and historical processes.

Ensure your response demonstrates a deep understanding of linguistic evolution, historical causality, and creative language construction. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining logical consistency and plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The alternative historical narrative is logically consistent and plausible given the linguistic change.",
            "The linguistic analysis demonstrates a deep understanding of language evolution and features, using appropriate terminology.",
            "The constructed sample text accurately reflects the described linguistic features, is internally consistent, and meets the specified word count.",
            "The reflection shows critical thinking about the scenario's plausibility and implications.",
            "The response demonstrates creativity while maintaining historical and linguistic plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
