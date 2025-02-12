import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "Fibonacci sequence",
            "fractal geometry",
            "prime numbers",
            "complex numbers",
            "topology",
            "chaos theory"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "form",
            "dynamics"
        ]
        cultures = [
            "West African",
            "Indian classical",
            "Chinese traditional",
            "Western classical",
            "Middle Eastern",
            "Polynesian"
        ]
        
        tasks = {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures)
            }
        }
        
        # Ensure cultures are different
        while tasks["2"]["culture1"] == tasks["2"]["culture2"]:
            tasks["2"]["culture2"] = random.choice(cultures)
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on the mathematical concept of {t['math_concept']}, focusing on the musical element of {t['musical_element']}. Then, apply this system to create a cross-cultural composition blending elements from {t['culture1']} and {t['culture2']} musical traditions. Your response should include:

1. Mathematical-Musical System Design (300-350 words):
   a) Explain how you incorporate {t['math_concept']} into your musical system.
   b) Describe how your system affects or generates {t['musical_element']}.
   c) Provide at least one mathematical formula or algorithm central to your system.
   d) Discuss how your system differs from traditional Western musical theory.
   e) Include a visual representation or diagram of your system (describe it textually).

2. Cross-Cultural Application (250-300 words):
   a) Briefly describe key characteristics of {t['culture1']} and {t['culture2']} musical traditions.
   b) Explain how you would apply your mathematical-musical system to create a composition blending these traditions.
   c) Discuss any challenges in reconciling your system with these cultural traditions and how you address them.

3. Sample Composition (200-250 words):
   a) Provide a detailed description of a short composition using your system and incorporating elements from both cultures.
   b) Explain how specific elements of your piece reflect your mathematical-musical system and the cultural traditions.

4. Notation and Performance (150-200 words):
   a) Describe how your musical system would be notated.
   b) Explain any new instruments or modifications to existing instruments needed to perform compositions in your system.
   c) Discuss how your system might be implemented using existing music software or technology.

5. Analysis and Implications (200-250 words):
   a) Analyze the potential impact of your system on music theory and composition.
   b) Discuss how your system might influence cross-cultural musical understanding and collaboration.
   c) Explore potential applications of your system outside of music (e.g., in mathematics, physics, or other arts).

6. Ethical and Cultural Considerations (150-200 words):
   a) Discuss any ethical implications of creating a mathematical musical system and applying it to diverse cultural traditions.
   b) Address concerns about cultural appropriation or the loss of traditional musical elements.
   c) Propose guidelines for responsible development and use of such cross-cultural, mathematically-based musical systems.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and the specified cultural traditions. Be creative in your approach while maintaining mathematical rigor and cultural sensitivity. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed musical system based on {t['math_concept']} that affects {t['musical_element']}, including a visual representation or diagram.",
            f"The cross-cultural application demonstrates understanding of both {t['culture1']} and {t['culture2']} musical traditions.",
            "The sample composition effectively incorporates the mathematical-musical system and cultural elements.",
            "The response addresses notation, performance, and potential implications of the new musical system, including implementation using existing music software or technology.",
            "Ethical and cultural considerations are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
