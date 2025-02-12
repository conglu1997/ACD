import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Stock Market Crash",
                "cognitive_bias": "Loss Aversion",
                "game_theory_concept": "Nash Equilibrium"
            },
            {
                "scenario": "Climate Change Negotiations",
                "cognitive_bias": "Hyperbolic Discounting",
                "game_theory_concept": "Tragedy of the Commons"
            },
            {
                "scenario": "Vaccine Distribution",
                "cognitive_bias": "Availability Heuristic",
                "game_theory_concept": "Prisoner's Dilemma"
            },
            {
                "scenario": "Social Media Misinformation",
                "cognitive_bias": "Confirmation Bias",
                "game_theory_concept": "Information Cascades"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Design and analyze an AI system that combines principles from cognitive science and game theory to model and predict human decision-making in the scenario of {t['scenario']}. Your system should incorporate the cognitive bias of {t['cognitive_bias']} and the game theory concept of {t['game_theory_concept']}. Your response should include:\n\n"
            f"1. System Architecture (300-350 words):\n"
            f"   a) Describe the key components of your AI system and how they interact.\n"
            f"   b) Explain how your system incorporates {t['cognitive_bias']} and {t['game_theory_concept']}.\n"
            f"   c) Detail the data inputs and outputs of your system.\n"
            f"   d) Discuss how your system handles uncertainty and incomplete information.\n\n"
            f"2. Cognitive Modeling (250-300 words):\n"
            f"   a) Explain how your system models human cognitive processes related to {t['cognitive_bias']}.\n"
            f"   b) Describe how this modeling influences the decision-making predictions.\n"
            f"   c) Discuss any novel approaches you've used to integrate cognitive biases into a computational model.\n\n"
            f"3. Game-Theoretic Analysis (250-300 words):\n"
            f"   a) Describe how your system applies {t['game_theory_concept']} to the {t['scenario']} scenario.\n"
            f"   b) Explain how the game-theoretic elements interact with the cognitive modeling components.\n"
            f"   c) Discuss any challenges in applying game theory to real-world, complex scenarios and how your system addresses them.\n\n"
            f"4. Prediction and Decision Support (200-250 words):\n"
            f"   a) Explain how your system generates predictions or decision recommendations.\n"
            f"   b) Describe a specific example of how your system would analyze a situation in the {t['scenario']} scenario.\n"
            f"   c) Discuss the potential accuracy and limitations of your system's predictions.\n\n"
            f"5. Ethical Considerations and Societal Impact (200-250 words):\n"
            f"   a) Discuss potential ethical implications of using your system for decision-making in the {t['scenario']} scenario.\n"
            f"   b) Analyze potential positive and negative societal impacts of widespread adoption of such systems.\n"
            f"   c) Propose safeguards or guidelines for responsible use of your system.\n\n"
            f"6. Future Research and Development (150-200 words):\n"
            f"   a) Suggest at least two potential improvements or extensions to your system.\n"
            f"   b) Propose a research agenda for advancing the integration of cognitive science and game theory in AI systems.\n\n"
            f"Ensure your response demonstrates a deep understanding of cognitive science, game theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\n"
            f"Format your answer with clear headings for each section. Your total response should be between 1350-1650 words."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively incorporates {t['cognitive_bias']} and {t['game_theory_concept']}.",
            "The cognitive modeling approach is well-explained and scientifically plausible.",
            f"The application of {t['game_theory_concept']} to the {t['scenario']} scenario is clear and appropriate.",
            "The prediction and decision support capabilities are logically described with a concrete example.",
            "Ethical considerations and societal impacts are thoughtfully discussed.",
            "Future research directions are innovative and relevant.",
            "The response demonstrates a deep understanding of cognitive science, game theory, and artificial intelligence.",
            "The proposed system is innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
