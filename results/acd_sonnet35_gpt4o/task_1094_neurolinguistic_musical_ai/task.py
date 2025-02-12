import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_areas = [
            {
                "brain_region": "Broca's area",
                "language_function": "speech production",
                "musical_element": "rhythm"
            },
            {
                "brain_region": "Wernicke's area",
                "language_function": "language comprehension",
                "musical_element": "melody"
            }
        ]
        return {
            "1": random.choice(language_areas),
            "2": random.choice(language_areas)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates neural patterns associated with language processing in {t['brain_region']} into musical compositions, focusing on the language function of {t['language_function']} and the musical element of {t['musical_element']}. Then, analyze the resulting 'neural melodies' (musical compositions derived from neural patterns) for linguistic content. Your response should include:

1. Neurolinguistic-Musical AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it interfaces with brain activity in {t['brain_region']}.
   c) Detail the process of translating neural patterns into {t['musical_element']}.
   d) Discuss how the system preserves linguistic information in the musical output.

2. Neural-Musical Mapping (250-300 words):
   a) Provide a detailed example of how a specific linguistic input would be processed and translated into a musical output.
   b) Explain the correspondence between linguistic features and musical elements.
   c) Discuss any challenges in maintaining the integrity of linguistic information during the translation process.

3. Reverse Translation and Analysis (250-300 words):
   a) Describe a method for analyzing the 'neural melodies' to extract linguistic content.
   b) Explain how your system would handle ambiguities or complex linguistic structures.
   c) Discuss the potential accuracy and limitations of this reverse translation process.

4. Cognitive and Linguistic Implications (200-250 words):
   a) Analyze how this system might impact our understanding of {t['language_function']}.
   b) Discuss potential applications in language learning, therapy, or cognitive enhancement.
   c) Explore any ethical considerations or potential risks of such a system.

5. Experimental Validation (150-200 words):
   a) Propose an experiment to test the effectiveness of your neurolinguistic-musical AI system.
   b) Describe how you would measure its performance in preserving linguistic information.
   c) Discuss potential challenges in experimentally validating such a complex, interdisciplinary system.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, music theory, and artificial intelligence. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Neurolinguistic-Musical AI System Design:', '2. Neural-Musical Mapping:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly.

Your total response should be between 1150-1400 words. Please include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design effectively integrates neurolinguistics, music theory, and artificial intelligence, with a focus on {t['brain_region']} and {t['language_function']}.",
            f"The neural-musical mapping provides a clear and plausible explanation of how linguistic information is translated into {t['musical_element']}.",
            "The reverse translation and analysis method is well-thought-out and addresses potential challenges.",
            "The response demonstrates creativity, interdisciplinary knowledge application, and critical thinking about the implications and limitations of the approach.",
            "The experimental validation proposal is feasible and addresses the unique challenges of the system.",
            "The response follows the specified format with clear headings and is within the required word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
