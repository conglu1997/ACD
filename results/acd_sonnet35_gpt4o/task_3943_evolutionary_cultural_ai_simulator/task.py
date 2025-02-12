import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_traits = ['lactose tolerance', 'skin pigmentation', 'height', 'disease resistance']
        cultural_norms = ['food taboos', 'marriage customs', 'gender roles', 'religious practices']
        environmental_factors = ['climate change', 'resource availability', 'population density', 'technological advancements']
        simulation_goals = ['predict future societal changes', 'understand historical developments', 'explore counterfactual scenarios', 'optimize societal resilience']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "biological_trait": random.choice(biological_traits),
                "cultural_norm": random.choice(cultural_norms),
                "environmental_factor": random.choice(environmental_factors),
                "simulation_goal": random.choice(simulation_goals)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the co-evolution of biological traits and cultural norms in human societies, focusing on the biological trait of {t['biological_trait']} and the cultural norm of {t['cultural_norm']}. Your system should account for the environmental factor of {t['environmental_factor']} and aim to {t['simulation_goal']}. Provide a comprehensive response addressing the following points:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating bio-cultural co-evolution.
   b) Explain how your system integrates principles from evolutionary biology, cultural anthropology, and artificial intelligence.
   c) Detail how your system models the specified biological trait and cultural norm.
   d) Discuss how the chosen environmental factor is incorporated into your simulation.

2. Evolutionary Algorithms and Cultural Transmission Models (250-300 words):
   a) Describe the evolutionary algorithms used to simulate biological trait changes.
   b) Explain your approach to modeling cultural transmission and norm evolution.
   c) Discuss how your system handles the interaction between genetic and cultural evolution.
   d) Provide a mathematical formulation or pseudocode for a key algorithm in your system.

3. Data Integration and Analysis (200-250 words):
   a) Describe the types of data your system would use for initialization and validation.
   b) Explain how your system integrates data from various sources (e.g., genetic studies, anthropological research, historical records).
   c) Discuss any novel data analysis techniques your system employs to understand bio-cultural dynamics.

4. Simulation Scenarios and Predictions (250-300 words):
   a) Describe a specific simulation scenario focusing on the given biological trait and cultural norm.
   b) Explain how your system generates predictions or insights related to the specified simulation goal.
   c) Discuss how your system handles uncertainty and variability in evolutionary and cultural processes.
   d) Provide an example output or visualization that your system might generate.

5. Validation and Calibration (200-250 words):
   a) Propose methods for validating your simulation against real-world data or known historical trends.
   b) Describe how you would calibrate your model to ensure realistic bio-cultural dynamics.
   c) Discuss the challenges in validating such complex, long-term simulations and how your system addresses them.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues related to simulating human biological and cultural evolution.
   b) Discuss how your system addresses concerns about determinism, reductionism, or potential misuse of results.
   c) Propose guidelines for the responsible development and use of bio-cultural evolution simulations.

7. Future Directions and Broader Impact (100-150 words):
   a) Suggest two potential extensions or improvements to your evolutionary cultural AI simulator.
   b) Discuss how your approach could be applied to other complex adaptive systems or societal challenges.
   c) Reflect on the potential long-term impacts of such simulations on our understanding of human nature and society.

Ensure your response demonstrates a deep understanding of evolutionary biology, cultural anthropology, and artificial intelligence. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, cultural anthropology, and artificial intelligence.",
            "The system architecture effectively integrates principles from multiple disciplines and addresses the specified biological trait and cultural norm.",
            "The evolutionary algorithms and cultural transmission models are well-designed and scientifically plausible.",
            "The data integration and analysis approach is comprehensive and innovative.",
            "The simulation scenarios and predictions are well-developed and relevant to the specified goal.",
            "The validation and calibration methods are appropriate and address the challenges of complex bio-cultural simulations.",
            "Ethical considerations and societal impact are thoroughly addressed.",
            "Future directions and broader impact are insightful and well-reasoned.",
            "The response is creative and demonstrates effective interdisciplinary knowledge integration.",
            "The response follows the required format and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
