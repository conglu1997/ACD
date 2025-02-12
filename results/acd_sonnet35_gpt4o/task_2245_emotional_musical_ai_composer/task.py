import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "Melancholy",
            "Euphoria",
            "Nostalgia",
            "Anticipation",
            "Contentment"
        ]
        
        cultures = [
            "West African",
            "Scandinavian",
            "Andean",
            "Japanese",
            "Middle Eastern"
        ]
        
        musical_elements = [
            "Rhythm",
            "Melody",
            "Harmony",
            "Timbre",
            "Dynamics"
        ]
        
        musical_scales = [
            "Pentatonic",
            "Chromatic",
            "Whole tone",
            "Octatonic",
            "Microtonal"
        ]
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "culture": random.choice(cultures),
                "musical_element": random.choice(musical_elements),
                "scale": random.choice(musical_scales)
            },
            "2": {
                "emotion": random.choice(emotions),
                "culture": random.choice(cultures),
                "musical_element": random.choice(musical_elements),
                "scale": random.choice(musical_scales)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music based on the emotion of {t['emotion']}, within the context of {t['culture']} culture, with a focus on the musical element of {t['musical_element']} and using the {t['scale']} scale. Your response should include the following sections:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI composer system.\n   b) Explain how your system processes emotional input and cultural context.\n   c) Detail how the system incorporates music theory, the specified musical element, and the given scale.\n   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.\n\n2. Emotional-Musical Translation (200-250 words):\n   a) Explain how your system translates {t['emotion']} into musical parameters.\n   b) Describe how the system incorporates {t['culture']} cultural elements in its composition.\n   c) Discuss how the focus on {t['musical_element']} and the use of the {t['scale']} scale influences the composition process.\n\n3. Sample Composition Analysis (200-250 words):\n   a) Provide a detailed description of a short musical piece your AI might compose based on the given parameters.\n   b) Analyze how this composition reflects the specified emotion, cultural context, musical element, and scale.\n   c) Discuss any challenges or unique solutions in this composition process.\n\n4. Learning and Adaptation (150-200 words):\n   a) Explain how your AI system could learn and improve its compositions over time.\n   b) Describe how it might adapt to feedback from human listeners or musicians.\n\n5. Cross-Cultural Applications (150-200 words):\n   a) Discuss how your system could be used to bridge cultural gaps through music.\n   b) Propose an experiment to test the system's effectiveness in cross-cultural communication.\n\n6. Ethical and Creative Implications (200-250 words):\n   a) Analyze the potential impact of AI-composed emotional music on human creativity and the music industry.\n   b) Discuss ethical considerations related to cultural appropriation and authenticity in AI-generated music.\n   c) Propose guidelines for responsible development and use of emotionally intelligent musical AI systems.\n\nEnsure your response demonstrates a deep understanding of music theory, emotional intelligence, cultural studies, and AI system design. Be creative in your approach while maintaining scientific and artistic plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1150-1450 words. Each section should adhere to the specified word count range.\n\nExample: For a system composing music based on 'Nostalgia' in 'Japanese' culture, focusing on 'Melody' using a 'Pentatonic' scale, you might consider how traditional Japanese instruments like the koto or shamisen could be incorporated, and how the pentatonic scale could evoke a sense of nostalgia within Japanese musical traditions."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of music theory, particularly in relation to the {t['musical_element']} and the {t['scale']} scale.",
            f"The proposed AI system architecture effectively integrates the emotion of {t['emotion']}, {t['culture']} cultural elements, and the specified musical parameters.",
            "The sample composition analysis shows a nuanced understanding of how emotion, culture, musical elements, and scale interact in the composition process.",
            "The discussion of learning and adaptation demonstrates an understanding of AI capabilities and limitations in musical composition.",
            "The cross-cultural applications and experiment proposal are innovative and well-reasoned.",
            "The ethical analysis comprehensively addresses issues related to AI in creative fields, cultural representation, and responsible development.",
            "The response adheres to the specified word count ranges for each section and the overall submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
