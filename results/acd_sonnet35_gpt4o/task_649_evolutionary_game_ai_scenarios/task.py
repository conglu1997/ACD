import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "Predator-Prey Coevolution",
                "evolutionary_principle": "Red Queen Hypothesis",
                "ai_challenge": "Developing adaptive strategies in a constantly changing environment"
            },
            {
                "scenario": "Symbiotic Network Formation",
                "evolutionary_principle": "Mutualism",
                "ai_challenge": "Optimizing collaborative behaviors in a multi-agent system"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a game-theoretic scenario based on the concept of {t['scenario']}, incorporating the evolutionary principle of {t['evolutionary_principle']} and addressing the AI challenge of {t['ai_challenge']}. Your response should include:

1. Scenario Design (200-250 words):
   a) Describe the game-theoretic scenario in detail, explaining how it relates to {t['scenario']}.
   b) Explain how the {t['evolutionary_principle']} is incorporated into the scenario.
      Note: The Red Queen Hypothesis suggests that organisms must constantly adapt and evolve to survive against ever-evolving opposing organisms.
      Mutualism refers to a symbiotic relationship where both species benefit from the interaction.
   c) Outline the specific {t['ai_challenge']} within this context.

2. Game Mechanics (150-200 words):
   a) Define the key elements of the game (e.g., players, actions, payoffs).
   b) Explain how these elements reflect both evolutionary and AI principles.
   c) Provide a mathematical representation of the game (e.g., payoff matrix or game tree). Use LaTeX notation for any mathematical formulas.

3. Evolutionary Dynamics (200-250 words):
   a) Describe how strategies might evolve over time in this scenario.
   b) Explain any equilibrium states or evolutionary stable strategies.
   c) Discuss how the {t['evolutionary_principle']} influences these dynamics.

4. AI Strategy Proposal (250-300 words):
   a) Propose an AI approach to develop successful strategies in this scenario.
   b) Explain how your AI system would adapt to the evolutionary dynamics.
   c) Describe any specific algorithms or techniques your AI would employ.
   d) Address how your AI approach tackles the {t['ai_challenge']}.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential real-world applications of your scenario and AI strategy.
   b) Address any ethical considerations in implementing such an AI system.
   c) Suggest guidelines for responsible development and use of evolutionary game AI.

6. Conclusion (50-100 words):
   Summarize the key insights from your analysis, highlighting the interplay between game theory, evolutionary biology, and artificial intelligence in your scenario.

Ensure your response demonstrates a deep understanding of game theory, evolutionary biology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your scenario design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The scenario effectively incorporates the evolutionary principle of {t['evolutionary_principle']} and addresses the AI challenge of {t['ai_challenge']}.",
            "The game mechanics and evolutionary dynamics are well-defined and scientifically plausible.",
            "The proposed AI strategy demonstrates creativity and a deep understanding of both evolutionary principles and AI techniques.",
            "The response shows interdisciplinary knowledge synthesis and strategic thinking in addressing the complex scenario.",
            "The conclusion effectively summarizes the key insights from the analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
