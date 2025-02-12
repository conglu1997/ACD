import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            "Bacterial quorum sensing",
            "Neuronal signaling in the human brain",
            "Plant root communication networks",
            "Insect swarm intelligence"
        ]
        artificial_systems = [
            "Distributed blockchain networks",
            "Federated learning systems",
            "Quantum neural networks",
            "Evolutionary algorithms in optimization"
        ]
        information_properties = [
            "Redundancy",
            "Compression efficiency",
            "Error correction capabilities",
            "Adaptability to noise"
        ]
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "artificial_system": random.choice(artificial_systems),
                "information_property": random.choice(information_properties)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "artificial_system": random.choice(artificial_systems),
                "information_property": random.choice(information_properties)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simulation system that models the evolution of information processing in biological and artificial systems, then use it to explore parallels and divergences in information evolution across these domains. This field of study, which we'll call "evolutionary infodynamics," combines principles from evolutionary biology and information theory to understand how information processing mechanisms evolve over time in different systems.

Focus on comparing {t['biological_system']} with {t['artificial_system']}, particularly in terms of {t['information_property']}. Your response should include:

1. Simulation Framework (300-350 words):
   a) Describe the key components and architecture of your simulation system.
   b) Explain how it models information evolution in both biological and artificial contexts.
   c) Detail how your system incorporates principles from evolutionary biology and information theory.
   d) Include a high-level diagram or pseudocode illustrating the simulation's core algorithm. (Describe this visually in words, as if explaining it to someone who cannot see the diagram.)

2. System-Specific Modeling (250-300 words):
   a) Explain how your simulation models information processing in {t['biological_system']}.
   b) Describe how it represents and evolves information in {t['artificial_system']}.
   c) Discuss any novel approaches or algorithms used to capture the unique characteristics of each system.

3. Comparative Analysis (250-300 words):
   a) Analyze how {t['information_property']} evolves differently (or similarly) in the two systems.
   b) Identify key factors that drive these evolutionary differences or similarities.
   c) Discuss any emergent behaviors or unexpected patterns observed in the simulation.

4. Information Metrics (200-250 words):
   a) Propose quantitative metrics to measure {t['information_property']} in both systems.
   b) Explain how these metrics capture the essence of information evolution.
   c) Describe how your simulation calculates and compares these metrics over time.
   d) Include at least one mathematical formula or equation that represents a key metric or process in your simulation.

5. Theoretical Implications (200-250 words):
   a) Discuss what your simulation reveals about the nature of information processing in biological vs. artificial systems.
   b) Explore potential implications for our understanding of natural and artificial evolution.
   c) Propose a novel hypothesis about information evolution based on your simulation results.

6. Practical Applications (150-200 words):
   a) Suggest potential real-world applications of insights gained from your simulation.
   b) Discuss how these findings might inform the design of new AI systems or biological experiments.

7. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your simulation approach.
   b) Propose methods to validate your simulation results against real-world data.
   c) Suggest two directions for future research to expand or improve your evolutionary infodynamics model.

Ensure your response demonstrates a deep understanding of evolutionary biology, information theory, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the comparison between {t['biological_system']} and {t['artificial_system']}, focusing on {t['information_property']}.",
            "The simulation framework is well-designed and clearly explained, demonstrating a deep understanding of evolutionary biology and information theory.",
            "The comparative analysis is insightful and reveals meaningful patterns or differences in information evolution across the two systems.",
            "The proposed information metrics are relevant and well-justified for measuring the specified information property, including at least one mathematical formula or equation.",
            "The theoretical implications and novel hypothesis are thought-provoking and well-reasoned.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
