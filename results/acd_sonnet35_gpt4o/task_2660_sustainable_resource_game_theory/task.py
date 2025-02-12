import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        resources = ['Freshwater', 'Forests', 'Fish stocks', 'Rare earth metals']
        behavioral_factors = ['Loss aversion', 'Hyperbolic discounting', 'Social norms', 'Prospect theory']
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'resource': random.choice(resources),
                'behavioral_factor': random.choice(behavioral_factors),
                'num_players': random.randint(3, 6),
                'time_horizon': random.randint(5, 20)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a game theory model for sustainable management of {t['resource']}, incorporating the behavioral economics principle of {t['behavioral_factor']}. Your model should involve {t['num_players']} players over a {t['time_horizon']}-year time horizon.

Background:
Game theory is a framework for modeling strategic interactions among rational decision-makers. Behavioral economics incorporates psychological insights into economic models to better predict and explain human behavior.

Your response should include:

1. Game Model Design (300-350 words):
   a) Describe the structure of your game theory model, including players, actions, payoffs, and time dynamics.
   b) Explain how you've incorporated the specified behavioral economics principle into your model.
   c) Detail how your model reflects real-world environmental and economic factors related to {t['resource']} management.
   d) Provide a mathematical formulation of your model, including key variables and at least one equation. Use LaTeX format for equations, e.g., $\\frac{{dR}}{{dt}} = r(1-\\frac{{R}}{{K}}) - H(t)$ for a logistic growth model with harvesting.

2. Equilibrium Analysis (250-300 words):
   a) Identify and describe the equilibrium state(s) of your game under rational player assumptions.
   b) Explain how the incorporation of {t['behavioral_factor']} affects these equilibria.
   c) Discuss the sustainability implications of these equilibrium states.

3. Policy Intervention (200-250 words):
   a) Propose a policy intervention to promote more sustainable outcomes in your model.
   b) Analyze the theoretical impact of this intervention on player behavior and game outcomes.
   c) Discuss potential real-world challenges in implementing such an intervention.

4. Simulation and Results (250-300 words):
   a) Describe a computational approach to simulate your game over the {t['time_horizon']}-year period.
   b) Present and interpret the results of your simulation, including any graphs or data (use ASCII art if needed).
   c) Compare simulation results with and without your proposed policy intervention.

5. Model Limitations and Extensions (150-200 words):
   a) Discuss key limitations of your model and how they might affect its real-world applicability.
   b) Propose at least two potential extensions to your model to address these limitations or expand its scope.

Ensure your response demonstrates a deep understanding of game theory, behavioral economics, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all five sections outlined in the instructions",
            "The game model design must incorporate the specified resource and behavioral factor",
            "The response must include at least one mathematical equation in LaTeX format",
            "The analysis must consider both rational and behaviorally-influenced equilibria",
            "The policy intervention must be clearly described and its impact analyzed",
            "The simulation approach and results must be presented and interpreted",
            "The response must demonstrate interdisciplinary knowledge integration",
            "The proposed model extensions must be relevant and well-reasoned",
            "The response should be within the specified word count range (1150-1400 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0