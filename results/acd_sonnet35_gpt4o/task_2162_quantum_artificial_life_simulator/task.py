import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "the evolution of cooperative behavior in a quantum-entangled ecosystem",
            "the emergence of quantum-assisted photosynthesis in a simulated alien biosphere"
        ]
        tasks = {
            "1": {"scenario": random.choice(scenarios)},
            "2": {"scenario": random.choice(scenarios)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired artificial life simulator that models the emergence of complex adaptive systems, then use it to explore {t['scenario']}. Your response should include the following sections:

1. Simulator Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired artificial life simulator.
   b) Explain how quantum principles are incorporated into the simulation of life processes.
   c) Detail how your simulator models complex adaptive systems and emergent behaviors.
   d) Include a diagram or flowchart illustrating the simulator's architecture (describe it textually).

2. Quantum-Biological Integration (200-250 words):
   a) Explain how your simulator integrates quantum mechanics with biological processes.
   b) Describe any novel algorithms or approaches used in your design.
   c) Discuss how your model handles the transition between quantum and classical regimes in biological systems.

3. Evolutionary Scenario Simulation (250-300 words):
   a) Describe how you would set up the simulation for the given scenario: {t['scenario']}.
   b) Explain the key parameters and initial conditions for the simulation.
   c) Predict potential outcomes and emergent behaviors that might arise.
   d) Discuss how quantum effects might influence the evolutionary process in your simulation.

4. Analysis and Interpretation (200-250 words):
   a) Propose methods for analyzing the results of your simulation.
   b) Explain how you would identify and quantify emergent behaviors or patterns.
   c) Discuss the potential implications of your simulation results for our understanding of real-world biological systems.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum-inspired approach to traditional artificial life simulations.
   b) Discuss the potential advantages and limitations of your simulator.
   c) Explain how your simulator might provide insights that classical models cannot.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical concerns related to quantum-inspired artificial life simulations.
   b) Suggest future research directions or potential applications of your simulator in fields such as evolutionary biology, astrobiology, or artificial intelligence.
   c) Discuss how your simulator might be extended to incorporate other quantum or biological phenomena.

Ensure your response demonstrates a deep understanding of quantum mechanics, artificial life, complex systems theory, and evolutionary biology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, artificial life, complex systems theory, and evolutionary biology.",
            "The simulator design is innovative and scientifically plausible.",
            "The evolutionary scenario is thoroughly explored and analyzed.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "Technical terminology is used correctly and complex concepts are clearly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
