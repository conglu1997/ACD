import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "dilemma": "Resource Allocation",
                "ethical_framework": "Utilitarianism",
                "game_theory_concept": "Nash Equilibrium"
            },
            {
                "dilemma": "Environmental Conservation",
                "ethical_framework": "Deontological Ethics",
                "game_theory_concept": "Prisoner's Dilemma"
            },
            {
                "dilemma": "Technological Regulation",
                "ethical_framework": "Virtue Ethics",
                "game_theory_concept": "Stag Hunt"
            },
            {
                "dilemma": "Healthcare Access",
                "ethical_framework": "Care Ethics",
                "game_theory_concept": "Tragedy of the Commons"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a social dilemma game that incorporates elements of game theory and ethical decision-making, focusing on the dilemma of {t['dilemma']}, using the ethical framework of {t['ethical_framework']}, and applying the game theory concept of {t['game_theory_concept']}. Then, propose and evaluate potential solutions to the dilemma. Your response should include:

1. Game Design (300-350 words):
   a) Describe the social dilemma game, including its setup, players, and possible actions.
   b) Explain how the game incorporates the specified ethical framework.
   c) Detail how the game theory concept is applied in the game structure.
   d) Discuss the potential outcomes and their implications for the players and society.

2. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of different strategies in the game.
   b) Discuss how the chosen ethical framework informs decision-making in this context.
   c) Identify any conflicts between individual and collective interests.
   d) Consider potential unintended consequences of different choices.

3. Game Theory Analysis (250-300 words):
   a) Apply the specified game theory concept to analyze player strategies.
   b) Identify any equilibria or optimal strategies in the game.
   c) Discuss how game theory insights inform our understanding of the dilemma.
   d) Explain any limitations of the game theory approach in this context.

4. Solution Proposal (200-250 words):
   a) Propose two potential solutions to address the dilemma.
   b) Explain how each solution attempts to balance ethical considerations and game theory insights.
   c) Discuss the potential effectiveness and feasibility of each solution.

5. Evaluation and Implications (200-250 words):
   a) Evaluate the proposed solutions in terms of their ethical and practical implications.
   b) Discuss potential challenges or obstacles in implementing these solutions.
   c) Consider how different stakeholders might respond to the proposed solutions.
   d) Reflect on broader implications for policy-making and social institutions.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how this analysis connects to at least two other academic disciplines.
   b) Discuss how insights from these disciplines might further inform our understanding of the dilemma.
   c) Propose a research question that could be explored through interdisciplinary collaboration.

Ensure your response demonstrates a deep understanding of ethical reasoning, game theory, and social psychology. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining logical consistency and real-world applicability.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should thoroughly address the dilemma of {t['dilemma']} using the ethical framework of {t['ethical_framework']} and the game theory concept of {t['game_theory_concept']}",
            "The game design should be creative, logically consistent, and effectively incorporate both ethical and game theory elements",
            "The ethical and game theory analyses should demonstrate a deep understanding of the relevant concepts and their application to the dilemma",
            "The proposed solutions should be innovative, well-reasoned, and address both ethical considerations and game theory insights",
            "The evaluation should critically assess the proposed solutions and consider broader implications",
            "The response should demonstrate interdisciplinary thinking and propose meaningful connections to other academic fields",
            "The overall response should be well-structured, use appropriate terminology, and provide clear explanations for complex ideas"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
