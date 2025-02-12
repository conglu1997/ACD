class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ecosystem": "Coral reef",
                "climate_scenario": "Ocean acidification and temperature increase"
            },
            "2": {
                "ecosystem": "Arctic tundra",
                "climate_scenario": "Permafrost thaw and vegetation shifts"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and optimize complex ecological interactions in a {t['ecosystem']} ecosystem under the climate change scenario of {t['climate_scenario']}. Your response should include:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum ecosystem simulator.
   b) Explain how quantum principles (e.g., superposition, entanglement) are utilized in your system.
   c) Detail how your system integrates ecological models with quantum algorithms.
   d) Discuss any novel quantum techniques developed for ecosystem simulation.

2. Ecosystem Modeling (250-300 words):
   a) Outline the key ecological interactions and processes your system models.
   b) Explain how your system accounts for the complexity and non-linearity of ecosystem dynamics.
   c) Describe how climate change factors are incorporated into the simulation.

3. Quantum-Ecological Integration (250-300 words):
   a) Explain how specific quantum algorithms enhance ecosystem modeling capabilities.
   b) Discuss how quantum computing addresses limitations of classical ecological simulations.
   c) Provide an example of how a particular ecological process is mapped to a quantum operation.

4. Simulation Results and Analysis (200-250 words):
   a) Present a hypothetical simulation output for the given ecosystem and climate scenario.
   b) Analyze the potential impacts on biodiversity, ecosystem services, and resilience.
   c) Discuss any unexpected or emergent behaviors revealed by the quantum simulation.

5. Optimization and Intervention Strategies (200-250 words):
   a) Explain how your system can be used to optimize conservation strategies.
   b) Propose specific interventions based on your simulation results.
   c) Discuss the potential advantages of quantum-informed ecological management.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of using quantum simulations for ecosystem management.
   b) Address potential risks of relying on quantum models for environmental decision-making.
   c) Acknowledge limitations of your system and areas for future improvement.

Ensure your response demonstrates a deep understanding of quantum computing principles, ecological systems, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all six required sections comprehensively.",
            "The quantum ecosystem simulator design is innovative, plausible, and well-explained.",
            "The integration of quantum computing principles with ecological modeling is logically sound and creative.",
            "The response demonstrates a deep understanding of quantum computing, ecology, and climate science.",
            "The proposed system effectively simulates and analyzes the given ecosystem under the specified climate change scenario.",
            "The response shows creativity in addressing complex ecological challenges while maintaining scientific rigor.",
            "The submission includes appropriate technical terminology with clear explanations for complex concepts.",
            "The response falls within the specified word count range (1350-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
