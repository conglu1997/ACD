import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum annealing",
            "Quantum walks"
        ]
        evolutionary_processes = [
            "Natural selection",
            "Genetic drift",
            "Gene flow",
            "Mutation",
            "Speciation"
        ]
        ecosystem_factors = [
            "Extreme temperature fluctuations",
            "High radiation levels",
            "Limited resource availability",
            "Rapid environmental changes",
            "Unique atmospheric composition"
        ]
        simulation_timescales = [
            "10,000 years",
            "100,000 years",
            "1 million years",
            "10 million years",
            "100 million years"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_process": random.choice(evolutionary_processes),
                "ecosystem_factor": random.choice(ecosystem_factors),
                "simulation_timescale": random.choice(simulation_timescales)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_process": random.choice(evolutionary_processes),
                "ecosystem_factor": random.choice(ecosystem_factors),
                "simulation_timescale": random.choice(simulation_timescales)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to model and predict complex evolutionary dynamics, then use it to simulate the evolution of a hypothetical alien ecosystem. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the evolutionary process of {t['evolutionary_process']}, and simulate an alien ecosystem characterized by {t['ecosystem_factor']}. Run your simulation for {t['simulation_timescale']}. Your response should include:

1. Quantum-Inspired AI Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how you incorporate {t['quantum_principle']} into your AI architecture.
   c) Detail how your system models and predicts evolutionary dynamics, particularly {t['evolutionary_process']}.
   d) Discuss any novel computational approaches used in your design.

2. Evolutionary Process Modeling (250-300 words):
   a) Explain how your system represents and simulates {t['evolutionary_process']}.
   b) Describe how {t['quantum_principle']} enhances the modeling of this evolutionary process.
   c) Discuss how your system accounts for the complexities and uncertainties in evolutionary dynamics.

3. Alien Ecosystem Simulation (300-350 words):
   a) Describe the initial conditions and key characteristics of your hypothetical alien ecosystem.
   b) Explain how you incorporate {t['ecosystem_factor']} into your simulation.
   c) Detail the major evolutionary events and trends observed over the course of {t['simulation_timescale']}.
   d) Provide a specific example of an organism or trait that evolved in response to the unique conditions.

4. Quantum-Classical Hybrid Approach (200-250 words):
   a) Discuss how your system combines quantum-inspired and classical computing techniques.
   b) Explain the advantages of this hybrid approach for evolutionary simulations.
   c) Address any challenges in integrating quantum and classical methods.

5. Analysis and Predictions (250-300 words):
   a) Analyze the key findings from your simulation.
   b) Compare the evolutionary dynamics observed in your alien ecosystem to those typically seen on Earth.
   c) Make three specific predictions about the future state of your simulated ecosystem beyond the initial {t['simulation_timescale']}.

6. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of evolution and complex systems.
   b) Explore possible applications in fields such as astrobiology, climate science, or biotechnology.
   c) Consider any ethical considerations or potential misuses of such a powerful predictive tool.

Ensure your response demonstrates a deep understanding of quantum computing, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, evolutionary biology, and artificial intelligence.",
            "The quantum-inspired AI architecture is well-designed and clearly incorporates the specified quantum principle.",
            "The evolutionary process modeling is scientifically sound and effectively utilizes the quantum-inspired approach.",
            "The alien ecosystem simulation is creative, plausible, and properly incorporates the specified ecosystem factor.",
            "The analysis and predictions are insightful and well-reasoned, based on the simulation results.",
            "The response addresses all required sections and stays within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
