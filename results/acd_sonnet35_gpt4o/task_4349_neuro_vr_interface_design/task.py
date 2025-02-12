import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "neural_signal": "EEG",
                "ai_technique": "Reinforcement Learning",
                "vr_application": "Therapeutic Environment",
                "brain_region": "Prefrontal Cortex"
            },
            "2": {
                "neural_signal": "fMRI",
                "ai_technique": "Generative Adversarial Networks",
                "vr_application": "Educational Simulation",
                "brain_region": "Hippocampus"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical brain-computer interface (BCI) system that integrates neuroscience, artificial intelligence, and virtual reality to create immersive experiences controlled directly by neural signals. Your system should use {t['neural_signal']} for neural signal acquisition, incorporate {t['ai_technique']} as the primary AI technique, and be applied to create a {t['vr_application']}. Focus on interactions with the {t['brain_region']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your BCI system, including neural signal acquisition, processing, and VR output.
   b) Explain how the AI technique is integrated into the system and its role in interpreting neural signals.
   c) Detail how the system interacts with the specified brain region to control the VR environment.
   d) Propose a novel feature that enhances the system's ability to create immersive experiences.
   e) Include a simple diagram or pseudocode snippet to illustrate a key aspect of your system design. (Describe this textually within your response.)

2. Neural Signal Processing (200-250 words):
   a) Explain the process of acquiring and preprocessing the specified neural signals.
   b) Describe how your system extracts relevant features from these signals.
   c) Discuss any challenges specific to the chosen neural signal type and how you address them.

3. AI-Driven Interpretation (200-250 words):
   a) Detail how the specified AI technique is used to interpret the processed neural signals.
   b) Explain how the AI model is trained and adapted to individual users.
   c) Describe how the AI component handles variability in neural signals across different users or mental states.

4. VR Integration and Feedback (150-200 words):
   a) Describe how the interpreted neural signals are translated into actions or experiences in the VR environment.
   b) Explain how the system provides feedback to the user to facilitate learning and control.
   c) Discuss how the VR environment is optimized for the specific application (e.g., therapy or education).

5. Ethical Considerations and Safety (100-150 words):
   a) Identify potential ethical issues related to direct brain-computer interfaces and immersive VR experiences.
   b) Discuss safety considerations, including potential psychological or physiological risks.
   c) Propose guidelines for responsible development and use of such systems.

6. Future Directions and Implications (150-200 words):
   a) Suggest potential advancements or extensions of your BCI system.
   b) Discuss how your system might contribute to our understanding of brain function and cognition.
   c) Propose a research question that could be investigated using your system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and virtual reality technologies. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

It is recommended to cite relevant scientific papers or resources throughout your response to support your design choices and theoretical foundations.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. System Architecture:') on a new line, followed by your response for that section. Strive for clarity and conciseness in your writing.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates understanding of neuroscience, artificial intelligence, and virtual reality technologies.",
            "The system design is creative while maintaining scientific plausibility.",
            "The response addresses all required sections comprehensively.",
            "The proposed system integrates the specified neural signal, AI technique, VR application, and brain region.",
            "The response includes at least one novel idea or approach in the system design.",
            "Ethical considerations and safety issues are addressed.",
            "The response is well-structured, clear, and within the specified word count range.",
            "The response includes a description of a diagram or pseudocode snippet illustrating a key aspect of the system design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
