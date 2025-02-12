import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Climate Change Mitigation",
                "description": "Multiple countries must decide whether to invest in expensive green technologies. The benefit of reduced climate change is shared globally, but the cost is borne individually.",
                "num_agents": 5,
                "rounds": 10
            },
            {
                "name": "Public Health Crisis",
                "description": "During a pandemic, individuals must choose whether to follow social distancing guidelines. The benefit of reduced transmission is shared by all, but the cost of isolation is individual.",
                "num_agents": 7,
                "rounds": 15
            },
            {
                "name": "Open Source Software Development",
                "description": "Tech companies must decide whether to contribute resources to open source projects. The benefits of improved software are shared industrywide, but the costs are borne by individual companies.",
                "num_agents": 4,
                "rounds": 8
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a multi-agent social dilemma scenario based on the following situation:

{t['name']}: {t['description']}

Number of agents: {t['num_agents']}
Number of rounds: {t['rounds']}

Your task is to design a game-theoretic model for this scenario and predict its outcomes. Follow these steps:

1. Model Design (200-250 words):
   a) Define the possible actions for each agent in each round.
   b) Specify the payoff structure for different combinations of actions.
   c) Explain how the payoffs reflect the social dilemma nature of the scenario.
   d) Describe any additional rules or constraints in your model.

2. Behavioral Factors (150-200 words):
   a) Identify 2-3 relevant behavioral economics principles or cognitive biases that might influence agents' decisions in this scenario.
   b) Explain how these factors could affect the agents' choices and the overall outcome.

3. Equilibrium Analysis (200-250 words):
   a) Determine the Nash equilibrium (or equilibria) for a single round of your game.
   b) Discuss whether this equilibrium is Pareto optimal.
   c) Explain how the multi-round nature of the game might affect strategic choices.

4. Outcome Prediction (200-250 words):
   a) Predict the likely outcome of the game over the specified number of rounds.
   b) Explain your reasoning, considering both game-theoretic principles and behavioral factors.
   c) Discuss any potential tipping points or critical thresholds in your model.

5. Policy Implications (150-200 words):
   a) Based on your analysis, propose a policy intervention that could improve the outcome of this social dilemma.
   b) Explain how your proposed intervention addresses the underlying incentive structure or behavioral factors.
   c) Discuss any potential unintended consequences of your proposed intervention.

Ensure your response demonstrates a deep understanding of game theory, behavioral economics, and the specific scenario. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining logical consistency and real-world plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all five required sections",
            "The model design should be logically consistent and reflect the social dilemma nature of the scenario",
            "The behavioral factors identified should be relevant and well-explained",
            "The equilibrium analysis should be mathematically sound and insightful",
            "The outcome prediction should consider both game-theoretic and behavioral factors",
            "The proposed policy intervention should be creative, well-reasoned, and address the core issues of the dilemma",
            "The overall response should demonstrate a deep understanding of game theory and behavioral economics"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
