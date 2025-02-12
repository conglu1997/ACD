import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "climate_factor": "Carbon pricing mechanisms",
                "game_theory_concept": "Nash equilibrium",
                "ai_technique": "Reinforcement learning"
            },
            {
                "climate_factor": "Renewable energy adoption",
                "game_theory_concept": "Shapley value",
                "ai_technique": "Multi-agent systems"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses game theory to model and optimize global climate change mitigation strategies, then analyze its predictions and ethical implications. Focus on the climate factor of {t['climate_factor']}, incorporate the game theory concept of {t['game_theory_concept']}, and utilize the AI technique of {t['ai_technique']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for modeling climate change mitigation strategies.
   b) Explain how it incorporates game theory principles and the specified AI technique.
   c) Detail how the system accounts for the complexity and uncertainty in climate systems.
   d) Discuss how {t['game_theory_concept']} is integrated into your system's decision-making process.

2. Climate Factor Modeling (250-300 words):
   a) Explain how your AI system models and analyzes {t['climate_factor']}.
   b) Describe the key variables and interactions considered in your model.
   c) Discuss how your system handles the long-term nature of climate change and potential tipping points.

3. Strategy Optimization (250-300 words):
   a) Detail how your system uses {t['ai_technique']} to optimize mitigation strategies.
   b) Explain how it balances competing interests of different global actors.
   c) Describe a hypothetical optimal strategy your system might propose for {t['climate_factor']}.

4. Predictive Analysis (200-250 words):
   a) Explain how your system generates and evaluates predictions.
   b) Discuss the potential impact of the optimized strategy on global emissions and climate trajectories.
   c) Address the limitations and uncertainties in your system's predictions.

5. Ethical Implications (200-250 words):
   a) Analyze the ethical considerations of using AI and game theory to guide climate policy.
   b) Discuss potential unintended consequences of implementing the system's recommendations.
   c) Address issues of fairness and equity in the proposed strategies.

6. Real-world Implementation (150-200 words):
   a) Propose how your system could be integrated into existing climate policy frameworks.
   b) Discuss challenges in translating the system's outputs into actionable policies.
   c) Suggest methods for validating and refining the system's performance over time.

Ensure your response demonstrates a deep understanding of climate science, game theory, artificial intelligence, and environmental policy. Be creative in your approach while maintaining scientific plausibility and addressing real-world constraints. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of climate science, game theory, and artificial intelligence, particularly in relation to {t['climate_factor']} and {t['game_theory_concept']}.",
            f"The system architecture should clearly incorporate {t['ai_technique']} and explain how it's integrated into the modeling and optimization process.",
            "The strategy optimization section should provide a plausible and insightful hypothetical strategy for addressing the specified climate factor.",
            "The ethical implications section should thoughtfully address potential consequences and fairness issues of the proposed system.",
            "The response should demonstrate creativity and innovation while maintaining scientific plausibility and real-world applicability."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
