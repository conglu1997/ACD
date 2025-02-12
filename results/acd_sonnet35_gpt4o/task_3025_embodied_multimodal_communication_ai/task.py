import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'context': 'A busy restaurant kitchen',
                'communication_modes': ['verbal', 'gestural', 'proxemic'],
                'cognitive_aspect': 'spatial reasoning and coordination'
            },
            {
                'context': 'A multilingual academic conference',
                'communication_modes': ['verbal', 'written', 'visual'],
                'cognitive_aspect': 'cross-cultural conceptual translation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating multimodal communication in an embodied context, then analyze its implications for human-AI interaction and cognitive science. Focus on the following scenario:

Context: {t['context']}
Communication Modes: {', '.join(t['communication_modes'])}
Cognitive Aspect: {t['cognitive_aspect']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for multimodal communication.
   b) Explain how it incorporates embodied cognition principles.
   c) Detail how the system processes and integrates different communication modes.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Multimodal Integration (200-250 words):
   a) Explain how your system integrates information from different communication modes.
   b) Describe any novel algorithms or methods used for multimodal fusion.
   c) Discuss how embodiment influences the interpretation and generation of multimodal signals.

3. Cognitive Modeling (200-250 words):
   a) Describe how your system models the specified cognitive aspect in the given context.
   b) Explain how this modeling aligns with or challenges current theories in cognitive science.
   c) Discuss potential insights your system might provide about human cognition and communication.

4. Human-AI Interaction Scenario (150-200 words):
   a) Provide a specific example of how your AI system would interact with humans in the given context.
   b) Explain how the system would interpret and respond to multimodal cues.
   c) Describe any challenges or unique features of this interaction.

5. Implications for AI Development (200-250 words):
   a) Discuss how your approach to embodied multimodal communication could enhance general AI capabilities.
   b) Explain potential applications in fields such as robotics, virtual agents, or assistive technologies.
   c) Describe how this technology might bridge the gap between current AI systems and human-like communication.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues arising from AI systems capable of nuanced, embodied communication.
   b) Discuss how these issues might be addressed or mitigated.
   c) Consider the broader societal implications of such AI systems.

7. Future Research Directions (100-150 words):
   a) Propose two novel research questions that arise from your system design.
   b) Suggest potential expansions or modifications to your system for future development.

Ensure your response demonstrates a deep understanding of embodied cognition, multimodal communication, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition and multimodal communication principles.",
            "The proposed AI system architecture is innovative and well-explained.",
            "The multimodal integration approach is clearly described and scientifically plausible.",
            "The cognitive modeling aspect is thoughtfully addressed and related to current theories.",
            "The human-AI interaction scenario is realistic and illustrates the system's capabilities well.",
            "The implications for AI development are insightful and well-reasoned.",
            "Ethical considerations are thoroughly explored.",
            "Future research directions are promising and well-justified.",
            "The overall response is creative, coherent, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
