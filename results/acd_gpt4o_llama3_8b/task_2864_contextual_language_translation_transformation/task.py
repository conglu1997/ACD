class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "Once upon a time, in a land far away, there lived a wise old owl who knew the secrets of the forest. This owl, with its vast knowledge, helped the animals by guiding them through the challenges they faced. One day, the owl encountered a young rabbit who was lost and scared, and with patience and wisdom, the owl led the rabbit back to safety.",
                "source_language": "English",
                "target_language": "Spanish",
                "context": "Translate the text to Spanish and rewrite it in the style of a fairy tale aimed at children."
            },
            "2": {
                "text": "In the bustling city of Tokyo, technology and tradition coexist in a unique harmony that captivates visitors from around the world. The neon lights of Shibuya contrast beautifully with the serene temples that stand as a testament to Japan's rich history. As the seasons change, cherry blossoms bloom, painting the city in a delicate pink hue, a sight that has inspired countless poets and artists.",
                "source_language": "English",
                "target_language": "Japanese",
                "context": "Translate the text to Japanese and rewrite it as a poetic description."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given text, source language, target language, and context:

Text: {t["text"]}
Source Language: {t["source_language"]}
Target Language: {t["target_language"]}
Context: {t["context"]}

Tasks:
1. Translate the text to the target language specified.
2. Rewrite the translated text according to the given context (e.g., style, audience).

Submit your response as a plain text string with sections for 'Translation' and 'Transformed Text'.

Example format:
Translation: [Your translation here]
Transformed Text: [Your transformed text here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and faithful to the original text.",
            "The transformed text should match the given context and style requirements.",
            "The transformed text should be coherent and well-written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
