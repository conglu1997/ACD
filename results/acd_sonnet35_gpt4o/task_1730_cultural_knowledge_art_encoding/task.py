import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures_and_elements = [
            ("Ancient Egyptian", "Concept of Ma'at (cosmic order and balance)"),
            ("Inuit", "Importance of Sedna (goddess of the sea)"),
            ("Maori", "Concept of Mana (spiritual power and prestige)"),
            ("Aztec", "Belief in Tonalli (animating spirit)"),
            ("Yoruba", "Concept of Ashe (life force)"),
            ("Tibetan", "Principle of Karma (cause and effect)")
        ]
        art_styles = [
            "Geometric Abstraction",
            "Color Field Painting",
            "Suprematism",
            "Abstract Expressionism",
            "Constructivism",
            "Minimalism"
        ]
        task1 = random.choice(cultures_and_elements)
        task2 = random.choice(cultures_and_elements)
        while task2 == task1:
            task2 = random.choice(cultures_and_elements)
        return {
            "1": {"culture": task1[0], "cultural_element": task1[1], "art_style": random.choice(art_styles)},
            "2": {"culture": task2[0], "cultural_element": task2[1], "art_style": random.choice(art_styles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for encoding and decoding cultural knowledge from {t['culture']} culture, specifically focusing on the {t['cultural_element']}, using abstract art in the style of {t['art_style']}. Then, analyze its potential applications and implications for AI and cultural preservation. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your encoding and decoding system.
   b) Explain how your system translates the {t['cultural_element']} into abstract art elements (e.g., shapes, colors, compositions).
   c) Detail the process of decoding the abstract art back into cultural knowledge.
   d) Discuss how your system ensures accuracy and consistency in encoding and decoding.
   e) Provide a simple diagram or flowchart of your system's architecture (describe it textually).

2. Cultural and Artistic Analysis (250-300 words):
   a) Analyze the challenges in representing the {t['cultural_element']} through {t['art_style']}.
   b) Explain how your system captures and preserves the nuances and complexities of this cultural element.
   c) Provide two specific examples of how aspects of the {t['cultural_element']} would be encoded in your system.

3. AI and Cognitive Science Implications (200-250 words):
   a) Discuss how your system contributes to our understanding of the relationship between visual representation, cultural knowledge, and cognition.
   b) Explain the implications of your system for developing AI that can understand and generate culturally meaningful abstract art.
   c) Propose a hypothesis about how this approach might inform theories of human cultural learning and transmission.

4. Applications and Impact (200-250 words):
   a) Explore potential applications of your system in fields such as cultural preservation, education, or cross-cultural communication.
   b) Analyze how your system might enhance or transform traditional approaches to documenting and sharing cultural knowledge.
   c) Discuss the potential impact of your system on global cultural understanding and appreciation.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues or concerns raised by your proposed system.
   b) Discuss how these ethical considerations might be addressed or mitigated.
   c) Propose guidelines for the responsible development and use of AI systems that encode cultural knowledge in art.

6. Evaluation and Future Work (150-200 words):
   a) Describe how you would evaluate the effectiveness and accuracy of your system.
   b) Discuss potential limitations of your approach.
   c) Suggest areas for future research or improvement in encoding cultural knowledge through abstract art.

Ensure your response demonstrates a deep understanding of the specified culture, the chosen art style, and relevant AI and cognitive science principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response using clear headings for each section, numbered exactly as above (1. System Design, 2. Cultural and Artistic Analysis, etc.). Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-defined system design for encoding and decoding the {t['cultural_element']} from {t['culture']} culture using abstract art in the style of {t['art_style']}.",
            f"The cultural and artistic analysis should provide clear examples and explanations of how specific aspects of the {t['cultural_element']} would be encoded.",
            "The response should discuss implications for AI and cognitive science, including potential contributions to understanding visual representation, cultural knowledge, and cognition.",
            "Applications and impact of the system should be explored, including its potential effect on cultural preservation and global understanding.",
            "Ethical considerations and guidelines for responsible development must be addressed.",
            "The response should include a plan for evaluation and suggestions for future work.",
            "The overall response should demonstrate creativity, interdisciplinary knowledge integration, and a deep understanding of the specified culture and art style.",
            "The response must be formatted with clear headings for each section, numbered exactly as specified in the instructions.",
            "The response should be between 1250-1550 words in total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
