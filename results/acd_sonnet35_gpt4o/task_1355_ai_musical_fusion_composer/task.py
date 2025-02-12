import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            "Classical Western",
            "Jazz",
            "Traditional Chinese",
            "Indian Classical",
            "West African",
            "Electronic Dance Music"
        ]
        musical_elements = [
            "rhythm",
            "melody",
            "harmony",
            "instrumentation",
            "structure"
        ]
        
        def get_distinct_traditions():
            t1 = random.choice(musical_traditions)
            t2 = random.choice([t for t in musical_traditions if t != t1])
            return t1, t2
        
        return {
            "1": {
                "tradition1": get_distinct_traditions()[0],
                "tradition2": get_distinct_traditions()[1],
                "focus_element": random.choice(musical_elements)
            },
            "2": {
                "tradition1": get_distinct_traditions()[0],
                "tradition2": get_distinct_traditions()[1],
                "focus_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of composing music that fuses {t['tradition1']} and {t['tradition2']} musical traditions, with a particular focus on {t['focus_element']}. Your response should include:\n\n1. AI System Design (300-350 words):\n   a) Describe the key components of your AI system for musical fusion composition.\n   b) Explain how your system would analyze and represent the musical elements of both traditions.\n   c) Detail how the system would generate new musical ideas that fuse these traditions.\n   d) Discuss any novel AI techniques or algorithms used in your system.\n   e) Address potential challenges in creating coherent musical fusions and how your system overcomes them.\n\n2. Musical Analysis (250-300 words):\n   a) Provide a brief overview of the key characteristics of both {t['tradition1']} and {t['tradition2']} musical traditions.\n   b) Analyze how {t['focus_element']} is typically handled in each tradition.\n   c) Explain how your AI system would approach fusing these different approaches to {t['focus_element']}.\n   d) Discuss potential areas of compatibility and conflict between the two traditions.\n\n3. Composition Process (300-350 words):\n   a) Describe a step-by-step process of how your AI system would compose a fusion piece.\n   b) Explain how the system would ensure a balance between the two traditions.\n   c) Provide a detailed example of how your system would handle a specific musical challenge, such as:\n      - Combining a rhythmic pattern from one tradition with a melodic structure from another\n      - Fusing harmonic systems from different traditions\n      - Integrating traditional instruments from both cultures\n   d) Discuss how your system would evaluate and refine its compositions.\n   e) Include a brief musical notation or textual description of a specific fusion element your system might create (e.g., a melodic phrase, rhythm pattern, or harmonic progression).\n\n4. Output Analysis (200-250 words):\n   a) Describe the expected characteristics of a composition produced by your AI system.\n   b) Analyze how this composition would reflect elements of both musical traditions.\n   c) Discuss potential strengths and weaknesses of the AI-generated fusion compared to human-composed fusion music.\n   d) Explain how you would evaluate the musical quality and cultural authenticity of the AI's compositions.\n\n5. Ethical and Cultural Considerations (150-200 words):\n   a) Discuss potential ethical implications of using AI for cross-cultural musical fusion.\n   b) Address concerns about cultural appropriation or misrepresentation.\n   c) Propose guidelines for responsible use of AI in creating cultural fusion music.\n\n6. Future Implications (150-200 words):\n   a) Speculate on how AI-driven musical fusion might impact global music trends and cross-cultural understanding.\n   b) Discuss potential applications of your system beyond music composition (e.g., music education, cultural preservation).\n   c) Suggest areas for future research or improvement in AI-driven musical composition and fusion.\n\nEnsure your response demonstrates a deep understanding of musical theory, cultural aspects of music, and AI capabilities. Use appropriate terminology from music theory and AI fields, providing clear explanations where necessary. Be creative in your approach while maintaining musical and technological plausibility.\n\nFormat your response with clear headings for each main section (numbered 1-6) and use lettered subheadings (a, b, c, etc.) within each section as outlined above. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of musical theory, cultural aspects of music, and AI capabilities.",
            "The proposed AI system is innovative, coherent, and technically plausible.",
            "The musical analysis shows sensitivity and nuanced understanding of both musical traditions involved.",
            "The composition process is well-detailed and addresses the fusion of the two traditions effectively.",
            "A specific fusion element is described or notated as requested.",
            "The output analysis critically evaluates the potential strengths and weaknesses of AI-generated fusion music.",
            "Ethical and cultural considerations are thoughtfully addressed.",
            "The response is well-structured, using the required headings and subheadings.",
            "All required sections are thoroughly addressed.",
            "The response is creative while maintaining musical and technological plausibility.",
            "The total word count is between 1350-1650 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
