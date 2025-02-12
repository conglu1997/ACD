import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Mandarin Chinese",
                "writing_system": "Chinese characters",
                "language_family": "Sino-Tibetan"
            },
            {
                "name": "Arabic",
                "writing_system": "Arabic script",
                "language_family": "Afroasiatic"
            },
            {
                "name": "Russian",
                "writing_system": "Cyrillic alphabet",
                "language_family": "Indo-European"
            },
            {
                "name": "Swahili",
                "writing_system": "Latin alphabet",
                "language_family": "Niger-Congo"
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating, interpreting, and explaining idiomatic expressions in {t['name']}, while also analyzing their cognitive and cultural foundations. Your response should include the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for idiomatic expression processing.
   b) Explain how these components interact to generate, interpret, and explain idioms.
   c) Discuss how your system incorporates cultural and cognitive knowledge.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Idiom Generation (200-250 words):
   a) Explain how your system would generate novel, culturally appropriate idiomatic expressions in {t['name']}.
   b) Describe the role of the {t['writing_system']} in idiom generation.
   c) Provide an example of a generated idiom, its literal translation, and its intended figurative meaning.

3. Idiom Interpretation (200-250 words):
   a) Detail how your system would interpret and explain the meaning of idiomatic expressions in {t['name']}.
   b) Discuss how your system handles ambiguity and context-dependent meanings.
   c) Explain how your system would translate idioms into non-idiomatic language while preserving meaning.

4. Cognitive and Cultural Analysis (200-250 words):
   a) Describe how your system analyzes the cognitive mechanisms underlying idiom comprehension and production.
   b) Explain how your system incorporates cultural knowledge specific to speakers of {t['name']}.
   c) Discuss how your system accounts for the historical and social factors that influence idiom formation and use.

5. Cross-linguistic Capabilities (150-200 words):
   a) Explain how your system could be adapted to work with other languages in the {t['language_family']} family.
   b) Discuss potential challenges in extending the system to languages from different language families.
   c) Propose a method for comparing idiomatic expressions across languages.

6. Evaluation and Ethical Considerations (150-200 words):
   a) Propose a method to evaluate your system's performance in generating and interpreting idioms.
   b) Discuss potential biases or ethical issues that could arise from your system's use or development.
   c) Suggest safeguards or guidelines to address these concerns.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and plausible system architecture for processing idiomatic expressions.",
            f"The idiom generation process is well-explained and considers the specific characteristics of {t['name']} and its writing system.",
            "The idiom interpretation process is clearly described and addresses challenges such as ambiguity and context-dependence.",
            "The cognitive and cultural analysis demonstrates a deep understanding of the factors influencing idiom formation and use.",
            f"The cross-linguistic capabilities section provides a thoughtful discussion of extending the system to other languages in the {t['language_family']} family and beyond.",
            "The evaluation method and ethical considerations are well-reasoned and comprehensive.",
            "The overall response displays creativity, scientific plausibility, and a strong interdisciplinary approach to the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
