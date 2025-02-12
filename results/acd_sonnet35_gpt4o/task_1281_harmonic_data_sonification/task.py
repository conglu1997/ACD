import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            "Solar wind interactions with Earth's magnetosphere",
            "Protein folding dynamics in cellular environments",
            "Global ocean currents and heat transfer patterns",
            "Neural activity patterns during complex decision-making",
            "Quantum entanglement in multi-particle systems"
        ]
        musical_elements = [
            "Pitch and harmony",
            "Rhythm and tempo",
            "Timbre and instrumentation",
            "Dynamics and volume",
            "Musical form and structure"
        ]
        tasks = {
            "1": {
                "phenomenon": random.choice(phenomena),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "phenomenon": random.choice(phenomena),
                "musical_element": random.choice(musical_elements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to represent complex datasets as musical compositions, then use it to analyze and interpret scientific phenomena. Your task focuses on the following:

Scientific Phenomenon: {t['phenomenon']}
Primary Musical Element: {t['musical_element']}

Your response should include the following sections:

1. Sonification System Design (250-300 words):
   a) Describe your method for converting data from the given phenomenon into musical elements.
   b) Explain how you will use the primary musical element in your system.
   c) Discuss how other musical elements will be incorporated to represent different aspects of the data.
   d) Provide an example of how a specific data point or pattern would be translated into sound.

2. Data-Music Mapping (200-250 words):
   a) Create a detailed mapping between at least 5 specific data variables from the phenomenon and musical parameters.
   b) Explain the rationale behind each mapping choice.
   c) Discuss how this mapping preserves the integrity and relationships within the original data.

3. Composition and Analysis (250-300 words):
   a) Describe a hypothetical musical piece generated from a dataset related to the phenomenon.
   b) Explain how key features of the phenomenon would be audible in the composition.
   c) Discuss how listening to this piece could provide insights not easily observable in traditional data visualizations.

4. Scientific Interpretation (200-250 words):
   a) Propose a specific hypothesis or research question that could be explored using your sonification system.
   b) Describe how scientists could use your system to analyze and interpret data related to the phenomenon.
   c) Discuss potential advantages and limitations of using this auditory approach compared to visual or numerical analysis methods.

5. Interdisciplinary Implications (150-200 words):
   a) Explore how this sonification approach might benefit other scientific fields or phenomena.
   b) Discuss potential applications in science education or public engagement with scientific concepts.
   c) Propose an interdisciplinary research project that could emerge from this work.

Ensure your response demonstrates a deep understanding of both the scientific phenomenon and musical theory. Be creative in your approach while maintaining scientific rigor and plausibility. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The sonification system design is creative, well-defined, and scientifically plausible",
            "The data-music mapping is detailed, logical, and preserves data integrity",
            "The composition and analysis section demonstrates a deep understanding of both the scientific phenomenon and musical theory",
            "The scientific interpretation and interdisciplinary implications show insightful reasoning and potential for real-world application"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
