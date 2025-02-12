import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        art_forms = ['painting', 'music', 'sculpture', 'poetry', 'dance']
        cognitive_processes = ['emotion', 'memory', 'attention', 'decision-making', 'imagination']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'input_modality': random.choice(sensory_modalities),
                'output_art_form': random.choice(art_forms),
                'cognitive_process': random.choice(cognitive_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that collaborates with an AI to create synesthetic art experiences, translating neural patterns into multi-sensory artistic outputs. Your system should take {t['input_modality']} input and produce {t['output_art_form']} as output, while focusing on the cognitive process of {t['cognitive_process']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your BCI-AI collaborative system.
   b) Explain how the BCI captures and interprets {t['input_modality']} neural signals.
   c) Detail how the AI processes these signals and translates them into {t['output_art_form']}.
   d) Discuss how the system incorporates the cognitive process of {t['cognitive_process']}.
   e) Include a diagram or flowchart of your system architecture (described in text).

2. Neural-AI Interface (250-300 words):
   a) Explain the mechanism for real-time communication between the human brain and the AI.
   b) Describe how the system maintains a balance between human creativity and AI contributions.
   c) Discuss any novel approaches to preserving the user's artistic intent throughout the process.

3. Synesthetic Mapping (250-300 words):
   a) Detail your approach to mapping {t['input_modality']} neural patterns to {t['output_art_form']}.
   b) Explain how your system creates a coherent synesthetic experience.
   c) Provide an example of how a specific {t['input_modality']} input might be translated into a {t['output_art_form']} output.

4. Cognitive Integration (200-250 words):
   a) Analyze how your system engages with the cognitive process of {t['cognitive_process']}.
   b) Explain how this integration enhances the artistic output or user experience.
   c) Discuss potential insights into {t['cognitive_process']} that might be gained through this system.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to brain-computer interfaces for artistic creation.
   b) Discuss implications for authorship, creativity, and the nature of art.
   c) Propose guidelines for responsible development and use of such technology.

6. Future Implications (150-200 words):
   a) Speculate on how this technology might evolve and impact the art world.
   b) Suggest two potential applications beyond artistic creation.
   c) Discuss how this system might influence our understanding of consciousness and creativity.

Ensure your response demonstrates a deep understanding of neurotechnology, artificial intelligence, and artistic processes. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed BCI-AI collaborative system that takes {t['input_modality']} input and produces {t['output_art_form']} as output, with a clear explanation of the system architecture.",
            f"The system effectively incorporates and analyzes the cognitive process of {t['cognitive_process']}, demonstrating a deep understanding of its role in the artistic creation process.",
            "The synesthetic mapping approach is clearly explained with a specific example, demonstrating creativity and plausibility.",
            "Ethical considerations are thoroughly addressed with appropriate guidelines suggested for responsible development and use.",
            "The response demonstrates a deep understanding of neurotechnology, artificial intelligence, and artistic processes, using appropriate technical terminology.",
            "The proposed system is innovative while maintaining scientific plausibility, and future implications are thoughtfully explored.",
            "The response adheres to the required word count (1350-1650 words) and formatting guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
