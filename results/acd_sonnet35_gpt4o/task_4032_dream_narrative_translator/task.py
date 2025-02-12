import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'sleep_stage': 'REM',
                'brain_region': 'Hippocampus',
                'narrative_element': 'Temporal sequencing',
                'application_domain': 'Psychological therapy'
            },
            {
                'sleep_stage': 'NREM',
                'brain_region': 'Prefrontal cortex',
                'narrative_element': 'Emotional valence',
                'application_domain': 'Creativity enhancement'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates neural activity during {t['sleep_stage']} sleep into coherent narrative structures, with a focus on the {t['brain_region']} and the narrative element of {t['narrative_element']}. Then, analyze its potential applications in {t['application_domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating sleep-related neural activity into narratives.
   b) Explain how your system processes and interprets neural signals from the {t['brain_region']}.
   c) Detail how your system generates coherent narratives from these neural patterns.
   d) Discuss any novel AI techniques or algorithms used in your system.

2. Neural-Linguistic Mapping (250-300 words):
   a) Explain how your system maps neural activity to linguistic elements, particularly {t['narrative_element']}.
   b) Describe the challenges in interpreting subjective experiences from neural data and how your system addresses them.
   c) Discuss how your approach accounts for individual differences in dream content and neural patterns.

3. Narrative Generation Process (250-300 words):
   a) Outline the steps your system takes to construct a coherent narrative from the interpreted neural data.
   b) Explain how your system ensures the narratives maintain logical consistency and structure.
   c) Describe how your system handles ambiguous or fragmented neural patterns in the narrative creation process.

4. Validation and Accuracy (200-250 words):
   a) Propose methods to validate the accuracy of your system's narrative translations.
   b) Describe potential experiments to test the system's performance and reliability.
   c) Discuss the ethical considerations of validating dream narratives and how you would address them.

5. Application in {t['application_domain']} (250-300 words):
   a) Explain how your dream narrative translation system could be applied in the field of {t['application_domain']}.
   b) Describe specific use cases or scenarios where your system could provide valuable insights or benefits.
   c) Discuss any challenges or limitations in applying your system to this domain and how they might be overcome.

6. Ethical Implications and Future Directions (200-250 words):
   a) Analyze the ethical implications of translating private dream experiences into shareable narratives.
   b) Discuss potential misuses of this technology and propose safeguards against them.
   c) Suggest future research directions or enhancements for your system.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, artificial intelligence, and the specific application domain. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            f"The system architecture effectively incorporates the {t['brain_region']} and {t['sleep_stage']} sleep stage.",
            f"The neural-linguistic mapping adequately addresses the narrative element of {t['narrative_element']}.",
            "The narrative generation process is well-explained and scientifically plausible.",
            "The validation and accuracy section proposes robust methods for testing the system.",
            f"The application in {t['application_domain']} is thoroughly explored with specific use cases.",
            "Ethical implications are thoughtfully discussed with proposed safeguards.",
            "The response is innovative and creative while maintaining scientific plausibility.",
            "The response is well-structured, following the required format and word count.",
            "All parts of each section are addressed thoroughly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
