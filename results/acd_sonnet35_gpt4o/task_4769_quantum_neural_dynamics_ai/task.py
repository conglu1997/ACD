import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        neural_processes = [
            "synaptic transmission",
            "action potential propagation",
            "memory formation"
        ]
        cognitive_functions = [
            "decision making",
            "pattern recognition",
            "emotional processing"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "neural_process": random.choice(neural_processes),
                "cognitive_function": random.choice(cognitive_functions)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "neural_process": random.choice(neural_processes),
                "cognitive_function": random.choice(cognitive_functions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to simulate and analyze the potential role of {t['quantum_effect']} in {t['neural_process']}, with a focus on its implications for {t['cognitive_function']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating quantum neural dynamics.
   b) Explain how your system models the specified quantum effect in neural processes.
   c) Detail how the system analyzes the impact on the given cognitive function.
   d) Include a high-level diagram or pseudocode snippet illustrating a core aspect of your system.

2. Quantum-Neural Interface (250-300 words):
   a) Explain how your system bridges quantum and classical aspects of neural function.
   b) Discuss any novel approaches to modeling quantum effects in a neurobiological context.
   c) Address potential challenges in accurately representing quantum phenomena in neural simulations.

3. Simulation Methodology (200-250 words):
   a) Describe the simulation techniques used in your AI system.
   b) Explain how you validate the accuracy of your quantum neural simulations.
   c) Discuss how your system handles the complexity and scale of neural networks.

4. Data Analysis and Interpretation (200-250 words):
   a) Explain how your AI system analyzes the simulation results.
   b) Describe the metrics and methods used to quantify the impact of quantum effects on neural processes.
   c) Discuss how your system might distinguish quantum effects from classical neural dynamics.

5. Implications for Cognitive Science (150-200 words):
   a) Discuss potential implications of your findings for our understanding of {t['cognitive_function']}.
   b) Speculate on how quantum effects in neural processes might influence broader cognitive phenomena.
   c) Propose a testable hypothesis based on your system's predictions.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical implications of research into quantum neural dynamics.
   b) Discuss possible societal impacts of a deeper understanding of quantum effects in cognition.
   c) Propose guidelines for responsible development and use of quantum-inspired AI systems.

7. Future Research Directions (100-150 words):
   a) Suggest two potential expansions or modifications to your system to explore additional aspects of quantum neural dynamics.
   b) Discuss how empirical neuroscience research could validate or challenge your system's predictions.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']}, {t['neural_process']}, and {t['cognitive_function']}.",
            "The AI system design is innovative and addresses the complexities of simulating quantum effects in neural networks.",
            "The analysis of potential implications for cognitive science is thorough and insightful.",
            "Ethical considerations are well-thought-out and address relevant issues in quantum-inspired AI research.",
            "The proposed future research directions are promising and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
