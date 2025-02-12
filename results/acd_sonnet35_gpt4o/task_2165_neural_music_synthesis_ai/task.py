import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "auditory cortex",
            "motor cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala"
        ]
        musical_elements = [
            "rhythm",
            "melody",
            "harmony",
            "timbre",
            "dynamics"
        ]
        musical_genres = [
            "classical",
            "jazz",
            "electronic",
            "world music",
            "rock"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "genre": random.choice(musical_genres)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that synthesizes and analyzes music based on neural activity patterns, incorporating principles from neuroscience, music theory, and machine learning. Your system should focus on the {t['brain_region']} brain region, primarily address the musical element of {t['musical_element']}, and be tailored for the {t['genre']} genre. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates principles from neuroscience, music theory, and machine learning.
   c) Detail how the system incorporates neural activity patterns from the {t['brain_region']} in its design and processing.
   d) Discuss how the system is adapted to work with {t['musical_element']} as the primary musical element.
   e) Explain how the system accounts for the characteristics of the {t['genre']} genre in its processing.

2. Neural-Music Mapping (250-300 words):
   a) Describe the process by which your system maps neural activity patterns to musical elements.
   b) Explain how the system interprets and translates neural signals from the {t['brain_region']} into musical parameters.
   c) Provide an example of how the system would generate a musical pattern based on a specific neural activity pattern.
   d) Discuss how the system ensures musical coherence and adherence to {t['genre']} conventions.

3. Music Analysis and Interpretation (250-300 words):
   a) Explain how your system analyzes and interprets existing music in terms of neural activity patterns.
   b) Describe how the system identifies and extracts {t['musical_element']} features from audio input.
   c) Discuss how the system handles variability and complexity in musical structures.
   d) Provide an example of how the system would analyze a given {t['genre']} piece, focusing on the {t['musical_element']} aspect.

4. Creative Applications (200-250 words):
   a) Describe potential creative applications of your system in music composition and performance.
   b) Explain how the system could be used to generate novel musical pieces based on neural inputs.
   c) Discuss how your system might be used to enhance or augment human musical creativity.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues related to using AI and neuroscience in music creation and analysis.
   b) Discuss how your system addresses concerns about artistic authenticity and copyright.
   c) Describe limitations of your system and areas for future improvement.

6. Evaluation Framework (200-250 words):
   a) Propose a method for evaluating the effectiveness of your system in generating and analyzing music.
   b) Describe how you would measure the system's performance in capturing the essence of {t['genre']} and {t['musical_element']}.
   c) Explain how you would assess the neurological accuracy and musical quality of the system's outputs.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of how neural activity in the {t['brain_region']} can be mapped to musical elements, particularly {t['musical_element']}.",
            f"The system design should be well-suited for analyzing and generating music in the {t['genre']} genre.",
            "The proposed AI system should integrate principles from neuroscience, music theory, and machine learning in a coherent and innovative way.",
            "The response should address all six required sections with appropriate depth and insight.",
            "The ideas presented should be creative and novel while maintaining scientific plausibility.",
            "The ethical considerations and limitations should be thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
