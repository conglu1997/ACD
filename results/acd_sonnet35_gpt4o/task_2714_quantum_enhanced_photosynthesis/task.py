import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum coherence', 'quantum entanglement', 'quantum tunneling']
        photosynthetic_components = ['light-harvesting complex', 'reaction center', 'electron transport chain']
        return {
            "1": {"quantum_effect": random.choice(quantum_effects), "photosynthetic_component": random.choice(photosynthetic_components)},
            "2": {"quantum_effect": random.choice(quantum_effects), "photosynthetic_component": random.choice(photosynthetic_components)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological mechanism to enhance photosynthesis efficiency using {t['quantum_effect']} in the {t['photosynthetic_component']}, and apply it to create an artificial photosynthesis system for sustainable energy production. Your response should include the following sections:

1. Quantum Biological Mechanism (250-300 words):
   a) Explain the chosen quantum effect and its potential role in photosynthesis.
   b) Describe how this quantum effect could enhance the efficiency of the specified photosynthetic component.
   c) Provide a theoretical model of your proposed quantum biological mechanism.
   d) Discuss any existing research or evidence supporting your proposed mechanism.

2. Artificial Photosynthesis System Design (300-350 words):
   a) Outline the key components of your artificial photosynthesis system.
   b) Explain how your quantum biological mechanism is incorporated into the system design.
   c) Describe the energy conversion process in your system, from light absorption to fuel production.
   d) Include a simple diagram or flowchart illustrating your system's structure and function.

3. Quantum Engineering Challenges (200-250 words):
   a) Identify the main technical challenges in implementing your quantum-enhanced system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any limitations of current technology in realizing your design.

4. Efficiency Analysis (200-250 words):
   a) Estimate the potential efficiency improvement of your quantum-enhanced system compared to natural photosynthesis and current artificial photosynthesis technologies.
   b) Provide a quantitative analysis to support your efficiency claims.
   c) Discuss any trade-offs between efficiency, cost, and scalability in your system.

5. Environmental and Economic Impact (150-200 words):
   a) Analyze the potential environmental benefits of your artificial photosynthesis system.
   b) Discuss the economic viability and potential market impact of your technology.
   c) Address any potential risks or negative consequences of widespread adoption.

6. Future Research Directions (150-200 words):
   a) Propose two specific areas for further research to enhance or validate your quantum biological mechanism.
   b) Suggest a potential interdisciplinary collaboration that could advance this technology.
   c) Speculate on how this research might influence our understanding of quantum effects in other biological systems.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology, as well as their potential applications in energy technology. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, and their potential applications in energy technology.",
            "The proposed quantum biological mechanism is well-explained and scientifically plausible.",
            "The artificial photosynthesis system design is innovative and incorporates the quantum mechanism effectively.",
            "The efficiency analysis provides a convincing quantitative comparison with existing technologies.",
            "The response addresses engineering challenges, environmental impacts, and economic considerations comprehensively.",
            "Future research directions and interdisciplinary collaborations are insightful and well-reasoned.",
            "The response is creative while maintaining scientific accuracy and plausibility.",
            "All sections are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
