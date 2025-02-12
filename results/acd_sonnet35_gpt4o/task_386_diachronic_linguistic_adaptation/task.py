import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        periods = [
            {"name": "Old English", "year": "1000", "feature": "case system"},
            {"name": "Middle English", "year": "1400", "feature": "loss of grammatical gender"},
            {"name": "Early Modern English", "year": "1600", "feature": "Great Vowel Shift"},
            {"name": "Late Modern English", "year": "1800", "feature": "regularization of spelling"}
        ]
        modern_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question.",
            "It was the best of times, it was the worst of times.",
            "All animals are equal, but some animals are more equal than others."
        ]
        return {
            "1": {"period": random.choice(periods), "text": random.choice(modern_texts)},
            "2": {"period": random.choice(periods), "text": random.choice(modern_texts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the evolution of English language features, focusing on the {t['period']['name']} period (around {t['period']['year']}), and adapt the following modern text to reflect these changes:

"{t['text']}"

Your response should include:

1. Historical Context (100-150 words):
   Briefly describe the historical and cultural context of the {t['period']['name']} period, focusing on factors that influenced language evolution.

2. Linguistic Analysis (200-250 words):
   Analyze key linguistic features of English during this period, with a particular focus on the {t['period']['feature']}. Explain how these features differ from modern English.

3. Text Adaptation (100-150 words):
   Rewrite the given modern text to reflect the linguistic features of the {t['period']['name']} period. Explain your choices in adapting specific words, phrases, or structures.

4. Phonetic Representation (50-100 words):
   Provide a phonetic transcription of a key phrase from your adapted text, using IPA symbols. Explain how the pronunciation differs from modern English.

5. Semantic Shift (100-150 words):
   Identify a word in the text that has undergone semantic shift between the historical period and modern times. Explain its historical meaning and how it has changed.

6. Challenges and Limitations (100-150 words):
   Discuss the challenges in accurately representing historical language forms and any limitations in our knowledge of {t['period']['name']} English.

Ensure your response demonstrates a deep understanding of historical linguistics, phonology, and the specific features of {t['period']['name']}. Use appropriate linguistic terminology throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the linguistic features of {t['period']['name']} English.",
            f"The historical context provided is accurate and relevant to the {t['period']['name']} period.",
            f"The linguistic analysis accurately describes the {t['period']['feature']} and other key features of the period.",
            "The adapted text reflects appropriate linguistic features of the historical period.",
            "The phonetic transcription uses IPA symbols correctly and explains pronunciation differences.",
            "The semantic shift example is accurate and well-explained.",
            "The response addresses challenges and limitations in representing historical language forms.",
            "Appropriate linguistic terminology is used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
