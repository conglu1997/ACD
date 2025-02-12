import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                'biological_process': 'Photosynthesis',
                'quantum_effect': 'Quantum coherence in energy transfer',
                'application_domain': 'Energy-efficient computing'
            },
            {
                'biological_process': 'Magnetoreception in birds',
                'quantum_effect': 'Quantum entanglement in cryptochrome proteins',
                'application_domain': 'Quantum sensing and navigation'
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum biological information processing system inspired by {t['biological_process']}, focusing on the quantum effect of {t['quantum_effect']}. Then, analyze its potential applications in {t['application_domain']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum biological information processing system.
   b) Explain how it incorporates the quantum effect {t['quantum_effect']} observed in {t['biological_process']}.
   c) Discuss how your system leverages biological principles to achieve quantum information processing.
   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your system.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system bridges the gap between quantum effects and biological structures.
   b) Describe any novel materials or techniques required to maintain quantum effects in a biological context.
   c) Discuss how your system addresses the challenge of maintaining quantum coherence in a warm, wet biological environment.

3. Information Processing Capabilities (200-250 words):
   a) Analyze the information processing capabilities of your system, including any quantum advantages.
   b) Compare its performance to classical computing systems in relevant metrics (e.g., speed, energy efficiency, or information density).
   c) Describe a specific computation or algorithm that your system could perform more efficiently than classical computers.

4. Applications in {t['application_domain']} (200-250 words):
   a) Propose at least two novel applications of your system in {t['application_domain']}.
   b) Explain how these applications leverage the unique features of your quantum biological system.
   c) Discuss the potential impact of these applications on the field and society at large.

5. Challenges and Future Directions (150-200 words):
   a) Identify major technical challenges in realizing your proposed system.
   b) Suggest potential solutions or research directions to address these challenges.
   c) Speculate on future developments that could enhance or expand your system's capabilities.

6. Ethical and Philosophical Implications (100-150 words):
   a) Discuss any ethical considerations arising from the development and use of your system.
   b) Explore how your system might influence our understanding of the relationship between quantum physics, biology, and information processing.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and information theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section. Your entire response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['biological_process']} and how it relates to {t['quantum_effect']}.",
            "The proposed quantum biological information processing system is innovative and scientifically plausible.",
            f"The applications in {t['application_domain']} are novel and well-explained.",
            "The response shows a deep integration of knowledge from quantum physics, biology, and information theory.",
            "The challenges, future directions, and ethical implications are thoughtfully considered.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
