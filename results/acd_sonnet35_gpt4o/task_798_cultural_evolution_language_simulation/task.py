import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "society_name": "Zephyria",
                "initial_language": "Zephyrian",
                "cultural_traits": ["nomadic", "oral tradition", "nature worship"],
                "external_influences": ["technological advancements", "climate change"],
                "simulation_duration": "500 years"
            },
            {
                "society_name": "Novaterra",
                "initial_language": "Novan",
                "cultural_traits": ["space colonization", "AI integration", "resource scarcity"],
                "external_influences": ["alien contact", "interstellar travel"],
                "simulation_duration": "1000 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system for modeling and simulating cultural evolution through language, then use it to predict linguistic and cultural changes in the hypothetical society of {t['society_name']} over {t['simulation_duration']}. Your task has the following components:\n\n1. Simulation System Design (300-350 words):\n   a) Describe the key components of your cultural evolution simulation system.\n   b) Explain how your system models the relationship between language and culture.\n   c) Detail how your system incorporates factors such as population dynamics, social networks, and external influences.\n   d) Describe the mathematical or computational framework used (e.g., agent-based modeling, dynamic systems).\n   e) Explain how your system handles the temporal aspect of cultural and linguistic change.\n\n2. Initial Conditions (200-250 words):\n   a) Describe the initial state of {t['society_name']}, including its language ({t['initial_language']}) and cultural traits ({', '.join(t['cultural_traits'])}).\n   b) Explain how these initial conditions are represented in your simulation system.\n   c) Discuss any assumptions or simplifications you've made in modeling this society.\n\n3. Simulation Process (250-300 words):\n   a) Provide a step-by-step explanation of how your simulation runs.\n   b) Describe how linguistic features (e.g., lexicon, syntax, phonology) evolve in your model.\n   c) Explain how cultural traits change and interact with linguistic evolution.\n   d) Discuss how external influences ({', '.join(t['external_influences'])}) are incorporated into the simulation.\n\n4. Predicted Outcomes (300-350 words):\n   a) Describe the predicted state of {t['society_name']}'s language and culture after {t['simulation_duration']}.\n   b) Highlight major linguistic changes (e.g., new dialects, lost or gained features).\n   c) Discuss significant cultural shifts and their relationship to language changes.\n   d) Explain any unexpected or emergent phenomena observed in your simulation.\n\n5. Analysis and Implications (250-300 words):\n   a) Analyze the factors that had the most significant impact on the simulated cultural and linguistic evolution.\n   b) Discuss the theoretical implications of your simulation results for understanding real-world cultural and linguistic change.\n   c) Compare your simulation's predictions with known historical patterns of language and cultural evolution.\n   d) Identify potential applications of your simulation system in fields such as historical linguistics, anthropology, or future studies.\n\n6. Limitations and Future Work (200-250 words):\n   a) Discuss the limitations of your simulation system and how they might affect the results.\n   b) Propose ways to validate or test the accuracy of your simulation against real-world data.\n   c) Suggest improvements or extensions to your system for future research.\n\nEnsure your response demonstrates a deep understanding of linguistic principles, cultural evolution theories, and complex systems modeling. Be creative in your approach while maintaining scientific plausibility and logical consistency. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic principles, cultural evolution theories, and complex systems modeling.",
            "The simulation system design is comprehensive, incorporating key factors such as population dynamics, social networks, and external influences.",
            "The initial conditions are well-described and appropriately represented in the simulation system.",
            "The simulation process is clearly explained, showing how linguistic features and cultural traits evolve over time.",
            "The predicted outcomes are detailed and logically follow from the initial conditions and simulation process.",
            "The analysis demonstrates insightful understanding of the factors influencing cultural and linguistic evolution.",
            "The limitations of the simulation are critically discussed, and proposed improvements are thoughtful and relevant.",
            "The response shows creativity and originality in approach while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
