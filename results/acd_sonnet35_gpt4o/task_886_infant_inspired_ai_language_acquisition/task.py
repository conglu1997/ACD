import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            {
                "feature": "Phonology",
                "description": "The sound system of the language"
            },
            {
                "feature": "Morphology",
                "description": "The structure and formation of words"
            },
            {
                "feature": "Syntax",
                "description": "The rules for forming grammatical sentences"
            },
            {
                "feature": "Semantics",
                "description": "The meaning of words and sentences"
            }
        ]
        return {
            "1": random.choice(language_features),
            "2": random.choice(language_features)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language acquisition system inspired by infant language learning processes, then apply it to teach an AI a constructed language. Focus on the language feature of {t['feature']}, defined as {t['description']}. Your task has the following parts:

1. Infant Language Acquisition Model (250-300 words):
   a) Describe key processes in infant language acquisition related to {t['feature']}.
   b) Explain how these processes could be adapted for an AI system.
   c) Propose a novel AI architecture or algorithm inspired by these infant learning processes.

2. Constructed Language Design (200-250 words):
   a) Create a simple constructed language with unique {t['feature']} properties.
   b) Provide examples demonstrating these properties.
   c) Explain how your language's {t['feature']} differs from natural languages.

3. AI Learning Implementation (250-300 words):
   a) Detail how your AI system would learn the {t['feature']} of your constructed language.
   b) Describe the stages of learning, from initial exposure to mastery.
   c) Explain how your system would handle errors or inconsistencies in input.
   d) Propose a method to evaluate the AI's proficiency in the language's {t['feature']}.

4. Comparative Analysis (200-250 words):
   a) Compare your AI language acquisition system to traditional machine learning approaches for language tasks.
   b) Discuss potential advantages and limitations of your infant-inspired approach.
   c) Hypothesize how this approach might perform with natural languages.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss ethical considerations in developing AI systems that learn like human infants.
   b) Propose practical applications of your system beyond language acquisition.
   c) Speculate on how this approach might influence future AI development.

Ensure your response demonstrates a deep understanding of language acquisition theories, cognitive development, and AI learning algorithms. Be creative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of infant language acquisition processes, particularly in relation to the given language feature.",
            "The AI language acquisition system design is innovative, detailed, and plausibly inspired by infant learning processes.",
            "The constructed language design is creative and clearly demonstrates the specified language feature.",
            "The AI learning implementation is well-explained and logically adapts infant learning processes to an AI system.",
            "The comparative analysis shows insightful understanding of both traditional machine learning and the proposed infant-inspired approach.",
            "Ethical and practical implications are thoughtfully addressed, demonstrating an understanding of the broader impact of this research.",
            "The response shows strong interdisciplinary reasoning, combining insights from linguistics, cognitive science, and artificial intelligence.",
            "The writing is clear, well-structured, and adheres to the specified format and word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
