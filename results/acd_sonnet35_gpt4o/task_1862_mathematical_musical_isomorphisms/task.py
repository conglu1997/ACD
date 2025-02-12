import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            {
                "concept": "Fourier Transform",
                "description": "A mathematical transform that decomposes functions depending on space or time into functions depending on spatial or temporal frequency"
            },
            {
                "concept": "Fibonacci Sequence",
                "description": "A sequence of numbers in which each number is the sum of the two preceding ones"
            }
        ]
        return {
            "1": random.choice(math_concepts),
            "2": random.choice(math_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that creates a bidirectional mapping between the mathematical concept of {t['concept']} and musical compositions. Then, use this system to explore cognitive processing of abstract structures. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your system for creating mathematical-musical isomorphisms.
   b) Explain how your system represents and processes information from both mathematical and musical domains.
   c) Detail the mechanisms used for mapping concepts between mathematics and music.
   d) Discuss how your system ensures the generated mappings are both mathematically valid and musically meaningful.

2. Isomorphism Creation (250-300 words):
   a) Create a detailed mapping between {t['concept']} and a musical structure or composition.
   b) Explain how key properties of {t['concept']} are represented in the musical domain.
   c) Describe how musical elements (e.g., pitch, rhythm, harmony) are used to encode mathematical information.
   d) Provide a specific example of how a mathematical operation or property would be expressed musically.

3. Reverse Mapping (200-250 words):
   a) Explain how your system would interpret a given musical piece to extract mathematical information.
   b) Describe the process of translating musical elements back into mathematical concepts.
   c) Discuss any challenges or ambiguities in this reverse mapping process and how your system addresses them.

4. Cognitive Science Application (250-300 words):
   a) Propose an experiment using your system to investigate how the human brain processes abstract structures across mathematical and musical domains.
   b) Describe the experimental design, including variables, methodology, and expected outcomes.
   c) Explain how this experiment could provide insights into cognitive flexibility, cross-domain thinking, or abstract reasoning.

5. Implications and Extensions (200-250 words):
   a) Discuss the potential implications of your system for mathematics education or music composition.
   b) Explore how this approach might contribute to our understanding of the relationship between mathematics and music.
   c) Propose an extension of your system to include a third domain (e.g., visual art, language) and briefly describe how this could work.

Ensure your response demonstrates a deep understanding of both mathematics and music theory. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering scientific and artistic validity throughout your response.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the mathematical concept and music theory.",
            "The proposed system creates a clear and logical bidirectional mapping between mathematics and music.",
            "The isomorphism creation and reverse mapping processes are well-explained and plausible.",
            "The cognitive science application is innovative and well-designed to investigate abstract structure processing.",
            "The response explores implications and extensions of the system in a thoughtful and creative manner.",
            "The overall response shows strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
