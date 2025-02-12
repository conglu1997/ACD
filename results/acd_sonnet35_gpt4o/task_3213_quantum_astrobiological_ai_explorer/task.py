import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Quantum entanglement",
            "Quantum superposition",
            "Quantum tunneling"
        ]
        biosignatures = [
            "Atmospheric methane",
            "Oxygen-ozone disequilibrium",
            "Red edge effect from vegetation"
        ]
        planetary_types = [
            "Super-Earth",
            "Ocean world",
            "Desert planet"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biosignature": random.choice(biosignatures),
                "planet_type": random.choice(planetary_types)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biosignature": random.choice(biosignatures),
                "planet_type": random.choice(planetary_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for detecting and analyzing potential biosignatures on exoplanets, focusing on the quantum principle of {t['quantum_principle']}, the biosignature {t['biosignature']}, and the planetary type {t['planet_type']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI system for exoplanet biosignature detection.
   b) Explain how you incorporate the specified quantum principle into the AI architecture.
   c) Detail how your system is optimized for detecting the given biosignature on the specified planetary type.
   d) Include a high-level diagram of your system architecture (described in words).
   e) Provide a brief pseudocode snippet illustrating a key aspect of your quantum-AI integration.

2. Quantum-Classical Integration (250-300 words):
   a) Explain how quantum and classical computing elements interact in your system.
   b) Describe any novel algorithms or techniques used in this integration.
   c) Discuss potential advantages of your quantum-enhanced approach over classical methods in biosignature detection.

3. Biosignature Analysis Process (250-300 words):
   a) Outline the step-by-step process your system uses to detect and analyze the specified biosignature.
   b) Explain how the quantum principle enhances this analysis.
   c) Discuss how your system accounts for potential false positives or ambiguities in biosignature detection.

4. Adaptive Learning and Uncertainty Handling (200-250 words):
   a) Describe how your system adapts to new data and refines its detection capabilities.
   b) Explain how it handles uncertainties inherent in exoplanet observation and biosignature detection.
   c) Propose a method for quantifying confidence levels in biosignature detection results.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss ethical considerations in the use of advanced AI for detecting extraterrestrial life.
   b) Explore the philosophical implications of potential biosignature discoveries.
   c) Propose guidelines for responsible disclosure and verification of potential biosignature detections.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how this technology might influence the search for extraterrestrial life and our understanding of astrobiology.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and astrobiology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response incorporates the quantum principle of {t['quantum_principle']} in a plausible and innovative way.",
            f"The system is well-designed for detecting the biosignature {t['biosignature']} on a {t['planet_type']}.",
            "The response demonstrates a deep understanding of quantum computing, AI, and astrobiology.",
            "The ethical and philosophical implications are thoughtfully considered.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "The response follows the specified format and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
