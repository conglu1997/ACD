import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = [
            ('visual', 'auditory'),
            ('auditory', 'tactile')
        ]
        cognitive_processes = [
            'decision making',
            'emotional processing'
        ]
        tasks = [
            {
                'modalities': modality_pair,
                'cognitive_process': process
            }
            for modality_pair, process in zip(modalities, cognitive_processes)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel multimodal communication system for AI that integrates {t['modalities'][0]} and {t['modalities'][1]} modalities. Then, analyze its potential impact on human-AI interaction and the cognitive process of {t['cognitive_process']}. Your response should include the following sections:

1. Multimodal System Design (300-350 words):
   a) Describe the key components of your multimodal AI communication system.
   b) Explain how it integrates {t['modalities'][0]} and {t['modalities'][1]} modalities.
   c) Detail the novel features that distinguish your system from existing multimodal AI systems.
   d) Discuss how your system addresses challenges in multimodal integration and synchronization.

2. Linguistic and Cognitive Foundations (250-300 words):
   a) Explain the linguistic theories or principles that underpin your multimodal system.
   b) Describe how your system reflects or challenges current understanding of human multimodal communication.
   c) Discuss any novel semantic or syntactic structures employed in your system.

3. Technical Implementation (250-300 words):
   a) Outline the AI architecture required to implement your multimodal system.
   b) Explain key algorithms or neural network structures used for modality integration.
   c) Discuss how your system handles potential conflicts or inconsistencies between modalities.
   d) Address scalability and real-time processing considerations.

4. Human-AI Interaction Analysis (200-250 words):
   a) Analyze how your multimodal system could enhance human-AI interaction.
   b) Discuss potential challenges or barriers in human adaptation to this new form of communication.
   c) Propose metrics for evaluating the effectiveness of your system in human-AI interactions.

5. Cognitive Impact Assessment (200-250 words):
   a) Examine how your multimodal system might influence the cognitive process of {t['cognitive_process']}.
   b) Discuss potential short-term and long-term effects on human cognitive abilities.
   c) Analyze how this system might shape human perception and processing of multimodal information.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify key ethical issues related to the development and use of your multimodal AI communication system.
   b) Propose guidelines for responsible development and implementation.
   c) Suggest two potential extensions or applications of your system in other domains.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The multimodal communication system design is innovative, coherent, and scientifically plausible.",
            "The analysis of human-AI interaction and cognitive impact is well-reasoned and insightful.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The submission uses appropriate technical terminology and provides clear explanations of complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
