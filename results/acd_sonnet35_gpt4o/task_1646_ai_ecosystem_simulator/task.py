class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "biome": "Coral reef ecosystem",
                "environmental_challenge": "Rapid ocean acidification",
                "emerging_phenomenon": "Symbiotic evolution",
                "key_species": ["Acropora coral", "Clownfish", "Zooxanthellae algae"],
                "environmental_factors": ["Temperature", "pH", "Dissolved oxygen", "Light intensity"]
            },
            "2": {
                "biome": "Temperate forest ecosystem",
                "environmental_challenge": "Extreme temperature fluctuations",
                "emerging_phenomenon": "Adaptive migration patterns",
                "key_species": ["Oak trees", "Red-tailed hawks", "White-tailed deer"],
                "environmental_factors": ["Temperature", "Precipitation", "Soil moisture", "Day length"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered ecosystem simulator for a {t['biome']} that models complex interactions between species, environmental factors, and emerging phenomena. Then, use your simulator to predict and analyze ecosystem responses to the environmental challenge of {t['environmental_challenge']}, with a focus on the emerging phenomenon of {t['emerging_phenomenon']}. Your response should include:

1. Ecosystem Model Design (250-300 words):
   a) Describe the key components and interactions in your {t['biome']} simulator, focusing on the key species: {', '.join(t['key_species'])}.
   b) Explain how your model incorporates species interactions, environmental factors ({', '.join(t['environmental_factors'])}), and feedback loops.
   c) Discuss how you've integrated the potential for {t['emerging_phenomenon']} into your model.
   d) Include a diagram or flowchart representing the main components and interactions in your ecosystem model (describe it textually).

2. AI Algorithm Implementation (200-250 words):
   a) Describe the specific AI algorithms or techniques used in your ecosystem simulator (e.g., neural networks, genetic algorithms, reinforcement learning).
   b) Explain how these algorithms model complex ecological processes and emergent behaviors.
   c) Provide pseudocode for a key function in your AI implementation that handles a critical aspect of the simulation.
   d) Discuss any novel approaches you've developed to handle the unique challenges of simulating a {t['biome']}.

3. Simulation of Environmental Challenge (250-300 words):
   a) Detail how you would use your simulator to model the effects of {t['environmental_challenge']}.
   b) Describe the key parameters and variables you would monitor during the simulation.
   c) Explain how your simulator captures the potential for {t['emerging_phenomenon']} in response to this challenge.
   d) Present a hypothetical dataset showing the changes in key variables over time during the simulation (provide this as a textual description of a graph or table).

4. Results Analysis and Interpretation (200-250 words):
   a) Present and interpret the simulated ecosystem's response to {t['environmental_challenge']}.
   b) Analyze how {t['emerging_phenomenon']} manifests in your simulation results.
   c) Discuss any surprising or counterintuitive outcomes from your simulation.
   d) Provide a quantitative assessment of the impact on at least two key species in your ecosystem.

5. Validation and Limitations (150-200 words):
   a) Propose specific methods to validate your simulator's predictions against real-world data.
   b) Discuss the limitations of your model and potential sources of error or uncertainty.
   c) Suggest improvements or extensions to enhance the simulator's accuracy and capabilities.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your simulation results for real-world ecosystem management.
   b) Propose two novel applications of your AI ecosystem simulator beyond ecological research.
   c) Speculate on how this type of simulation might influence environmental policy-making.

Ensure your response demonstrates a deep understanding of ecology, complex systems theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, and number your paragraphs within each section. Include any graphs, tables, or pseudocode as textual descriptions. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts and includes numbered paragraphs within each section.",
            "The ecosystem model design demonstrates a deep understanding of ecological principles and complex systems, incorporating all specified key species and environmental factors.",
            "The AI algorithm implementation includes specific AI techniques and pseudocode for a key function.",
            "The simulation of the environmental challenge includes a hypothetical dataset showing changes in key variables over time.",
            "The results analysis provides a quantitative assessment of the impact on at least two key species.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The implications and applications discussed are thoughtful and demonstrate an understanding of broader environmental issues."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
