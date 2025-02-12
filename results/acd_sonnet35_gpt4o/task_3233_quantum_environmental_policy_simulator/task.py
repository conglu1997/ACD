import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Ocean acidification",
                "region": "Great Barrier Reef",
                "time_frame": "50 years"
            },
            {
                "challenge": "Deforestation",
                "region": "Amazon Rainforest",
                "time_frame": "30 years"
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that models complex environmental systems and simulates the impact of policy decisions. Then, use your system to propose solutions for {t['challenge']} in the {t['region']} over the next {t['time_frame']}. Your response should include:

1. Quantum Environmental Modeling System (300-350 words):
   a) Describe the key components of your quantum-based environmental modeling system.
   b) Explain how you leverage quantum principles (e.g., superposition, entanglement) to model complex environmental interactions.
   c) Detail how your system integrates various environmental factors (e.g., climate patterns, biodiversity, human activities).
   d) Provide a high-level diagram or pseudocode illustrating your system's architecture.

2. Quantum-Classical Interface for Policy Simulation (250-300 words):
   a) Explain how your system translates policy decisions into parameters for quantum simulation.
   b) Describe how simulation results are interpreted and translated back into actionable policy insights.
   c) Discuss any novel quantum algorithms you've developed for environmental system simulation.
   d) Address how your system handles uncertainty and probabilistic outcomes in policy simulations.

3. Application to Environmental Challenge (300-350 words):
   a) Apply your quantum environmental policy simulator to the given challenge and region.
   b) Describe the key environmental factors and policy levers your simulation considers.
   c) Present at least three policy scenarios your system simulated, including their projected outcomes.
   d) Propose a comprehensive policy solution based on your simulation results, explaining the rationale behind your recommendations.

4. Comparative Analysis (200-250 words):
   a) Compare the capabilities of your quantum-based system to traditional environmental modeling techniques.
   b) Discuss the advantages and potential limitations of using quantum computing in this context.
   c) Analyze how your system's projections might differ from current scientific consensus on the given environmental challenge.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Discuss ethical implications of using quantum simulations to inform environmental policy.
   b) Address potential issues of data privacy, algorithmic bias, and the digital divide in the context of your system.
   c) Propose guidelines for responsible development and use of quantum environmental policy simulators.
   d) Discuss how to ensure transparency and accountability in the policy-making process when using such advanced simulations.

6. Future Developments and Global Impact (200-250 words):
   a) Suggest potential improvements or extensions to your quantum environmental policy simulator.
   b) Discuss how this technology could be applied to other global environmental challenges.
   c) Explore the potential long-term impacts of using quantum computing in environmental science and policy-making.
   d) Propose a roadmap for integrating quantum environmental simulations into international policy frameworks.

Ensure your response demonstrates a deep understanding of quantum computing principles, environmental science, and policy-making processes. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles and their application to environmental modeling.",
            "The proposed system effectively integrates quantum computing with environmental science and policy-making processes.",
            "The application to the specific environmental challenge is thorough, innovative, and scientifically plausible.",
            "The comparative analysis shows a clear understanding of the advantages and limitations of quantum-based approaches.",
            "Ethical considerations and future developments are thoughtfully addressed.",
            "The overall response demonstrates high-level interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
