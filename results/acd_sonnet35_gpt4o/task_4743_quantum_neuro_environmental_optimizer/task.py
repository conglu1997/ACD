import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Quantum entanglement",
                "neural_data_type": "Electroencephalogram (EEG)",
                "ecosystem": "Coral reef",
                "environmental_challenge": "Ocean acidification",
                "species": ["coral polyps", "clownfish", "parrotfish"]
            },
            {
                "quantum_principle": "Quantum superposition",
                "neural_data_type": "Functional near-infrared spectroscopy (fNIRS)",
                "ecosystem": "Tropical rainforest",
                "environmental_challenge": "Deforestation",
                "species": ["howler monkeys", "toucans", "jaguars"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-neural hybrid AI system that optimizes environmental resource management by simulating ecosystem dynamics at a quantum level and integrating real-time neurological data from multiple species. Your system should incorporate the quantum principle of {t['quantum_principle']}, utilize {t['neural_data_type']} for neural data collection, focus on the {t['ecosystem']} ecosystem, and address the environmental challenge of {t['environmental_challenge']}. Consider the following species in your ecosystem: {', '.join(t['species'])}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-neural hybrid AI system.
   b) Explain how quantum computing is integrated with neural network processing.
   c) Detail how the system collects and processes real-time neurological data from the specified species.
   d) Provide a high-level diagram or flowchart of your system (describe it textually using ASCII characters).

2. Quantum-Neural Integration (250-300 words):
   a) Explain how {t['quantum_principle']} is utilized in your system's ecosystem simulations.
   b) Describe how quantum computations interface with neural network processing.
   c) Discuss potential advantages and challenges of this hybrid approach.
   d) Provide a brief example of how your system would simulate a specific ecosystem interaction at the quantum level.

3. Ecosystem Modeling (250-300 words):
   a) Outline how your system models the {t['ecosystem']} ecosystem at a quantum level.
   b) Explain how neurological data from the specified species is incorporated into the model.
   c) Describe how the system predicts and optimizes ecosystem dynamics.

4. Environmental Challenge Application (200-250 words):
   a) Detail how your system addresses {t['environmental_challenge']}.
   b) Provide a specific scenario demonstrating the system's problem-solving approach.
   c) Discuss potential limitations of your approach and propose solutions.

5. Data Collection and Privacy (150-200 words):
   a) Explain how {t['neural_data_type']} data is collected from the specified species.
   b) Discuss ethical considerations and propose guidelines for responsible data collection.
   c) Describe measures to ensure data privacy and security.

6. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate your system's effectiveness in environmental resource management.
   b) Describe an experiment to test your system's performance against traditional methods.
   c) Discuss how you would validate the accuracy of your quantum-level ecosystem simulations.

7. Future Implications and Societal Impact (150-200 words):
   a) Discuss potential long-term effects of implementing your system on ecosystem management and conservation.
   b) Explore how this technology might influence human-nature relationships and environmental policies.
   c) Propose related areas of research that could enhance quantum-neural environmental management.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and environmental science. Be creative and innovative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing (specifically {t['quantum_principle']}), neuroscience (including {t['neural_data_type']}), and environmental science (focusing on {t['ecosystem']} and {t['environmental_challenge']})",
            "The system architecture is innovative, well-explained, and incorporates the specified quantum principle and neural data type",
            "The quantum-neural integration is plausibly described, addresses potential challenges, and includes a specific example of quantum-level ecosystem simulation",
            f"The ecosystem modeling approach is well-thought-out and considers both quantum aspects and neurological data from {', '.join(t['species'])}",
            f"The application to {t['environmental_challenge']} is clearly explained and includes a plausible scenario",
            "The data collection and privacy considerations are thoroughly addressed, with specific reference to the given species",
            "The response includes a textual ASCII representation of the system architecture or flowchart",
            "The response is well-formatted with clear headings and falls within the specified word count range (1450-1800 words)",
            "The response demonstrates proficiency in all key areas: quantum computing, neuroscience, environmental science, system design, and ethical considerations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
