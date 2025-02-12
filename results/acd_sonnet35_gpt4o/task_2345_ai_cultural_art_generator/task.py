import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_traditions = [
            {
                "culture": "Japanese",
                "art_form": "Ukiyo-e",
                "key_elements": ["woodblock printing", "everyday life scenes", "landscapes", "vibrant colors"],
                "historical_period": "Edo period (1603-1867)"
            },
            {
                "culture": "Aboriginal Australian",
                "art_form": "Dot painting",
                "key_elements": ["symbols", "storytelling", "natural ochre colors", "dreamtime narratives"],
                "historical_period": "Ancient to contemporary"
            },
            {
                "culture": "Renaissance Italian",
                "art_form": "Fresco painting",
                "key_elements": ["religious themes", "perspective", "human anatomy", "architectural settings"],
                "historical_period": "14th to 16th century"
            },
            {
                "culture": "West African",
                "art_form": "Kente cloth weaving",
                "key_elements": ["geometric patterns", "symbolic colors", "silk and cotton strips", "royal and ceremonial use"],
                "historical_period": "12th century to present"
            }
        ]
        return {
            "1": random.choice(cultural_traditions),
            "2": random.choice(cultural_traditions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates original artwork inspired by the {t['culture']} tradition of {t['art_form']}. Your system should preserve the essence of this art form while creating new, innovative pieces. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI art generation system.
   b) Explain how your system incorporates knowledge of {t['art_form']} and its key elements: {', '.join(t['key_elements'])}.
   c) Detail any novel machine learning techniques or algorithms your system employs.
   d) Discuss how your system ensures cultural authenticity while allowing for creativity.

2. Data Collection and Preprocessing (200-250 words):
   a) Identify the types of data your system would require to learn about {t['art_form']}.
   b) Explain how you would preprocess and augment this data for training.
   c) Discuss ethical considerations in data collection, especially regarding cultural artifacts.

3. Artistic Style Transfer and Innovation (200-250 words):
   a) Describe how your AI system captures and transfers the style of {t['art_form']}.
   b) Explain how it generates novel elements while maintaining cultural authenticity.
   c) Discuss any techniques used to ensure diversity in the generated artworks.

4. Cultural Sensitivity and Preservation (150-200 words):
   a) Explain how your system respects and preserves the cultural significance of {t['art_form']}.
   b) Discuss potential risks of cultural appropriation and how your system mitigates them.
   c) Describe how you would involve {t['culture']} artists or cultural experts in the development process.

5. Evaluation and Feedback (150-200 words):
   a) Propose methods to evaluate the quality and cultural authenticity of the generated art.
   b) Describe how you would incorporate feedback from {t['culture']} artists and cultural experts.
   c) Discuss how your system could adapt and improve based on this feedback.

6. Practical Applications and Implications (150-200 words):
   a) Suggest potential applications for your AI art generation system.
   b) Discuss how it might impact the preservation and evolution of {t['art_form']}.
   c) Consider potential positive and negative consequences for {t['culture']} artists and their community.

Ensure your response demonstrates a deep understanding of both AI technologies and the cultural significance of {t['art_form']}. Be creative in your approach while maintaining cultural sensitivity and addressing real-world constraints. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both AI technologies and the cultural significance of {t['art_form']}.",
            "The proposed AI system architecture is innovative and well-explained.",
            "The approach to data collection and preprocessing is thorough and ethically considerate.",
            f"The system's method for artistic style transfer and innovation respects the tradition of {t['art_form']} while allowing for creativity.",
            "Cultural sensitivity and preservation are thoughtfully addressed throughout the response.",
            "The evaluation methods and feedback incorporation process are well-designed and culturally appropriate.",
            "Practical applications and implications are insightfully discussed, considering both positive and negative potential impacts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
