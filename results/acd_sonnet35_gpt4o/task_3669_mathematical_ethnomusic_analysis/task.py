import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "Golden ratio",
            "Prime numbers",
            "Fractals",
            "Modular arithmetic",
            "Graph theory"
        ]
        musical_elements = [
            "Rhythm",
            "Melody",
            "Harmony",
            "Timbre",
            "Form",
            "Texture"
        ]
        cultural_traditions = [
            "West African polyrhythms",
            "Indian classical ragas",
            "Chinese pentatonic scales",
            "Western classical counterpoint",
            "Javanese gamelan music",
            "Middle Eastern maqam system"
        ]
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "cultural_tradition1": random.choice(cultural_traditions),
                "cultural_tradition2": random.choice(cultural_traditions)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "cultural_tradition1": random.choice(cultural_traditions),
                "cultural_tradition2": random.choice(cultural_traditions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on the mathematical concept of {t['math_concept']}, focusing primarily on the musical element of {t['musical_element']}. Then use this system to analyze and compare the musical traditions of {t['cultural_tradition1']} and {t['cultural_tradition2']}. Your response should include:

1. Mathematical Musical System Design (300-350 words):
   a) Explain how you incorporate {t['math_concept']} into your musical system.
   b) Describe how your system represents and manipulates {t['musical_element']}.
   c) Provide at least two specific examples of how your system generates or analyzes musical patterns.
   d) Discuss any novel insights or relationships between mathematics and music revealed by your system.
   e) Include at least one mathematical formula or equation that is central to your system.

2. Cultural Analysis: {t['cultural_tradition1']} (250-300 words):
   a) Briefly describe the key characteristics of {t['cultural_tradition1']}, including at least two specific musical examples.
   b) Apply your mathematical musical system to analyze this tradition, focusing on {t['musical_element']}.
   c) Discuss at least three insights or patterns revealed by your analysis.
   d) Explain how your system's mathematical basis enhances understanding of this tradition.

3. Cultural Analysis: {t['cultural_tradition2']} (250-300 words):
   a) Briefly describe the key characteristics of {t['cultural_tradition2']}, including at least two specific musical examples.
   b) Apply your mathematical musical system to analyze this tradition, focusing on {t['musical_element']}.
   c) Discuss at least three insights or patterns revealed by your analysis.
   d) Explain how your system's mathematical basis enhances understanding of this tradition.

4. Comparative Analysis (200-250 words):
   a) Compare and contrast {t['cultural_tradition1']} and {t['cultural_tradition2']} using your mathematical musical system.
   b) Identify at least two surprising similarities and two differences revealed by your analysis.
   c) Discuss how the mathematical basis of your system contributes to a deeper cross-cultural understanding.
   d) Provide a visual representation (described in words) of your comparative analysis.

5. Theoretical Implications (200-250 words):
   a) Discuss at least three broader implications of your mathematical musical system for music theory and ethnomusicology.
   b) Propose how your system could be used to analyze at least two other musical traditions or elements not previously mentioned.
   c) Suggest at least two potential applications of your system in music composition or education.

6. Limitations and Future Work (150-200 words):
   a) Acknowledge at least two limitations of your mathematical musical system.
   b) Propose specific ways to address these limitations or expand the system's capabilities.
   c) Suggest three future research directions that could build upon your work.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and cultural anthropology. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and cultural accuracy.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) for each point within a section. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['math_concept']} and its application to {t['musical_element']}.",
            "The mathematical musical system is well-designed, clearly explained, and includes at least one mathematical formula or equation.",
            f"The analyses of {t['cultural_tradition1']} and {t['cultural_tradition2']} are insightful, culturally sensitive, and include specific musical examples.",
            "The comparative analysis reveals at least two surprising similarities and two differences between the musical traditions.",
            "The response shows innovative thinking while maintaining scientific and cultural accuracy.",
            "The theoretical implications include at least three broader implications and two potential applications.",
            "The limitations and future work section acknowledges at least two limitations and suggests three future research directions.",
            "The response adheres to the specified format, including headings, subheadings, and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
