import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystem_types = [
            {
                "type": "Coral Reef",
                "info_challenge": "Signal Degradation",
                "evolutionary_pressure": "Ocean Acidification"
            },
            {
                "type": "Rainforest Canopy",
                "info_challenge": "Noise Interference",
                "evolutionary_pressure": "Deforestation"
            },
            {
                "type": "Urban Microbiome",
                "info_challenge": "Information Overload",
                "evolutionary_pressure": "Antibiotic Resistance"
            },
            {
                "type": "Deep Sea Hydrothermal Vent",
                "info_challenge": "Limited Bandwidth",
                "evolutionary_pressure": "Extreme Temperature Fluctuations"
            }
        ]
        selected_tasks = random.sample(ecosystem_types, 2)
        return {"1": selected_tasks[0], "2": selected_tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated ecosystem based on information theory principles, focusing on a {t['type']} environment. Your simulation should incorporate the information challenge of {t['info_challenge']} and the evolutionary pressure of {t['evolutionary_pressure']}. Your response should include the following sections:

1. Ecosystem Model Design (300-350 words):
   a) Describe the key components and species in your {t['type']} ecosystem simulation.
   b) Explain how you incorporate information theory principles into your model, particularly addressing the challenge of {t['info_challenge']}.
   c) Detail how your model represents and simulates the evolutionary pressure of {t['evolutionary_pressure']}.
   d) Discuss any novel algorithms or data structures you've developed for this simulation.
   e) Include a simple diagram or flowchart of your ecosystem model (describe it textually).

2. Information Dynamics Analysis (250-300 words):
   a) Analyze how information flows through your simulated ecosystem.
   b) Explain how different species or components in your model encode, transmit, and interpret information.
   c) Discuss how the challenge of {t['info_challenge']} affects these information dynamics.
   d) Propose a quantitative metric to measure information transfer efficiency in your ecosystem.

3. Evolutionary Algorithms and Adaptation (250-300 words):
   a) Describe the evolutionary algorithms used in your simulation.
   b) Explain how species in your model adapt to the pressure of {t['evolutionary_pressure']}.
   c) Discuss any emergent behaviors or unexpected adaptations you've observed in your simulations.
   d) Propose a novel mechanism for rapid information-based evolution in your ecosystem.

4. Simulation Results and Analysis (200-250 words):
   a) Present the results of running your ecosystem simulation over an extended period.
   b) Analyze any patterns, cycles, or equilibria that emerge in your simulated ecosystem.
   c) Discuss how the interplay between information dynamics and evolutionary pressures shapes these results.
   d) Compare your simulation results with real-world observations of {t['type']} ecosystems, noting similarities and differences.

5. Implications and Applications (150-200 words):
   a) Discuss the implications of your model for our understanding of real-world ecosystem dynamics.
   b) Propose a practical application of your simulation in ecosystem management or conservation.
   c) Suggest how your model could be extended to study other complex adaptive systems.

6. Limitations and Future Work (150-200 words):
   a) Acknowledge the limitations of your current ecosystem model.
   b) Propose three specific improvements or extensions to address these limitations.
   c) Suggest a novel research question that could be explored using an enhanced version of your model.

Ensure your response demonstrates a deep understanding of information theory, evolutionary biology, and complex systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the {t['type']} ecosystem and incorporate the information challenge of {t['info_challenge']} and the evolutionary pressure of {t['evolutionary_pressure']}",
            "The ecosystem model design should demonstrate a strong understanding of information theory principles and evolutionary biology",
            "The information dynamics analysis should be thorough and include a proposed quantitative metric",
            "The evolutionary algorithms and adaptation section should include a novel mechanism for rapid information-based evolution",
            "The simulation results and analysis should present and interpret data from running the ecosystem simulation",
            "The response should demonstrate interdisciplinary thinking by connecting concepts from information theory, evolutionary biology, and complex systems theory",
            "The proposed practical application and future research question should be innovative and scientifically plausible",
            "The response should be well-structured, following the given format with clear headings for each section",
            "The response should demonstrate a balance between technical accuracy and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
