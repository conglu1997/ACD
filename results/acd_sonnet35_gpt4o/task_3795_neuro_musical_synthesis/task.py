import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "prefrontal cortex",
            "auditory cortex",
            "hippocampus",
            "amygdala"
        ]
        musical_elements = [
            "rhythm",
            "harmony",
            "melody",
            "timbre"
        ]
        emotional_states = [
            "joy",
            "sadness",
            "fear",
            "anger"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze music based on neural activity patterns, integrating concepts from neuroscience, music theory, and artificial intelligence. Focus on the brain region: {t['brain_region']}, the musical element: {t['musical_element']}, and the emotional state: {t['emotional_state']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neuro-musical synthesis and analysis.
   b) Explain how your system integrates neural data, musical theory, and emotional processing.
   c) Detail how you model the relationship between {t['brain_region']} activity and {t['musical_element']}.
   d) Discuss any novel AI techniques or algorithms used in your model.

2. Neural-Musical Mapping (250-300 words):
   a) Explain how your system maps neural activity in the {t['brain_region']} to {t['musical_element']}.
   b) Describe how you incorporate the emotional state of {t['emotional_state']} into this mapping.
   c) Discuss any challenges in this mapping process and how your system addresses them.

3. Music Generation Process (250-300 words):
   a) Detail the step-by-step process of how your system generates music based on neural inputs.
   b) Explain how your system ensures musical coherence and emotional resonance.
   c) Provide an example of a musical passage your system might generate, describing its characteristics.

4. Music Analysis Capabilities (200-250 words):
   a) Describe how your system analyzes existing music in terms of neural activity and emotional states.
   b) Explain how it identifies and interprets {t['musical_element']} in relation to {t['brain_region']} activity.
   c) Discuss potential applications of this analysis capability in music therapy or neuroscience research.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your neuro-musical AI system.
   b) Describe potential experiments to validate the system's output against human brain activity and musical perception.
   c) Discuss how you would refine and improve your system based on these evaluations.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical implications of using AI to interpret and generate music based on neural activity.
   b) Discuss privacy concerns and propose guidelines for responsible use of such technology.
   c) Suggest future research directions or potential applications in fields such as neuroscience, music therapy, or AI-assisted composition.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, music theory, and artificial intelligence.",
            f"The system architecture effectively integrates neural data from the {t['brain_region']}, musical theory related to {t['musical_element']}, and processing of the emotional state {t['emotional_state']}.",
            "The neural-musical mapping process is thoroughly explained and scientifically plausible.",
            "The music generation and analysis processes are clearly described and demonstrate innovation.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response is well-structured, coherent, and demonstrates creative problem-solving within the constraints of scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
