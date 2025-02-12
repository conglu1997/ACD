import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = ['Fibonacci sequence', 'Golden ratio', 'Prime numbers', 'Fractals']
        musical_elements = ['Melody', 'Harmony', 'Rhythm', 'Timbre']
        cultural_traditions = ['Western classical', 'Indian classical', 'West African', 'Chinese traditional']
        
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "cultural_tradition": random.choice(cultural_traditions)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements),
                "cultural_tradition": random.choice(cultural_traditions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates musical compositions based on mathematical principles and cultural elements, then analyze its output. Your task is to create a composition system that incorporates the mathematical concept of {t['math_concept']}, focuses on the musical element of {t['musical_element']}, and draws inspiration from the {t['cultural_tradition']} musical tradition. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your music generation system.
   b) Explain how you incorporate the {t['math_concept']} into your system's design.
   c) Detail how your system integrates {t['cultural_tradition']} musical knowledge.
   d) Discuss how your system focuses on generating or manipulating the {t['musical_element']}.
   e) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Mathematical-Musical Mapping (250-300 words):
   a) Explain how your system maps {t['math_concept']} to musical parameters.
   b) Describe how {t['cultural_tradition']} influences this mapping.
   c) Discuss any novel algorithms you've developed for this integration.
   d) Provide an example of how a simple musical phrase might be generated using your system.

3. Cultural Integration (200-250 words):
   a) Describe how your system incorporates key features of {t['cultural_tradition']} music.
   b) Explain how these cultural elements interact with the mathematical principles in your system.
   c) Discuss any challenges in representing diverse cultural elements within a mathematical framework.
   d) Explain how your system handles potential conflicts between mathematical principles and cultural authenticity.

4. Composition Process (250-300 words):
   a) Outline the step-by-step process your system uses to generate a composition.
   b) Explain how mathematical operations are used in this composition process.
   c) Provide a short example of a generated composition (at least 16 measures), using standard music notation or a clear alternative representation.
   d) Discuss how your system ensures musical coherence and cultural authenticity.

5. Analysis of Output (200-250 words):
   a) Analyze the musical qualities of your system's output, focusing on the {t['musical_element']}.
   b) Discuss how the {t['math_concept']} is evident in the generated composition.
   c) Evaluate how well the output reflects {t['cultural_tradition']} musical characteristics.
   d) Suggest potential improvements or extensions to your system.

6. Implications and Applications (200-250 words):
   a) Discuss the implications of your system for understanding the relationship between mathematics and music.
   b) Explore potential applications in music education, composition, or music therapy.
   c) Address any ethical considerations in using AI for cultural music generation.
   d) Propose an experiment to test the effectiveness or cultural authenticity of your system's output.
   e) Suggest a novel application of your system beyond music composition, in a different field or domain.

Ensure your response demonstrates a deep understanding of music theory, mathematical principles, and the specified cultural tradition. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining musical and cultural authenticity.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['math_concept']} and how it can be applied to music composition.",
            f"The system architecture effectively integrates {t['math_concept']} with {t['cultural_tradition']} musical elements, focusing on {t['musical_element']}.",
            "The mathematical-musical mapping is innovative and logically consistent.",
            f"The approach to incorporating {t['cultural_tradition']} musical tradition is well-explained and culturally sensitive.",
            "The composition process is clearly outlined and includes a specific example of generated music of at least 16 measures.",
            "The analysis of the system's output is thorough and addresses mathematical, musical, and cultural aspects.",
            "The implications and applications are thoughtfully discussed, including ethical considerations and a novel application beyond music composition.",
            "The response addresses potential conflicts between mathematical principles and cultural authenticity.",
            "The response is well-structured, coherent, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
