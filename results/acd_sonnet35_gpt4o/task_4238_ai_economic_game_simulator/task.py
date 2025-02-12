import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        economic_scenarios = [
            "Trade war between major economies",
            "Global pandemic economic recovery",
            "Transition to renewable energy sources",
            "Implementation of universal basic income"
        ]
        game_theory_concepts = [
            "Nash equilibrium",
            "Prisoner's dilemma",
            "Evolutionary game theory",
            "Cooperative game theory"
        ]
        ai_techniques = [
            "Reinforcement learning",
            "Multi-agent systems",
            "Bayesian networks",
            "Genetic algorithms"
        ]
        return {
            "1": {
                "scenario": random.choice(economic_scenarios),
                "game_theory_concept": random.choice(game_theory_concepts),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "scenario": random.choice(economic_scenarios),
                "game_theory_concept": random.choice(game_theory_concepts),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates complex economic scenarios using game theory principles, and use it to analyze and predict outcomes of global economic policies. Your system should focus on the scenario of {t['scenario']}, incorporate the game theory concept of {t['game_theory_concept']}, and utilize the AI technique of {t['ai_technique']}. Provide your response in the following format:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI economic simulation system.\n   b) Explain how your system incorporates the specified game theory concept and AI technique.\n   c) Detail how these components work together to model and analyze the given economic scenario.\n   d) Include a high-level diagram or pseudocode snippet illustrating a key aspect of your system.\n\n2. Economic Modeling (250-300 words):\n   a) Explain how your system models the complex economic scenario.\n   b) Describe the key variables, actors, and interactions in your model.\n   c) Discuss how your model accounts for uncertainty and dynamic changes in the economic environment.\n\n3. Game Theory Integration (250-300 words):\n   a) Describe how the specified game theory concept is implemented in your system.\n   b) Explain how this concept enhances the analysis of the economic scenario.\n   c) Provide an example of how your system would use this concept to predict economic outcomes.\n\n4. AI Implementation (250-300 words):\n   a) Detail how you implement the specified AI technique in your system.\n   b) Explain how this AI technique improves the simulation and analysis capabilities.\n   c) Discuss any novel approaches or adaptations of the AI technique for this specific application.\n\n5. Policy Analysis and Prediction (200-250 words):\n   a) Describe how your system would analyze the effects of different economic policies in the given scenario.\n   b) Explain the process of generating and evaluating policy recommendations.\n   c) Discuss how your system accounts for potential unintended consequences of policies.\n\n6. Validation and Limitations (150-200 words):\n   a) Propose methods to validate your system's predictions against real-world economic data.\n   b) Discuss the limitations of your approach and potential areas for improvement.\n   c) Address potential biases in your system and how they might be mitigated.\n\n7. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues in using AI to simulate and predict economic outcomes.\n   b) Discuss the implications of using such a system for policy-making.\n   c) Propose guidelines for the responsible development and use of AI in economic modeling.\n\nEnsure your response demonstrates a deep understanding of economics, game theory, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1550-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of economics, game theory, and artificial intelligence.",
            "The system design effectively integrates the specified game theory concept and AI technique.",
            "The economic modeling approach is comprehensive and accounts for complexity and uncertainty.",
            "The policy analysis and prediction process is well-reasoned and considers potential consequences.",
            "The discussion of validation, limitations, and ethical considerations shows critical thinking and awareness of real-world implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
