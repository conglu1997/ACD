import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "primary_modality": "Gravitational waves",
                "secondary_modality": "Chemical signals",
                "cognitive_principle": "Distributed cognition",
                "information_encoding": "Fractal patterns"
            },
            {
                "primary_modality": "Quantum entanglement",
                "secondary_modality": "Bioluminescence",
                "cognitive_principle": "Embodied cognition",
                "information_encoding": "Topological data structures"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multimodal communication system for potential extraterrestrial intelligence, integrating principles from linguistics, cognitive science, and information theory. Your system should use {t['primary_modality']} as the primary modality and {t['secondary_modality']} as a secondary modality. Incorporate the cognitive principle of {t['cognitive_principle']} and use {t['information_encoding']} for information encoding.

Brief explanations:
- Distributed cognition: The idea that cognition and knowledge can be distributed across objects, individuals, artefacts, and tools in the environment.
- Embodied cognition: The theory that many features of cognition are shaped by aspects of the entire body of the organism.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your multimodal communication system.
   b) Explain how it integrates the specified primary and secondary modalities.
   c) Discuss how the system incorporates the given cognitive principle.
   d) Detail your approach to information encoding using the specified method.
   e) Include a high-level diagram or detailed textual description of your system's architecture.

2. Linguistic and Cognitive Foundations (250-300 words):
   a) Explain the linguistic principles underlying your communication system.
   b) Discuss how your system accounts for potential differences in alien cognitive architectures.
   c) Describe how the incorporated cognitive principle influences the system's design and functionality.
   d) Analyze potential challenges in establishing semantic meaning across different cognitive frameworks.

3. Information Theory Analysis (200-250 words):
   a) Discuss the information-theoretic properties of your communication system.
   b) Explain how your encoding method optimizes information transfer.
   c) Analyze the system's robustness against noise and potential for error correction.
   d) Compare the theoretical information density of your system to human language and binary digital systems.

4. Practical Implementation (200-250 words):
   a) Describe how your system could be practically implemented for both transmission and reception.
   b) Discuss any technological challenges in realizing your system and propose solutions.
   c) Explain how your system could be scaled or adapted for different types of extraterrestrial intelligence.
   d) Propose a method for initial calibration and establishment of basic shared references.

5. Hypothetical First Contact Scenario (150-200 words):
   a) Present a brief scenario of first contact using your communication system.
   b) Describe the initial steps in establishing communication.
   c) Discuss potential misunderstandings and how your system might address them.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of initiating communication with extraterrestrial intelligence.
   b) Analyze potential risks or unintended consequences of using your system.
   c) Address limitations of your approach and propose areas for future research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, information theory, and xenobiology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['primary_modality']} and {t['secondary_modality']} as communication modalities.",
            f"The system effectively incorporates the cognitive principle of {t['cognitive_principle']}.",
            f"The information encoding method using {t['information_encoding']} is well-explained and justified.",
            "The response shows innovative integration of linguistics, cognitive science, and information theory.",
            "The practical implementation and first contact scenario are plausible and well-reasoned.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The response adheres to the specified word count and formatting requirements.",
            "The system architecture is clearly described and includes novel approaches.",
            "The linguistic and cognitive foundations are well-explained and consider alien cognitive architectures.",
            "The information theory analysis provides a thorough comparison with existing communication systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
