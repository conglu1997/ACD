import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_enhancements = [
            {
                "enhancement": "Memory Augmentation",
                "quantum_approach": "Quantum Associative Memory",
                "ethical_dilemma": "Inequality in access to cognitive enhancement"
            },
            {
                "enhancement": "Accelerated Learning",
                "quantum_approach": "Quantum Reinforcement Learning",
                "ethical_dilemma": "Potential loss of human diversity in thinking"
            }
        ]
        return {
            "1": random.choice(cognitive_enhancements),
            "2": random.choice(cognitive_enhancements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates complex neural networks and ethical decision-making processes, focusing on the cognitive enhancement of {t['enhancement']} using the quantum approach of {t['quantum_approach']}. Then, use this system to analyze the implications of enhancing human cognitive abilities, particularly addressing the ethical dilemma of {t['ethical_dilemma']}. Your response should include the following sections:

1. Quantum Neural Architecture (300-350 words):
   a) Describe the key components of your quantum neural simulation system.
   b) Explain how your system integrates quantum computing principles with neural network modeling.
   c) Detail how the {t['quantum_approach']} is implemented in your architecture.
   d) Discuss any novel quantum algorithms or techniques you've incorporated to model complex neural processes.

2. Cognitive Enhancement Simulation (250-300 words):
   a) Explain how your system simulates the cognitive enhancement of {t['enhancement']}.
   b) Describe the expected improvements in cognitive function and their underlying mechanisms.
   c) Discuss potential limitations or side effects of this enhancement.
   d) Propose a method for quantifying the enhancement's impact on cognitive performance.

3. Ethical Decision-Making Module (250-300 words):
   a) Describe how your system models ethical decision-making processes.
   b) Explain how quantum principles are applied to simulate moral reasoning.
   c) Discuss how your system handles ethical ambiguities and conflicting values.
   d) Provide an example scenario demonstrating your system's ethical decision-making process.

4. Analysis of Ethical Implications (300-350 words):
   a) Use your quantum neuroethics simulator to analyze the ethical dilemma of {t['ethical_dilemma']}.
   b) Describe the simulation parameters and initial conditions used for this analysis.
   c) Present the results of your simulation, including any unexpected outcomes.
   d) Discuss the broader societal implications of widespread adoption of this cognitive enhancement.

5. Quantum Advantage in Neuroethics (200-250 words):
   a) Explain how quantum computing provides unique advantages in simulating neuroethical scenarios.
   b) Compare the capabilities of your quantum system to classical computing approaches in this domain.
   c) Discuss any quantum phenomena (e.g., superposition, entanglement) that play a crucial role in your simulations.

6. Future Developments and Challenges (200-250 words):
   a) Propose two potential enhancements or extensions to your quantum neuroethics simulator.
   b) Discuss emerging technologies that could further advance this field.
   c) Identify key challenges in implementing this system and suggest approaches to overcome them.

7. Responsible Development Framework (150-200 words):
   a) Propose guidelines for the ethical development and use of quantum-enhanced cognitive technologies.
   b) Discuss safeguards to prevent misuse or unintended consequences of these technologies.
   c) Suggest a governance structure for overseeing research and application in this field.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and ethical philosophy. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and addressing the complexity of the ethical implications.

Format your response with clear headings for each section. Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, neuroscience, and ethical philosophy, particularly in relation to {t['enhancement']} and {t['quantum_approach']}.",
            "The proposed quantum neural architecture is innovative, logically consistent, and effectively integrates quantum computing with neural network modeling.",
            f"The analysis of the ethical implications of {t['ethical_dilemma']} is thorough and insightful, using the quantum neuroethics simulator in a plausible way.",
            "The response addresses the unique advantages of quantum computing in simulating neuroethical scenarios.",
            "The proposed responsible development framework shows a nuanced understanding of the ethical challenges in this field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
