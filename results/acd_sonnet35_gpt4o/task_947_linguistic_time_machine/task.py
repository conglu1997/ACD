import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ["English", "Spanish", "Mandarin", "Arabic"]
        time_periods = ["past", "future"]
        years = list(range(100, 501, 100))  # 100 to 500 years in steps of 100
        phrases = [
            "The quick brown fox jumps over the lazy dog",
            "I love to eat delicious food with my family",
            "Technology has greatly changed our daily lives",
            "Music brings joy and harmony to the world"
        ]
        
        return {
            "1": {
                "language": random.choice(languages),
                "time_direction": random.choice(time_periods),
                "years": random.choice(years),
                "phrase": random.choice(phrases)
            },
            "2": {
                "language": random.choice(languages),
                "time_direction": random.choice(time_periods),
                "years": random.choice(years),
                "phrase": random.choice(phrases)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that predicts phonological changes in {t['language']} over time. Your task is to analyze potential changes {t['years']} years in the {t['time_direction']} and apply them to the phrase: "{t['phrase']}". 

Your response should include the following sections:

1. System Design (200-250 words):
   • Describe the key components of your AI system for predicting phonological changes.
   • Explain how your system incorporates historical linguistic data and principles of sound change.
   • Outline the types of data your system would need for training.

2. Phonological Analysis (200-250 words):
   • Identify 3-5 potential phonological changes that might occur in {t['language']} over {t['years']} years.
   • Explain the linguistic principles or historical trends that inform these predictions.
   • Use IPA notation to illustrate these changes. (Note: IPA refers to the International Phonetic Alphabet)

3. Phrase Evolution (150-200 words):
   • Apply your predicted changes to the phrase: "{t['phrase']}"
   • Provide both the original and evolved versions in IPA notation.
   • Explain each change you applied and its potential impact on the language's sound system.

4. Implications and Limitations (150-200 words):
   • Discuss potential implications of accurate phonological prediction for linguistics or other fields.
   • Identify limitations of your approach and potential ethical considerations.
   • Suggest a method to validate your system's predictions.

Format your response with clear headings for each section. Use bullet points where appropriate. Your total response should be between 700-900 words.

Example of the kind of analysis expected (do not use this exact example in your response):
• Potential change: Final 'r' dropping in English
• IPA representation: /kɑr/ → /kɑ:/
• Explanation: This change is observed in some English dialects and might spread, leading to compensatory lengthening of the preceding vowel.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response focuses on phonological changes in {t['language']} over {t['years']} years in the {t['time_direction']}.",
            "The system design incorporates historical linguistic data and principles of sound change.",
            "The response includes 3-5 potential phonological changes with explanations and IPA notation.",
            f"The phrase \"{t['phrase']}\" is transformed according to the predicted changes, with IPA notation provided.",
            "Implications and limitations of the approach are discussed.",
            "The response demonstrates understanding of historical linguistics and language evolution.",
            "The proposed system is creative while maintaining linguistic plausibility.",
            "The response is formatted with clear headings and adheres to the specified word count range."
        ]
        scores = [float(eval_with_llm_judge(instructions, submission, [criterion])) for criterion in criteria]
        return sum(scores) / len(scores)
