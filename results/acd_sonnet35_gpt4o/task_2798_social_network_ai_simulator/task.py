import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        network_types = [
            "Small-world network",
            "Scale-free network",
            "Random network",
            "Hierarchical network"
        ]
        social_phenomena = [
            "Information cascades",
            "Echo chambers",
            "Social contagion",
            "Collective behavior",
            "Group polarization"
        ]
        return {
            "1": {
                "network_type": random.choice(network_types),
                "social_phenomenon": random.choice(social_phenomena)
            },
            "2": {
                "network_type": random.choice(network_types),
                "social_phenomenon": random.choice(social_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes complex social networks, focusing on a {t['network_type']} and the social phenomenon of {t['social_phenomenon']}. Your system should be capable of predicting emergent behaviors and potential societal impacts. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain key concepts from network theory relevant to {t['network_type']}.
   b) Describe the social psychological principles underlying {t['social_phenomenon']}.
   c) Discuss how these theories interact in the context of social network dynamics.

2. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system models and simulates a {t['network_type']}.
   c) Detail how your system incorporates social psychological principles to simulate {t['social_phenomenon']}.
   d) Provide a visual representation of your system architecture (describe it textually).

3. Simulation Process (250-300 words):
   a) Outline the steps your system takes to simulate network evolution and emergent behaviors.
   b) Explain how your system handles the interplay between individual agent behaviors and network-level phenomena.
   c) Describe any novel algorithms or approaches used in your simulation.
   d) Include a pseudocode snippet (5-10 lines) illustrating a key algorithm in your simulation process.

4. Analysis and Prediction (200-250 words):
   a) Describe the metrics and methods your system uses to analyze the simulated network.
   b) Explain how your system predicts emergent behaviors related to {t['social_phenomenon']}.
   c) Discuss how your system evaluates potential societal impacts of the observed network dynamics.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues related to simulating and predicting human social behavior.
   b) Address limitations of your approach in capturing the complexity of real-world social networks.
   c) Propose guidelines for the responsible development and use of AI systems that model social dynamics.
   d) Suggest potential applications and future research directions for your system.

Ensure your response demonstrates a deep understanding of network theory, social psychology, complex systems modeling, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the {t['network_type']} and the social phenomenon of {t['social_phenomenon']}.",
            "The theoretical framework demonstrates a deep understanding of network theory and social psychology.",
            "The AI system architecture is well-designed and clearly explained, showing innovation in integrating network theory and social psychology.",
            "The simulation process is logically described and includes a relevant pseudocode snippet.",
            "The analysis and prediction methods are well-thought-out and appropriate for the given network type and social phenomenon.",
            "Ethical considerations are thoroughly discussed, and limitations are honestly addressed.",
            "The response shows interdisciplinary knowledge integration and creative problem-solving in the context of social network simulation and analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
