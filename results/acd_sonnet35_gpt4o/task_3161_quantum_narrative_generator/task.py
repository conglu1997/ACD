import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'narrative_element': 'Character development',
                'cognitive_aspect': 'Decision-making'
            },
            {
                'quantum_principle': 'Entanglement',
                'narrative_element': 'Plot structure',
                'cognitive_aspect': 'Memory formation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that generates multi-dimensional narratives based on the quantum principle of {t['quantum_principle']}, focusing on the narrative element of {t['narrative_element']} and its impact on the cognitive aspect of {t['cognitive_aspect']}. Then, analyze its implications for storytelling and human cognition. Your response should include:

1. Quantum Narrative System Architecture (300-350 words):
   a) Describe the key components of your quantum narrative generation system.
   b) Explain how it incorporates the specified quantum principle in narrative creation.
   c) Detail how the system models and generates the given narrative element.
   d) Discuss how your system accounts for and influences the specified cognitive aspect.

2. Quantum-Narrative Mapping (250-300 words):
   a) Explain how quantum states or processes in your system correspond to narrative elements.
   b) Provide a specific example of how this mapping works for the given narrative element.
   c) Discuss potential advantages of this quantum-inspired approach over classical narrative generation.

3. Multi-dimensional Narrative Generation (250-300 words):
   a) Describe the process of generating a multi-dimensional narrative using your system.
   b) Explain how the quantum principle enhances or alters traditional storytelling.
   c) Provide a brief example of a quantum-generated narrative fragment, highlighting its unique features.

4. Cognitive Impact Analysis (200-250 words):
   a) Analyze how exposure to quantum-generated narratives might affect the specified cognitive aspect.
   b) Discuss potential long-term implications for human cognition and creativity.
   c) Propose an experiment to measure the cognitive effects of quantum-generated narratives.

5. Philosophical and Ethical Implications (200-250 words):
   a) Explore the philosophical questions raised by quantum narrative generation.
   b) Discuss ethical considerations in using quantum computing for creative expression.
   c) Speculate on how this technology might influence our understanding of consciousness and reality.

6. Future Applications and Research Directions (150-200 words):
   a) Propose two potential applications of quantum narrative generation beyond entertainment.
   b) Suggest areas for future research that could further develop this technology.
   c) Discuss how quantum narrative generation might intersect with other fields of study.

Ensure your response demonstrates a deep understanding of quantum physics, narrative theory, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, narrative theory, and cognitive science.",
            "The proposed quantum narrative generation system is creative, internally consistent, and scientifically plausible.",
            "The system effectively integrates the specified quantum principle and narrative element in its design and output.",
            "The response includes novel approaches to narrative generation and analysis of cognitive impacts.",
            "The philosophical and ethical implications are thoughtfully explored and logically presented.",
            "The response addresses all required sections and adheres to the specified word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
