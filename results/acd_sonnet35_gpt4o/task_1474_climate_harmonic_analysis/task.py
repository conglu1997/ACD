import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = [
            {
                'variable': 'Temperature',
                'unit': 'Celsius',
                'musical_element': 'Pitch'
            },
            {
                'variable': 'Precipitation',
                'unit': 'mm',
                'musical_element': 'Rhythm'
            },
            {
                'variable': 'Wind speed',
                'unit': 'km/h',
                'musical_element': 'Dynamics'
            },
            {
                'variable': 'Atmospheric pressure',
                'unit': 'hPa',
                'musical_element': 'Harmony'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(climate_variables, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates climate data into musical compositions, then use harmonic analysis to interpret and predict climate patterns. Focus on the climate variable of {t['variable']} (measured in {t['unit']}) and its corresponding musical element of {t['musical_element']}. Your response should include the following sections:

1. Data-to-Music Translation System (300-350 words):
   a) Describe your method for converting {t['variable']} data into {t['musical_element']}.
   b) Explain how your system preserves the integrity and patterns of the climate data in the musical output.
   c) Provide an example of how a specific {t['variable']} pattern would be represented musically.
   d) Discuss how your system handles extreme values or anomalies in the data.
   e) Explain how your translation method could be scaled to incorporate multiple climate variables simultaneously.
   f) Provide a simple mathematical formula or algorithm that formalizes your data-to-music translation process.
   g) Give a brief example of the musical notation or representation that would result from the following sample data: [{t['variable']} readings over 5 days: 15.2, 16.8, 14.5, 17.1, 15.9 {t['unit']}]

2. Harmonic Analysis Methodology (250-300 words):
   a) Describe your approach to analyzing the musical compositions generated from climate data.
   b) Explain how traditional music theory concepts (e.g., intervals, chord progressions, cadences) are applied to interpret climate patterns.
   c) Discuss any novel analytical techniques you've developed specifically for this climate-music system.
   d) Provide an example of how a specific musical pattern in your system would be interpreted in terms of climate behavior.

3. Climate Pattern Prediction (200-250 words):
   a) Explain how your harmonic analysis can be used to predict future climate patterns.
   b) Describe the mathematical or statistical models you would use to transform musical predictions back into climate projections.
   c) Discuss the potential accuracy and limitations of this prediction method.
   d) Compare your music-based prediction method to traditional climate modeling techniques.

4. Interdisciplinary Implications (200-250 words):
   a) Explore how this climate-music system might lead to new insights in climate science.
   b) Discuss potential applications in other scientific fields or artistic domains.
   c) Consider how this approach might enhance public understanding and engagement with climate data.
   d) Propose an experiment to test the effectiveness of your system in a real-world scenario.

5. Ethical Considerations and Challenges (150-200 words):
   a) Address potential ethical issues in representing critical climate data through music.
   b) Discuss challenges in ensuring scientific rigor while using an artistic medium.
   c) Consider potential misuse or misinterpretation of your system and propose safeguards.

Ensure your response demonstrates a deep understanding of music theory, mathematical modeling, and climate science. Use appropriate terminology from all fields and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, mathematical modeling, and climate science, using appropriate terminology from all fields.",
            f"The data-to-music translation system for {t['variable']} to {t['musical_element']} is well-explained, creative, and scientifically plausible.",
            "The harmonic analysis methodology effectively applies music theory concepts to interpret climate patterns.",
            "The climate pattern prediction method using musical analysis is logically explained and compared to traditional techniques.",
            "The interdisciplinary implications section explores novel applications and proposes a realistic experiment.",
            "Ethical considerations and challenges are thoughtfully addressed with proposed safeguards.",
            "The response is well-structured, adhering to the specified sections and word counts.",
            "A mathematical formula or algorithm for the data-to-music translation process is provided and clearly explained.",
            "An example of musical notation or representation for the given climate data sample is included and consistent with the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
