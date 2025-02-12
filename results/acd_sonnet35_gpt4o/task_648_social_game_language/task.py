import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Corporate Negotiation",
                "context": "A high-stakes business deal between two rival companies with a 48-hour deadline",
                "players": ["CEO", "CFO", "Legal Counsel"],
                "objectives": ["Maximize profit", "Minimize risk", "Protect intellectual property"],
                "time_constraint": "48 hours",
                "existing_model": "Prisoner's Dilemma"
            },
            {
                "name": "International Diplomacy",
                "context": "A multilateral peace negotiation between three countries with diverse cultural backgrounds, concluding in one week",
                "players": ["Diplomat A", "Diplomat B", "Diplomat C"],
                "objectives": ["Secure resources", "Maintain sovereignty", "Forge alliances"],
                "time_constraint": "One week",
                "existing_model": "Nash Equilibrium"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a language game that models complex social interactions in the context of {t['name']}. Your task has the following components:\n\n1. Game Design (350-400 words):\n   a) Create a set of at least 5 unique linguistic rules and elements that represent social actions, intentions, and outcomes.\n   b) Explain how your game incorporates at least 3 principles from game theory and 3 from social psychology.\n   c) Describe how players use language constructs to make moves and influence the game state.\n   d) Provide examples of basic 'moves' or 'utterances' in your game and their effects.\n   e) Explain how the time constraint of {t['time_constraint']} is incorporated into the game mechanics.\n   f) Provide a visual representation or diagram of your game design (use ASCII art or Unicode characters).\n   g) Briefly contrast your game with the {t['existing_model']} model, highlighting key differences and similarities.\n\n2. Scenario Analysis (300-350 words):\n   a) Apply your language game to the given scenario: {t['context']}\n   b) Describe how each player ({', '.join(t['players'])}) would use the game language to pursue their objectives ({', '.join(t['objectives'])}).\n   c) Provide a short example 'dialogue' or sequence of moves using your game language.\n   d) Analyze potential conflicts or synergies between different players' objectives and how these might be expressed through the game language.\n   e) If applicable, discuss how cultural differences might influence the players' strategies and communication styles.\n   f) Explain how the game might evolve over multiple rounds or iterations.\n\n3. Outcome Prediction (250-300 words):\n   a) Based on your game rules, predict possible outcomes of the scenario.\n   b) Explain how different linguistic strategies might lead to various results.\n   c) Discuss any emergent behaviors or unexpected consequences that might arise.\n   d) Analyze how the time constraint affects the potential outcomes.\n   e) Consider long-term implications of the game outcomes beyond the immediate scenario.\n\n4. Linguistic and Psychological Analysis (300-350 words):\n   a) Analyze how your game language reflects or distorts real-world social interactions.\n   b) Discuss the psychological principles at play in your game design.\n   c) Explain how your game might provide insights into human communication and decision-making.\n   d) Address potential biases in your language game design and how they might affect the outcomes.\n   e) Discuss how your game might be used to study or model specific linguistic or psychological phenomena.\n\n5. Limitations and Ethical Considerations (200-250 words):\n   a) Identify and discuss potential limitations or weaknesses of your game design.\n   b) Discuss potential ethical implications of modeling social interactions as a language game.\n   c) Address concerns about privacy, manipulation, or misuse of such a system.\n   d) Consider the ethical implications of using this game in real-world negotiations or conflict resolution.\n\n6. Extensions and Applications (200-250 words):\n   a) Propose how your language game could be extended or applied in fields such as AI, education, or conflict resolution.\n   b) Suggest a research question that could be explored using your game system.\n   c) Discuss potential real-world applications of your game, considering both benefits and risks.\n   d) Propose a method for empirically testing the validity and effectiveness of your game in modeling real-world social interactions.\n\nEnsure your response demonstrates a deep understanding of linguistics, game theory, social psychology, and cultural factors. Be creative in your game design while maintaining logical consistency and real-world applicability. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, game theory, social psychology, and cultural factors.",
            "The language game design is creative, logically consistent, and incorporates at least 5 unique linguistic elements and 6 principles from game theory and social psychology.",
            "The game design includes a clear visual representation and a thoughtful comparison with the specified existing model.",
            "The scenario analysis and outcome prediction show a nuanced understanding of complex social dynamics, including potential conflicts and synergies between players' objectives, and consider the impact of time constraints, cultural differences (if applicable), and long-term evolution of the game.",
            "The linguistic and psychological analysis provides insightful connections between the game and real-world interactions, addresses potential biases in the game design, and suggests applications for studying specific phenomena.",
            "Limitations of the game design are critically discussed, and ethical considerations are thoughtfully addressed, showing awareness of potential implications in various contexts.",
            "The proposed extensions and applications are innovative, demonstrate interdisciplinary thinking, consider both benefits and risks of real-world implementation, and include a method for empirical validation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
