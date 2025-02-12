import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'math_concept': 'Fourier transform',
                'musical_element': 'Harmony',
                'brain_region': 'Auditory cortex'
            },
            {
                'math_concept': 'Fractal geometry',
                'musical_element': 'Rhythm',
                'brain_region': 'Prefrontal cortex'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the mathematical concept of {t['math_concept']} into a musical composition focusing on {t['musical_element']}, then analyze how this composition is processed in the {t['brain_region']}. 

Brief explanations:
- {t['math_concept']}: {TaskFamily.get_math_explanation(t['math_concept'])}
- {t['musical_element']}: {TaskFamily.get_music_explanation(t['musical_element'])}

Your task has the following components:

1. Mathematical-Musical Translation System (250-300 words):
   a) Describe your system for translating {t['math_concept']} into musical elements, focusing on {t['musical_element']}.
   b) Explain how your system preserves the key properties of the mathematical concept in the musical translation.
   c) Provide a specific example of how a particular aspect of {t['math_concept']} would be represented musically.
   d) Include a brief textual description of a visual representation of your translation system (e.g., a diagram or flowchart).

2. Composition Analysis (200-250 words):
   a) Describe the structure and characteristics of the resulting musical composition.
   b) Explain how the composition reflects the underlying mathematical concept.
   c) Discuss any challenges or limitations in representing {t['math_concept']} through {t['musical_element']}.

3. Neurocognitive Processing (200-250 words):
   a) Describe how the {t['brain_region']} would be involved in processing this mathematical-musical composition.
   b) Explain any unique activation patterns you would expect to see in the {t['brain_region']} when listening to this composition.
   c) Discuss how the brain's processing of this composition might differ from its processing of traditional music.

4. Experimental Design (150-200 words):
   a) Propose an experiment to test how the {t['brain_region']} processes your mathematical-musical composition.
   b) Describe the methodology, including any brain imaging techniques you would use.
   c) Explain what results would support your hypotheses about the neural processing of the composition.

5. Cognitive Implications (150-200 words):
   a) Discuss how this mathematical-musical system might enhance understanding or recall of {t['math_concept']}.
   b) Explain potential applications of your system in mathematics education or cognitive therapy.
   c) Propose how this system might be extended to other mathematical concepts or brain regions.

6. Artistic and Cultural Considerations (100-150 words):
   a) Discuss the artistic merit of the resulting composition beyond its mathematical representation.
   b) Explain how different cultural musical traditions might influence the interpretation of your mathematical-musical mappings.

Ensure your response demonstrates a deep understanding of {t['math_concept']}, music theory (especially {t['musical_element']}), and the function of the {t['brain_region']}. Use appropriate terminology from each field and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def get_math_explanation(concept: str) -> str:
        explanations = {
            'Fourier transform': 'A mathematical method that decomposes a function of time into its constituent frequencies',
            'Fractal geometry': 'A branch of mathematics that studies complex patterns that are self-similar across different scales'
        }
        return explanations.get(concept, 'A complex mathematical concept')

    @staticmethod
    def get_music_explanation(element: str) -> str:
        explanations = {
            'Harmony': 'The combination of simultaneous musical notes to produce chords and chord progressions',
            'Rhythm': 'The pattern of regular or irregular pulses in music, often expressed through the duration and accentuation of notes'
        }
        return explanations.get(element, 'A fundamental element of musical composition')

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified mathematical concept and its translation into music.",
            "The musical composition analysis is thorough and clearly relates to the underlying mathematical principles.",
            "The neurocognitive processing explanation is scientifically grounded and specific to the given brain region.",
            "The experimental design is well-thought-out and appropriate for testing the hypotheses.",
            "The discussion of cognitive implications and potential applications is insightful and creative.",
            "The artistic and cultural considerations demonstrate an understanding of music beyond its mathematical representation.",
            "The overall response shows strong interdisciplinary integration of mathematics, music, and neuroscience.",
            "The response includes a clear description of a visual representation of the translation system.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
