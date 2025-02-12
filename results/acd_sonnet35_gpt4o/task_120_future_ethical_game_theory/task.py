import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "technology": "Mind-reading devices",
                "social_issue": "Privacy rights"
            },
            {
                "technology": "Genetic modification",
                "social_issue": "Socioeconomic inequality"
            },
            {
                "technology": "Artificial superintelligence",
                "social_issue": "Human agency and control"
            },
            {
                "technology": "Virtual reality immersion",
                "social_issue": "Reality perception and social cohesion"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a game theory scenario set in a future society where {t['technology']} is widespread, focusing on the social issue of {t['social_issue']}. Your task is to create a strategic interaction between multiple parties that explores the ethical implications and decision-making processes in this context.

Follow these steps:

1. Scenario Setup (3-4 sentences):
   Describe the futuristic setting, the relevant technology, and the key players involved in the game theory scenario.

2. Game Structure:
   a) Define the players and their objectives (1 sentence each)
   b) Outline the possible actions/strategies for each player (2-3 bullet points per player)
   c) Explain how the players' actions interact and influence outcomes (2-3 sentences)

3. Payoff Matrix:
   Create a simplified payoff matrix for the scenario, showing at least two possible strategies for each player and their corresponding outcomes. Explain the values in your matrix (2-3 sentences).

4. Ethical Analysis (4-5 sentences):
   Discuss the ethical implications of the various strategies and outcomes. Consider concepts such as utilitarianism, deontology, or virtue ethics in your analysis.

5. Nash Equilibrium (2-3 sentences):
   Identify and explain the Nash Equilibrium (or equilibria) in your scenario. Discuss whether this equilibrium is ethically optimal.

6. Societal Impact (3-4 sentences):
   Analyze how this game theory scenario might influence broader societal dynamics related to the given social issue. Consider potential long-term consequences and policy implications.

7. Propose a Mechanism (3-4 sentences):
   Suggest a mechanism or policy that could potentially lead to a more ethically desirable outcome in this scenario. Explain how it would work and its potential effectiveness.

Ensure your response is creative, ethically nuanced, and grounded in game theory principles. Demonstrate a clear understanding of how advanced technology could impact social dynamics and decision-making processes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The scenario should incorporate {t['technology']} and address the social issue of {t['social_issue']}",
            "The response should include all required sections: Scenario Setup, Game Structure, Payoff Matrix, Ethical Analysis, Nash Equilibrium, Societal Impact, and Proposed Mechanism",
            "The game theory scenario should be logically consistent and demonstrate a clear understanding of game theory principles",
            "The ethical analysis should be nuanced and consider multiple perspectives",
            "The proposed mechanism should be innovative and address the ethical concerns raised in the scenario",
            "The response should demonstrate interdisciplinary thinking, combining elements of technology, ethics, game theory, and social science"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
