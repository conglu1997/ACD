import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "resource allocation in a small community",
                "behavioral_aspect": "fairness vs. self-interest",
                "num_players": "3-5"
            },
            {
                "context": "information sharing in a competitive market",
                "behavioral_aspect": "trust vs. strategic deception",
                "num_players": "4-6"
            },
            {
                "context": "collective action for climate change mitigation",
                "behavioral_aspect": "short-term vs. long-term benefits",
                "num_players": "5-8"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel economic game that explores {t['behavioral_aspect']} in the context of {t['context']}. Your game should involve {t['num_players']} players. Follow these steps:

1. Game Design (200-250 words):
   a) Describe the basic structure of your game, including rounds and key decisions.
   b) Explain the rules and how points or rewards are allocated.
   c) Discuss how your game incorporates {t['behavioral_aspect']}.
   d) Explain how the game reflects real-world dynamics of {t['context']}.

2. Theoretical Analysis (150-200 words):
   a) Identify the Nash equilibrium (or equilibria) of your game.
   b) Discuss conflicts between individual and collective rationality.

3. Behavioral Predictions (150-200 words):
   a) Predict how human players might deviate from optimal strategies.
   b) Discuss cognitive biases or social factors influencing decisions.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test your game and its predictions.
   b) Describe methodology, sample size, procedure, and controls.
   c) Explain how you would measure and analyze key variables.

5. Implications (100-150 words):
   a) Discuss potential implications for understanding behavior in {t['context']}.
   b) Propose how insights could be applied to real-world decisions.

Format your response using the numbered sections above. Be creative while maintaining scientific rigor. Total response: 800-1050 words.

Example structure (do not copy content):
1. Game Design
   [Your game design here]

2. Theoretical Analysis
   [Your analysis here]

3. Behavioral Predictions
   [Your predictions here]

4. Experimental Design
   [Your experimental design here]

5. Implications
   [Your discussion of implications here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The game design is novel, incorporates {t['behavioral_aspect']}, and reflects {t['context']}.",
            "The theoretical analysis correctly identifies Nash equilibria and discusses rationality conflicts.",
            "Behavioral predictions consider relevant cognitive biases and social factors.",
            "The experimental design is clear, with appropriate methodology and controls.",
            f"Implications for {t['context']} are insightful and applicable to real-world decisions.",
            "The response demonstrates interdisciplinary knowledge of game theory, behavioral economics, and social psychology.",
            "The writing follows the specified structure and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
