import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Japanese",
                "emotions": ["mono no aware", "wabi-sabi", "koi no yokan", "yugen", "amae"]
            },
            {
                "name": "Inuit",
                "emotions": ["iktsuarpok", "pittiarniq", "inuuqatigiittiarniq", "quviannikumut", "uqumangirniq"]
            },
            {
                "name": "Zulu",
                "emotions": ["ubuntu", "amandla", "indaba", "tokoloho", "eish"]
            },
            {
                "name": "Danish",
                "emotions": ["hygge", "janteloven", "arbejdsglæde", "overskud", "andægtig"]
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a synesthesia-like mapping between emotions and colors for the {t['name']} culture. Your task has the following components:

1. Emotion-Color Mapping (200-250 words):
   a) Create a mapping between the five given emotions and specific colors for the {t['name']} culture.
   b) Explain the rationale behind each emotion-color pairing, considering cultural context and symbolism.
   c) Describe how these mappings might differ from those in Western cultures.

Emotions: {', '.join(t['emotions'])}

2. Synesthesia Simulation (150-200 words):
   a) Propose a method to simulate this emotion-color synesthesia in an AI system.
   b) Explain how this simulation could be used to generate or interpret emotional content in text or images.

3. Cross-Cultural Analysis (200-250 words):
   a) Compare your emotion-color mappings for the {t['name']} culture with those of another culture of your choice.
   b) Discuss similarities and differences, explaining their potential cultural or cognitive origins.
   c) Propose a hypothesis about universal vs. culture-specific aspects of emotion-color associations.

4. Artistic Application (150-200 words):
   a) Describe an artwork that could be created using your emotion-color mappings.
   b) Explain how this artwork might be interpreted differently by viewers from the {t['name']} culture vs. other cultures.

5. Cognitive Implications (150-200 words):
   a) Discuss how these emotion-color associations might influence cognition and perception in the {t['name']} culture.
   b) Propose an experiment to test whether these associations affect memory or decision-making processes.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and cultural studies. Be creative in your mappings and analysis while maintaining cultural sensitivity and scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 850-1100 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent emotion-color mapping for the {t['name']} culture, with explanations for each pairing",
            "The proposed synesthesia simulation method for AI is plausible and well-explained",
            "The cross-cultural analysis demonstrates insight into cultural differences and similarities",
            "The artistic application is creative and culturally relevant",
            "The cognitive implications discussion shows understanding of how emotion-color associations might affect cognition",
            "The response demonstrates interdisciplinary knowledge synthesis across cognitive science, linguistics, and visual arts",
            "The answer is well-structured, using clear headings for each section, and adheres to the 850-1100 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
