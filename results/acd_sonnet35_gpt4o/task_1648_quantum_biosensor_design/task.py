import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum entanglement",
            "quantum superposition",
            "quantum tunneling"
        ]
        pollutants = [
            "heavy metals",
            "microplastics",
            "pesticides",
            "pharmaceutical residues"
        ]
        ecosystems = [
            "coral reef",
            "rainforest river",
            "urban lake",
            "arctic tundra"
        ]
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "pollutant": random.choice(pollutants),
                "ecosystem": random.choice(ecosystems)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "pollutant": random.choice(pollutants),
                "ecosystem": random.choice(ecosystems)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based biosensor system for real-time detection of {t['pollutant']} in a {t['ecosystem']} environment, utilizing the quantum principle of {t['quantum_principle']}. Your response should include the following sections, each with its own heading:

1. Quantum Biosensor Design (300-350 words):
   a) Describe the overall structure and components of your quantum biosensor system.
   b) Explain how you incorporate the specified quantum principle into the biosensor design.
   c) Detail the biochemical mechanisms used for detecting the given pollutant.
   d) Discuss how your design is optimized for the specific ecosystem.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system integrates quantum components with biological sensing elements.
   b) Describe any novel features that enhance sensitivity or specificity of pollutant detection.
   c) Discuss potential challenges in maintaining quantum effects in a biological environment and how you address them.

3. Data Processing and Analysis (200-250 words):
   a) Outline the data processing pipeline from quantum signal to actionable environmental information.
   b) Explain how your system achieves real-time monitoring capability.
   c) Describe any machine learning or AI components used in data interpretation.

4. Environmental Impact and Implementation (200-250 words):
   a) Analyze the potential ecological impact of deploying your quantum biosensor system in the given ecosystem.
   b) Propose a strategy for implementing a network of these biosensors for comprehensive monitoring.
   c) Discuss how the real-time data from your system could inform environmental management decisions.

5. Practical Limitations and Future Developments (150-200 words):
   a) Identify current technological limitations that may affect the performance of your quantum biosensor system.
   b) Suggest potential future advancements that could overcome these limitations.
   c) Propose one other environmental application for your quantum biosensor technology.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using quantum-enhanced environmental monitoring systems.
   b) Address privacy concerns related to collecting high-resolution environmental data.
   c) Propose guidelines for responsible development and use of quantum biosensor technologies.

7. Mathematical Representation (100-150 words):
   a) Provide at least one equation or mathematical representation that describes a key aspect of your quantum biosensor system.
   b) Explain the significance of each term in your equation and how it relates to the system's function.

Ensure your response demonstrates a deep understanding of quantum physics, biochemistry, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Quantum Biosensor Design:') followed by your response for that section. Your total response should be between 1300-1650 words.

IMPORTANT: Your response should be complete and coherent. Do not include any placeholder text or incomplete sections."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and how it can be applied to biosensor design for detecting {t['pollutant']} in a {t['ecosystem']} environment.",
            "The quantum biosensor design is innovative, well-explained, and scientifically plausible.",
            "The quantum-biological interface is clearly described and addresses potential challenges.",
            "The data processing and analysis section provides a coherent pipeline from quantum signal to environmental information.",
            "The environmental impact and implementation strategy is well-reasoned and ecosystem-specific.",
            "Practical limitations are identified and future developments are proposed.",
            "Ethical considerations are thoughtfully discussed with relevant guidelines proposed.",
            "The mathematical representation is relevant and correctly explained.",
            "The response follows the specified format with clear headings for each section.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from quantum physics, biochemistry, and environmental science in a novel and scientifically plausible manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
