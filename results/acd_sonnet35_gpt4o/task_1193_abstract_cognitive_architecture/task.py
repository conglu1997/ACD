import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                'type': 'Gaseous planet with floating organisms',
                'sensory_input': 'Pressure waves and chemical gradients',
                'communication_medium': 'Modulated gas emissions'
            },
            {
                'type': 'Underground fungal network',
                'sensory_input': 'Electrical impulses and chemical signals',
                'communication_medium': 'Mycelial connections'
            }
        ]
        return {str(i+1): {'environment': env} for i, env in enumerate(environments)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an abstract cognitive architecture for a hypothetical non-human intelligence evolved in the following environment:

Environment: {t['environment']['type']}
Primary sensory input: {t['environment']['sensory_input']}
Communication medium: {t['environment']['communication_medium']}

Your task is to create a detailed proposal for this cognitive architecture, including:

1. Sensory Processing (200-250 words):
   - Describe how the organism processes its primary sensory inputs.
   - Explain how this processing is adapted to its environment.
   - Propose at least one novel mechanism for sensory integration.

2. Memory and Learning (200-250 words):
   - Design a system for storing and retrieving information.
   - Explain how this system is suited to the organism's environment and sensory inputs.
   - Describe a unique learning mechanism that could emerge in this cognitive architecture.

3. Decision Making and Problem Solving (200-250 words):
   - Outline the process by which the organism makes decisions and solves problems.
   - Explain how this process is influenced by the environment and available information.
   - Propose a novel approach to problem-solving that this architecture could employ.

4. Communication and Language (200-250 words):
   - Describe how the organism communicates using its primary medium.
   - Explain the structure and properties of its communication system.
   - Propose how this communication system might influence or be influenced by the organism's cognitive processes.

5. Consciousness and Self-Awareness (150-200 words):
   - Discuss whether and how this organism might experience consciousness or self-awareness.
   - Explain how the unique aspects of its cognitive architecture and environment might shape these experiences.

6. Comparative Analysis (150-200 words):
   - Compare and contrast this cognitive architecture with human cognition.
   - Discuss potential advantages or limitations of this architecture compared to human cognition.
   - Propose how studying this hypothetical cognitive architecture could provide insights into human cognition or AI development.

7. Visual Representation (Description of 100-150 words):
   - Provide a text-based description of a simple diagram representing your cognitive architecture.
   - Include key components and their relationships.
   - Explain how this visual representation captures the unique aspects of your design.

Ensure your response is well-structured, scientifically plausible, and demonstrates a deep understanding of cognitive science, neurobiology, and information processing. Be creative in your design while maintaining internal consistency and logical coherence. Use appropriate technical terminology and provide explanations where necessary.

Format your response with clear headings for each section, adhering strictly to the word count guidelines provided. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, neurobiology, and information processing.",
            "The proposed cognitive architecture is creative, internally consistent, and logically coherent.",
            "The design effectively adapts to the given environmental parameters.",
            "The response includes novel mechanisms and approaches in multiple aspects of the cognitive architecture.",
            "The comparative analysis provides insightful connections to human cognition and AI development.",
            "The response adheres to the specified format and word count guidelines for each section.",
            "The visual representation description effectively captures the unique aspects of the cognitive architecture design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
