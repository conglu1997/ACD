import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_forms = [
            {
                "medium": "visual art",
                "culture": "Indigenous Australian",
                "theme": "connection to land"
            },
            {
                "medium": "music",
                "culture": "West African",
                "theme": "oral history"
            },
            {
                "medium": "poetry",
                "culture": "Japanese",
                "theme": "transience of life"
            },
            {
                "medium": "dance",
                "culture": "Indian classical",
                "theme": "spiritual devotion"
            }
        ]
        return {
            "1": random.choice(art_forms),
            "2": random.choice(art_forms)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating culturally informed artistic expressions, then use it to explore the philosophical implications of AI-generated art in society. Focus on the art form of {t['medium']} within the context of {t['culture']} culture, addressing the theme of {t['theme']}. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the key components and processes of your AI system for creating culturally informed art.
   b) Explain how your system integrates cultural knowledge, artistic techniques, and thematic understanding.
   c) Discuss any novel approaches or algorithms specific to generating {t['medium']} in the style of {t['culture']} culture.
   d) Address how your system ensures cultural sensitivity and authenticity in its creations.

2. Artistic Creation Process (250-300 words):
   a) Outline the step-by-step process your AI uses to create a {t['medium']} piece in the {t['culture']} style, addressing the theme of {t['theme']}.
   b) Explain how the system balances creativity with cultural authenticity.
   c) Describe how your AI incorporates feedback or iterates on its creations.

3. Sample Artwork Description (200-250 words):
   a) Provide a detailed description of a sample {t['medium']} piece your AI system would create.
   b) Explain how this piece reflects {t['culture']} cultural elements and addresses the theme of {t['theme']}.
   c) Discuss the artistic choices made by the AI and their cultural significance.

4. Evaluation and Interpretation (200-250 words):
   a) Propose methods to evaluate the cultural authenticity and artistic merit of the AI-generated {t['medium']}.
   b) Describe how you would validate the system's output against human-created art in the same cultural context.
   c) Discuss potential reactions from {t['culture']} artists and cultural experts to this AI-generated art.

5. Philosophical Implications (250-300 words):
   a) Explore the philosophical questions raised by AI systems creating culturally informed art.
   b) Discuss the implications for concepts of creativity, authorship, and cultural ownership.
   c) Address the ethical considerations of AI systems engaging with and potentially influencing cultural expressions.

6. Societal Impact and Future Directions (200-250 words):
   a) Analyze the potential impact of AI-generated cultural art on society, education, and cross-cultural understanding.
   b) Propose guidelines for the responsible development and use of AI in cultural art creation.
   c) Suggest future research directions or extensions of your system to other cultural contexts or art forms.

Ensure your response demonstrates a deep understanding of AI, art history, cultural studies, and philosophy. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining cultural sensitivity and ethical considerations.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and creative design for an AI system capable of generating {t['medium']} in the style of {t['culture']} culture, addressing the theme of {t['theme']}.",
            "The artistic creation process is well-explained and demonstrates a balance between AI creativity and cultural authenticity.",
            f"The sample artwork description vividly illustrates a piece that reflects {t['culture']} cultural elements and effectively addresses the theme of {t['theme']}.",
            "The evaluation methods proposed are thorough and consider both cultural authenticity and artistic merit.",
            "The philosophical implications are thoughtfully explored, addressing key questions about creativity, authorship, and cultural ownership in the context of AI-generated art.",
            "The analysis of societal impact and future directions demonstrates a nuanced understanding of the potential effects of AI in cultural art creation.",
            "The overall response shows a deep understanding of AI, art history, cultural studies, and philosophy, with appropriate use of terminology and clear explanations throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
