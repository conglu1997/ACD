import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            ("Fibonacci sequence", "13"),
            ("Golden ratio", "1.618")
        ]
        cultural_aspects = [
            "Lunar calendar-based society",
            "Nomadic desert civilization"
        ]
        return {
            str(i+1): {
                'mathematical_concept': concept[0],
                'parameter': concept[1],
                'cultural_aspect': aspect
            } for i, (concept, aspect) in enumerate(zip(mathematical_concepts, cultural_aspects))
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to generate and analyze musical scales based on the mathematical concept of the {t['mathematical_concept']} (using {t['parameter']} as a key parameter), then use it to create and explore a hypothetical musical tradition for a fictional {t['cultural_aspect']}. Your response should include the following sections:

1. Mathematical Scale Generation (300-350 words):
   a) Explain how you use the {t['mathematical_concept']} to generate a unique musical scale, incorporating {t['parameter']} as a key parameter.
   b) Provide the mathematical formula or algorithm for your scale generation.
   c) Describe the properties of your generated scale (e.g., number of notes, intervals, frequency ratios).
   d) Compare your scale to traditional scales (e.g., pentatonic, heptatonic) in terms of mathematical properties.
   e) Include a visual representation (using ASCII characters) of your scale, showing the relative positions of notes.

2. Cultural Integration (250-300 words):
   a) Describe key characteristics of your fictional {t['cultural_aspect']}.
   b) Explain how your mathematical scale reflects or complements these cultural characteristics.
   c) Propose at least two unique musical instruments that would be well-suited to play your scale, describing their construction and playing technique.
   d) Describe a significant musical tradition or ceremony in this culture that showcases the use of your scale.
   e) Explain how the mathematical properties of your scale (especially the use of {t['parameter']}) influence the cultural practices you've described.

3. Music Theory Analysis (250-300 words):
   a) Analyze the harmonic possibilities of your scale, including consonant and dissonant intervals.
   b) Describe potential chord structures that could be derived from your scale.
   c) Explain how melodic patterns in your scale might differ from those in traditional Western music.
   d) Propose a notation system for your scale that reflects its mathematical basis and cultural context.

4. Composition Example (200-250 words):
   a) Describe a short musical piece composed using your scale.
   b) Explain how this piece reflects both the mathematical properties of the scale (including the use of {t['parameter']}) and the cultural context.
   c) Discuss any unique challenges or opportunities presented by composing in this scale.
   d) Provide a brief notation or representation of a key motif from your composition using your proposed notation system.

5. Cross-Cultural Comparison (200-250 words):
   a) Compare your fictional musical tradition to at least two real-world musical traditions.
   b) Analyze how the mathematical basis of your scale might influence the perception of this music by listeners from different cultural backgrounds.
   c) Propose an experiment to test the emotional or psychological effects of music composed in your scale compared to traditional scales.

6. Potential Applications (150-200 words):
   a) Suggest how this approach to scale generation could be applied in music education or music therapy.
   b) Discuss potential applications in algorithmic composition or AI-generated music.
   c) Explore how this system could be used to study or preserve endangered musical traditions.

Ensure your response demonstrates a deep understanding of music theory, mathematical concepts, and cultural anthropology. Be creative and innovative in your approach while maintaining scientific and cultural plausibility. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Include a word count at the end of each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['mathematical_concept']} and its application to musical scale generation, incorporating {t['parameter']} as a key parameter",
            f"The proposed musical tradition is creative, coherent, and plausibly integrated with the fictional {t['cultural_aspect']}, with a clear explanation of how the scale's mathematical properties influence cultural practices",
            "The music theory analysis shows a deep understanding of harmonic and melodic principles, with a well-thought-out notation system",
            "The composition example effectively illustrates the unique properties of the generated scale and reflects the cultural context",
            "The cross-cultural comparison demonstrates insight into real-world musical traditions and proposes a feasible experiment",
            "The response includes innovative yet plausible applications of the scale generation system",
            "The submission adheres to the specified word count for each section and includes a visual representation of the scale using ASCII characters",
            "The response demonstrates creativity and interdisciplinary knowledge integration throughout all sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
