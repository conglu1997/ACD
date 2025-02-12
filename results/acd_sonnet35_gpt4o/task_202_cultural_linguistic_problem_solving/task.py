import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            "Convince a friend to join you on a spontaneous adventure",
            "Apologize for being late to an important meeting",
            "Explain the concept of recycling to a child",
            "Negotiate a better price for a product you want to buy",
            "Comfort a friend who has just experienced a loss"
        ]
        language_culture_pairs = [
            ("Japanese", "Japan"),
            ("Spanish", "Mexico"),
            ("Arabic", "Egypt"),
            ("French", "France"),
            ("Mandarin", "China"),
            ("German", "Germany"),
            ("Russian", "Russia"),
            ("Hindi", "India")
        ]
        return {
            "1": {
                "problem": random.choice(problems),
                "languages": random.sample(language_culture_pairs, 3)
            },
            "2": {
                "problem": random.choice(problems),
                "languages": random.sample(language_culture_pairs, 3)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate culturally and linguistically appropriate solutions to the following problem in three different languages and cultural contexts:\n\nProblem: {t['problem']}\n\nLanguages and Cultures:\n1. {t['languages'][0][0]} ({t['languages'][0][1]})\n2. {t['languages'][1][0]} ({t['languages'][1][1]})\n3. {t['languages'][2][0]} ({t['languages'][2][1]})\n\nFor each language and culture, provide the following:\n\n1. Solution (100-150 words):\n   Write a response in the specified language that addresses the problem. Your response should be culturally appropriate and incorporate at least one idiomatic expression or cultural reference specific to that language and culture.\n\n2. English Translation (100-150 words):\n   Provide an English translation of your solution, including explanations of any idiomatic expressions or cultural references used.\n\n3. Cultural Analysis (50-75 words):\n   Explain how your solution reflects the cultural norms, communication styles, and values of the specific culture. Highlight any unique aspects of your approach that are particularly relevant to that culture.\n\n4. Linguistic Features (50-75 words):\n   Describe at least two linguistic features (e.g., honorifics, gendered language, formal/informal distinctions) that you incorporated into your solution and explain their significance in the language.\n\nEnsure that your responses demonstrate a deep understanding of each language and culture, while effectively addressing the given problem. Be creative in your approach while maintaining cultural authenticity and linguistic accuracy."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solutions are provided in the correct languages and adhere to the word limits.",
            "Each solution effectively addresses the given problem while being culturally appropriate.",
            "The responses incorporate accurate and relevant idiomatic expressions or cultural references.",
            "The English translations accurately convey the meaning of the original solutions.",
            "The cultural analyses demonstrate a deep understanding of each culture's norms and values.",
            "The linguistic features are correctly identified and explained for each language.",
            "The overall response shows creativity, cultural sensitivity, and linguistic accuracy across all three languages and cultures."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
