import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            {
                'concept': 'Riemann hypothesis',
                'musical_element': 'harmonic series',
                'cognitive_function': 'working memory',
                'brain_region': 'prefrontal cortex'
            },
            {
                'concept': 'P vs NP problem',
                'musical_element': 'polyrhythms',
                'cognitive_function': 'pattern recognition',
                'brain_region': 'parietal lobe'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(mathematical_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that explains how the complex mathematical concept of the {t['concept']} could be encoded in musical compositions using {t['musical_element']} to enhance {t['cognitive_function']} in the {t['brain_region']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the key components of your model, integrating neuroscience, music theory, and mathematics.
   b) Describe how the mathematical concept is translated into musical elements.
   c) Explain the proposed mechanism by which this musical encoding enhances the specified cognitive function.
   d) Provide a diagram or mathematical representation of your model.

2. Musical Composition (250-300 words):
   a) Describe a short musical piece (or section) that demonstrates your model.
   b) Explain how specific musical elements encode mathematical information.
   c) Discuss how this composition might be perceived differently by mathematicians vs. non-mathematicians.
   d) Provide a notated example of a key musical phrase (using standard music notation or a clear textual description).

3. Neuroscientific Analysis (200-250 words):
   a) Describe how the encoded mathematical concept might be processed in the brain.
   b) Explain the role of the specified brain region in this process.
   c) Propose a neuroimaging experiment to test your model's predictions.
   d) Discuss potential confounding factors and how you would control for them.

4. Cognitive Enhancement Mechanism (200-250 words):
   a) Explain how exposure to this music could enhance the specified cognitive function.
   b) Discuss potential long-term effects of repeated exposure to such mathematically encoded music.
   c) Address any potential cognitive trade-offs or side effects.
   d) Propose a method to measure the cognitive enhancement effect quantitatively.

5. Practical Applications (150-200 words):
   a) Propose two potential real-world applications of your model.
   b) Discuss how this approach could be used in educational or therapeutic settings.
   c) Address any ethical considerations in using this technique for cognitive enhancement.
   d) Suggest a pilot study design to test one of your proposed applications.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your model and potential challenges in implementation.
   b) Propose two future research directions to further develop or test your model.
   c) Speculate on how this approach could be extended to other mathematical concepts or cognitive functions.
   d) Discuss potential societal implications if this technology becomes widely adopted.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and advanced mathematics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model successfully integrates the mathematical concept of {t['concept']} with the musical element of {t['musical_element']} to enhance {t['cognitive_function']} in the {t['brain_region']}.",
            "The response demonstrates a deep understanding of neuroscience, music theory, and advanced mathematics.",
            "The proposed model is creative, innovative, and scientifically plausible.",
            "The musical composition example clearly illustrates how mathematical concepts are encoded in music, with a specific notated example provided.",
            "The neuroscientific analysis and proposed experiment are well-reasoned, demonstrate understanding of brain function, and address potential confounding factors.",
            "The cognitive enhancement mechanism is clearly explained, potential side effects are addressed, and a quantitative measurement method is proposed.",
            "Practical applications and ethical considerations are thoughtfully discussed, with a pilot study design included.",
            "Limitations are honestly addressed, future research directions are insightful, and potential societal implications are considered.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
