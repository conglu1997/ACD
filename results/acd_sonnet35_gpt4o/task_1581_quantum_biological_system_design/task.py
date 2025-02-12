import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                'effect': 'quantum tunneling',
                'biological_context': 'enzyme catalysis',
                'cellular_process': 'metabolic regulation'
            },
            {
                'effect': 'quantum coherence',
                'biological_context': 'photosynthesis',
                'cellular_process': 'energy production'
            },
            {
                'effect': 'quantum entanglement',
                'biological_context': 'magnetoreception',
                'cellular_process': 'navigation in birds'
            },
            {
                'effect': 'quantum superposition',
                'biological_context': 'olfaction',
                'cellular_process': 'scent detection'
            }
        ]
        return {str(i+1): effect for i, effect in enumerate(random.sample(quantum_effects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 45 minutes to complete this task. Design and analyze a hypothetical quantum biological system incorporating the quantum effect of {t['effect']} in the biological context of {t['biological_context']}, focusing on its impact on {t['cellular_process']}. Your response should include:

1. Quantum Biological System Design (300-350 words):
   a) Describe the key components and mechanisms of your proposed quantum biological system.
   b) Explain how the specified quantum effect is integrated into the biological context.
   c) Discuss the theoretical basis for your design, citing relevant principles from quantum physics and biology.
   d) Provide a diagram or schematic representation of your system (describe it textually).
   e) Include at least one equation or mathematical representation related to the quantum effect being discussed.

2. Cellular Impact Analysis (250-300 words):
   a) Analyze how your quantum biological system could influence the specified cellular process.
   b) Discuss potential advantages or enhancements provided by the quantum effect.
   c) Address any challenges or limitations in implementing this system within living cells.

3. Experimental Validation Proposal (250-300 words):
   a) Design an experimental approach to validate the presence and function of your quantum biological system.
   b) Describe specific techniques or technologies that would be required.
   c) Discuss potential obstacles in detecting quantum effects in biological systems and how you would address them.

4. Broader Implications (200-250 words):
   a) Explore potential applications of your quantum biological system in medicine, biotechnology, or other fields.
   b) Discuss how this system might change our understanding of cellular functions or quantum physics.
   c) Address any ethical considerations or potential risks associated with manipulating quantum effects in biological systems.

5. Comparative Analysis (200-250 words):
   a) Compare your proposed quantum biological system to a classical (non-quantum) biological system that serves a similar function.
   b) Discuss the potential evolutionary advantages or disadvantages of quantum-enhanced biological processes.
   c) Speculate on why such quantum systems may or may not have evolved naturally.

6. Future Research Directions (150-200 words):
   a) Propose two potential extensions or modifications to your quantum biological system.
   b) Suggest areas for future research that could further our understanding of quantum effects in biology.
   c) Discuss how advancements in this field might influence other scientific disciplines.

Ensure your response demonstrates a deep understanding of both quantum physics and biology, as well as the potential interplay between these fields. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate terminology from both quantum physics and biology, providing explanations where necessary.

Your total response should be between 1350-1650 words. Use clear headings for each section and number your paragraphs within each section. Responses outside this range or not adhering to the specified format will be penalized."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The quantum biological system effectively incorporates {t['effect']} in the context of {t['biological_context']}.",
            f"The analysis demonstrates a clear understanding of how the quantum effect impacts {t['cellular_process']}.",
            "The response shows creativity and innovation in the system design while maintaining scientific plausibility.",
            "The experimental validation proposal is well-reasoned and addresses the challenges of detecting quantum effects in biological systems.",
            "The response demonstrates a high level of understanding in both quantum physics and biology, using appropriate terminology from both fields.",
            "The response includes at least one relevant equation or mathematical representation related to the quantum effect.",
            "The evolutionary aspects of the quantum biological system are adequately addressed in the comparative analysis section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
