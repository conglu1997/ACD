import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "Desert planet with two suns and frequent sandstorms",
                "culture": "Nomadic tribes with a complex system of resource sharing",
                "text": "We must work together to survive the harsh conditions of our world.",
                "twist": "Incorporate a linguistic feature that reflects the concept of time dilation due to the two suns."
            },
            {
                "environment": "Underwater civilization in a bioluminescent coral reef",
                "culture": "Highly spiritual society with a caste system based on bioluminescence",
                "text": "The Great Glow guides us through the depths of our existence.",
                "twist": "Include a grammatical structure that changes based on the speaker's depth in the ocean."
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a constructed language (conlang) for a civilization with the following parameters:\n\nEnvironment: {t['environment']}\nCulture: {t['culture']}\nLinguistic twist: {t['twist']}\n\nComplete the following tasks:\n\n1. Conlang Structure (150-200 words):\n   a) Phonology: Describe 5-7 unique sounds and any phonological rules\n   b) Morphology: Explain how words are formed, including any affixes or mutations\n   c) Syntax: Outline the basic sentence structure and word order\n   d) Unique Feature: Describe one feature that reflects the environment or culture\n\n2. Lexicon (75-100 words):\n   Provide 8-10 essential words or phrases in your conlang, including:\n   - Word in conlang\n   - IPA pronunciation\n   - English translation\n   - Brief explanation of cultural or environmental significance\n\n3. Translation (75-100 words):\n   Translate the following text into your conlang:\n   \"{t['text']}\"\n   - Provide the translation\n   - Include IPA pronunciation\n   - Explain any cultural or environmental nuances in the translation\n\n4. Linguistic Analysis (100-150 words):\n   a) Explain how your conlang reflects the given environment and culture\n   b) Describe how you incorporated the linguistic twist\n   c) Discuss one potential challenge in using this language\n\nPresent your response in clearly labeled sections corresponding to the four tasks above. Be creative and consistent in your language design while ensuring it reflects the given parameters."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang's structure includes phonology, morphology, syntax, and a unique feature reflecting the environment or culture.",
            "The lexicon contains 8-10 words with IPA pronunciation, English translation, and cultural/environmental significance.",
            "The translation of the given text is provided in the conlang with IPA pronunciation and explanation of nuances.",
            f"The conlang incorporates elements of the specified environment: {t['environment']}",
            f"The conlang reflects aspects of the given culture: {t['culture']}",
            f"The linguistic twist is addressed: {t['twist']}",
            "The response demonstrates creativity and interdisciplinary knowledge application.",
            "The response follows the specified format with clearly labeled sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
