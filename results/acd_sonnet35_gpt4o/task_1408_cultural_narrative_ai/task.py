import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "culture": "Inuit",
                "theme": "relationship with nature",
                "narrative_element": "oral storytelling traditions"
            },
            {
                "culture": "Yoruba",
                "theme": "ancestral wisdom",
                "narrative_element": "proverbs and folktales"
            },
            {
                "culture": "Maori",
                "theme": "origin myths",
                "narrative_element": "genealogical narratives"
            },
            {
                "culture": "Andean",
                "theme": "cosmic balance",
                "narrative_element": "cyclical time concepts"
            }
        ]
        return {
            "1": random.choice(cultures),
            "2": random.choice(cultures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes culturally-specific narratives, focusing on the {t['culture']} culture, the theme of {t['theme']}, and incorporating {t['narrative_element']}. Then, use your system to create a sample narrative and analyze its cultural significance. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the key components of your AI system for generating and analyzing culturally-specific narratives.
   b) Explain how your system incorporates cultural knowledge, linguistic patterns, and narrative structures.
   c) Detail how the system ensures cultural authenticity and sensitivity in its narrative generation.
   d) Discuss any ethical considerations in developing an AI system that works with cultural narratives.

2. Cultural-Linguistic Framework (250-300 words):
   a) Explain how your system represents and processes cultural concepts and linguistic features specific to the {t['culture']} culture.
   b) Describe how the system incorporates the theme of {t['theme']} into its narrative generation.
   c) Detail how {t['narrative_element']} are integrated into the AI's narrative structure and analysis.

3. Sample Narrative Generation (200-250 words):
   Using your designed system, generate a short narrative (100-150 words) that reflects the {t['culture']} culture, incorporates the theme of {t['theme']}, and uses {t['narrative_element']}. Ensure that your narrative is culturally sensitive and accurate.

4. Narrative Analysis (250-300 words):
   a) Analyze the generated narrative, explaining its cultural significance and how it reflects {t['culture']} values and worldviews.
   b) Discuss how the narrative incorporates the theme of {t['theme']} and utilizes {t['narrative_element']}.
   c) Identify any potential cultural misrepresentations or sensitivities in the generated narrative.

5. Cross-Cultural Comparison (200-250 words):
   a) Compare how your system would approach narrative generation for a different culture (choose one from the task options).
   b) Discuss the challenges in adapting the system to multiple cultures and how these could be addressed.
   c) Explore the potential of such a system for promoting cross-cultural understanding.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical implications of using AI to generate culturally-specific narratives.
   b) Explore potential benefits and risks of this technology for cultural preservation and education.
   c) Propose guidelines for the responsible development and use of culture-generating AI systems.

Ensure your response demonstrates a deep understanding of cultural anthropology, linguistics, narrative theory, and AI technologies. Be innovative in your approach while maintaining cultural respect and scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Remember to be culturally sensitive and accurate throughout your response, especially when generating and analyzing narratives.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and ethically-considered design for an AI system that effectively generates and analyzes narratives specific to the {t['culture']} culture, incorporating the theme of {t['theme']} and {t['narrative_element']}.",
            f"The cultural-linguistic framework demonstrates a deep understanding of the {t['culture']} culture and how to represent its concepts and linguistic features in an AI system.",
            f"A sample narrative is generated that authentically reflects the {t['culture']} culture, incorporates the theme of {t['theme']}, and uses {t['narrative_element']}. The narrative is creative, unique, and culturally sensitive.",
            "The narrative analysis shows insight into the cultural significance of the generated story and identifies any potential misrepresentations or sensitivities.",
            "The cross-cultural comparison thoughtfully explores the challenges and potential of adapting the system to multiple cultures.",
            "The discussion of ethical and societal implications demonstrates a nuanced understanding of the potential benefits and risks of using AI for cultural narrative generation.",
            "The overall response shows a strong grasp of cultural anthropology, linguistics, narrative theory, and AI, with appropriate use of technical terminology and clear explanations of complex concepts.",
            "The response adheres to the specified word count guidelines for each section and the overall submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
