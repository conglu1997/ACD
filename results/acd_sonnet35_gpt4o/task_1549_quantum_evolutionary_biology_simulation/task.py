import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            "quantum coherence in photosynthesis",
            "quantum tunneling in enzyme catalysis",
            "quantum entanglement in magnetoreception",
            "quantum superposition in olfaction"
        ]
        environmental_factors = [
            "increased solar radiation",
            "global temperature rise",
            "changes in Earth's magnetic field",
            "atmospheric composition alterations"
        ]
        tasks = [
            {
                "quantum_phenomenon": phenomenon,
                "environmental_factor": factor
            }
            for phenomenon in quantum_phenomena
            for factor in environmental_factors
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational simulation that models the evolution of {t['quantum_phenomenon']} in a population over multiple generations, considering the environmental factor of {t['environmental_factor']}. Your response should include:

1. Simulation Design (250-300 words):
   a) Describe the key components of your simulation, including how you model the quantum biological phenomenon and its inheritance.
   b) Explain how you incorporate evolutionary mechanisms (e.g., mutation, selection, drift) into your model.
   c) Detail how you represent and simulate the effects of the given environmental factor.

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your simulation bridges quantum and classical aspects of biology.
   b) Discuss any novel approaches to modeling quantum effects in a biological context.
   c) Address potential challenges in accurately representing quantum phenomena in an evolutionary simulation.

3. Simulation Results and Analysis (250-300 words):
   a) Describe a hypothetical run of your simulation, including initial conditions and key parameters.
   b) Present the results of this run, focusing on how the quantum biological phenomenon evolves over generations.
   c) Analyze how the environmental factor influences the evolutionary trajectory of the quantum phenomenon.

4. Implications for Evolutionary Theory (200-250 words):
   a) Discuss how your simulation results might impact our understanding of evolutionary processes.
   b) Speculate on potential long-term evolutionary consequences of quantum biological phenomena.
   c) Propose a testable hypothesis based on your simulation results.

5. Future Research Directions (150-200 words):
   a) Suggest two potential expansions or modifications to your simulation to explore additional aspects of quantum evolutionary biology.
   b) Discuss how empirical research could validate or challenge your simulation's predictions.

6. Ethical Considerations and Societal Impact (100-150 words):
   a) Identify potential ethical implications of research into quantum evolutionary biology.
   b) Discuss possible societal impacts of a deeper understanding of quantum effects in biological evolution.

Ensure your response demonstrates a deep understanding of both quantum mechanics and evolutionary biology. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and evolutionary biology.",
            "The simulation design effectively incorporates the specified quantum biological phenomenon and environmental factor.",
            "The analysis of simulation results is thorough and insightful, with clear connections to evolutionary theory.",
            "The response includes creative and plausible speculations about the implications of quantum effects in biological evolution.",
            "The proposed future research directions and ethical considerations are thoughtful and relevant.",
            "The overall response is well-structured, scientifically sound, and demonstrates interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
