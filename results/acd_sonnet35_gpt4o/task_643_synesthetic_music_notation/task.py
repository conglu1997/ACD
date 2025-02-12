import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            {
                "element": "rhythm",
                "synesthetic_modality": "texture"
            },
            {
                "element": "harmony",
                "synesthetic_modality": "color"
            },
            {
                "element": "melody",
                "synesthetic_modality": "shape"
            },
            {
                "element": "timbre",
                "synesthetic_modality": "taste"
            }
        ]
        return {
            "1": random.choice(musical_elements),
            "2": random.choice(musical_elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a synesthetic music notation system that represents the musical element of {t['element']} using the synesthetic modality of {t['synesthetic_modality']}. Your task has four parts:

1. Notation System Design (250-300 words):
   a) Describe how you will use {t['synesthetic_modality']} to represent different aspects of {t['element']} in music.
   b) Explain the key components and structure of your notation system.
   c) Provide examples of how your system would represent at least three different states or variations of {t['element']}.

2. Mathematical Foundation (200-250 words):
   a) Describe the mathematical principles or concepts underlying your notation system.
   b) Explain how these mathematical foundations relate to both the musical element and the synesthetic modality.
   c) Provide at least one formula or equation that is central to your system's functionality.

3. Cognitive and Emotional Analysis (200-250 words):
   a) Analyze how your notation system might affect the cognitive processing of music by musicians and listeners.
   b) Discuss the potential emotional impacts of experiencing music through this synesthetic representation.
   c) Explain how your system might influence creativity and musical composition.

4. Practical Application and Limitations (150-200 words):
   a) Describe a practical scenario where your notation system could be applied (e.g., music education, composition, therapy).
   b) Discuss any limitations or challenges in implementing and using your system.
   c) Suggest how your system could be expanded or combined with other synesthetic modalities for a more comprehensive music representation.

Ensure your response demonstrates a deep understanding of music theory, mathematics, cognitive science, and synesthesia. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The notation system effectively uses {t['synesthetic_modality']} to represent {t['element']} in music.",
            "The mathematical foundation is well-developed and logically connected to both the musical element and synesthetic modality.",
            "The cognitive and emotional analysis demonstrates a nuanced understanding of how this system might impact music perception and creation.",
            "The response shows creativity, interdisciplinary knowledge application, and critical thinking about the practical applications and limitations of the approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
