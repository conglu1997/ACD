import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "bird_species": "European Robin",
                "navigation_scenario": "Long-distance migration",
                "quantum_principle": "Entanglement",
                "magnetic_field_strength": "50 μT",
                "example_flight_path": "[51.5074° N, 0.1278° W] to [59.3293° N, 18.0686° E]"
            },
            "2": {
                "bird_species": "Arctic Tern",
                "navigation_scenario": "Pole-to-pole migration",
                "quantum_principle": "Superposition",
                "magnetic_field_strength": "30 μT",
                "example_flight_path": "[82.5° N, 62.3° W] to [64.9° S, 64.0° W]"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network to model the navigation system of the {t['bird_species']} during {t['navigation_scenario']}, incorporating the quantum principle of {t['quantum_principle']}. Consider the Earth's magnetic field strength of {t['magnetic_field_strength']} and the example flight path: {t['example_flight_path']}. Your response should address the following points:

1. Quantum-Biological Model (300-350 words):
   a) Explain the current scientific understanding of how birds might use quantum effects in navigation.
   b) Describe how the {t['quantum_principle']} principle could be involved in this process.
   c) Propose a model for how quantum effects in the bird's brain could interact with Earth's magnetic field.
   d) Discuss how your model accounts for the given magnetic field strength and example flight path.

2. Neural Network Architecture (350-400 words):
   a) Design a novel neural network architecture that incorporates quantum-inspired elements.
   b) Explain how your architecture mimics or utilizes the proposed quantum-biological processes.
   c) Describe at least three key components of your architecture and their interactions.
   d) Illustrate how your network would process navigational cues and generate directional output.
   e) Provide a diagram or pseudocode representation of your architecture.

3. Implementation Strategy (250-300 words):
   a) Outline a potential method for implementing your quantum-inspired neural network.
   b) Discuss any novel algorithms or data structures required.
   c) Explain how your implementation could be trained or optimized using real-world data.
   d) Address challenges in simulating quantum effects in a classical computing environment.
   e) Propose a method for validating your model using the given flight path data.

4. Performance Analysis (250-300 words):
   a) Propose metrics to evaluate the performance of your model in simulating bird navigation.
   b) Compare the expected performance to classical neural network approaches.
   c) Discuss how your model could be validated against observed bird navigation behaviors.
   d) Analyze potential limitations of your approach and areas for future improvement.
   e) Estimate the computational resources required to run your model.

5. Broader Implications (200-250 words):
   a) Discuss how your model could contribute to our understanding of quantum biology.
   b) Explore potential applications of your quantum-inspired neural network beyond bird navigation.
   c) Address ethical considerations in developing AI systems that mimic biological quantum processes.
   d) Speculate on how this technology might impact future research in neuroscience and AI.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing potential limitations.

Format your response with clear headings for each section, and include subheadings for each point (a, b, c, etc.). Your total response should be between 1350-1600 words. Include relevant calculations, diagrams, or pseudocode where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence, with appropriate use of technical terminology.",
            f"The quantum-biological model incorporates the {t['quantum_principle']} principle and accounts for the given magnetic field strength of {t['magnetic_field_strength']}.",
            "The proposed neural network architecture incorporates quantum-inspired elements in a novel and plausible way, with at least three key components clearly described.",
            "The implementation strategy addresses challenges in simulating quantum effects in a classical computing environment and proposes a method for validation using the given flight path data.",
            "The performance analysis includes meaningful comparisons to classical approaches, discusses validation methods, and estimates computational resources required.",
            "The response explores broader implications and ethical considerations of the proposed model, including potential impacts on future research.",
            "The response is well-formatted with clear headings and subheadings, and includes relevant calculations, diagrams, or pseudocode where appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
